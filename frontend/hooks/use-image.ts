"use client";
import { create } from 'zustand';

interface CompressedImageState {
    original_size: string;
    compressed_size: string;
    quality: number;
    compressed_url: string;
}

interface ImageStore {
    compressedImage: CompressedImageState | null;
    error: { title: string, description: string } | null;
    compress: (image: File, quality: number) => Promise<CompressedImageState | null>;
}

export const useImage = create<ImageStore>((set) => ({
    compressedImage: null,
    error: null,
    compress: async (image: File, quality: number) => {
        set({ compressedImage: null, error: null });
        try {
            const url = 'http://127.0.0.1:8000/api/image/compress';
            const formData = new FormData();
            formData.append('image', image);
            formData.append('quality', quality.toString());

            const response = await fetch(url, {
                method: 'POST',
                body: formData,
                cache: 'no-store'
            });
            if (response.ok) {
                const data: CompressedImageState = await response.json();
                set({ compressedImage: data, error: null });
                return data;
            }
            set({ error: { title: "Error compressing image", description: "There was an error compressing your image. Please try again." } });
            return null;
        } catch (error) {
            console.error('Error compressing image:', error);
            set({ error: { title: "Internal Server Error", description: "There was an internal server error.Plese try again later" } });
            return null;
        }

    }
}));