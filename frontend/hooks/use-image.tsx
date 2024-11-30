"use client";
import { create } from 'zustand';
interface CompressedImageState {
    original_size: string,
    compressed_size: string,
    quality: number,
    compressed_url: string,
}
interface ImageStore {
    compressedImage: CompressedImageState | null
    compress: (image: File, quality: number) => Promise<CompressedImageState | null>;
    error: string | null
}



export const useImage = create<ImageStore>((set) => ({
    compressedImage: null,
    error: null,
    compress: async (image: File, quality: number) => {
        set({ compressedImage: null, error: null });
        try {
            const url = `http://127.0.0.1:8000/image/compress?quality=${quality}`;
            const formData = new FormData();
            formData.append('image', image);
            // no cache
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
                cache: 'no-store',
                headers: {
                    "Cache-Control": "no-store",
                }
            },);
            if (response.ok) {
                const data = (await response.json()) as CompressedImageState;
                set({ compressedImage: data });
                return data;

            }
            set({
                compressedImage: null, error: "Error compressing image"
            });

            return null;

        } catch (error) {
            console.log(error);
            set({ compressedImage: null, error: "Error compressing image" });
            return null;

        }
    }
}));