"use client";
import { create } from 'zustand';

interface ImageStore {
    // url: string | null;
    compress: (image: File, quality: number) => Promise<string | null>;
}

export const useImage = create<ImageStore>(() => ({
    compress: async (image: File, quality: number) => {
        const url = 'http://127.0.0.1:8000/image/compress';
        const formData = new FormData();
        formData.append('image', image);
        formData.append('quality', quality.toString());

        const response = await fetch(url, {
            method: 'POST',
            body: formData,
        });
        if (response.ok) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            console.log("url", url);
            return url || null;
        }
        return null;

    }
}));