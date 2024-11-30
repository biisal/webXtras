"use client";

import { useState, ChangeEvent, useTransition } from "react";
import { useImage } from "@/hooks/use-image";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import Image from "next/image";

const ImageCompress = () => {
  const { compress } = useImage();
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [quality, setQuality] = useState<number>(50);
  const [compressedImageUrl, setCompressedImageUrl] = useState<string | null>(null);
  const [pending, setTransition] = useTransition();

  const handleImageChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedImage(e.target.files[0]);
    }
  };

  const handleQualityChange = (value: number[]) => {
    setQuality(value[0]);
  };

  const handleCompress = async () => {
    if (selectedImage) {
      setTransition(async () => {
        try {
          const compressedUrl = await compress(selectedImage, quality);
          setCompressedImageUrl(compressedUrl);
        } catch (error) {
          console.error("Error compressing image:", error);
        }
      })
    }
  };

  return (
    <Card className="max-w-md mx-auto mt-8">
      <CardHeader>
        <CardTitle>Image Compressor</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="image-upload">Select Image</Label>
          <Input
            id="image-upload"
            type="file"
            accept="image/*"
            onChange={handleImageChange}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="quality-slider">Quality: {quality}%</Label>
          <Slider
            id="quality-slider"
            min={10}
            max={80}
            step={10}
            value={[quality]}
            onValueChange={handleQualityChange}
          />
        </div>
        <Button onClick={handleCompress} disabled={!selectedImage || pending}>
          Compress Image
        </Button>
        {compressedImageUrl && (
          <div className="space-y-2">
            <h3 className="text-lg font-semibold">Compressed Image</h3>
            <div className="max-w-full h-60 relative">
              <Image
                src={compressedImageUrl}
                alt="Compressed"
                fill
                className="rounded-md object-cover"
              />
            </div>
            <Button asChild>
              <a
                href={compressedImageUrl}
                download="compressed_image"
              >
                Download Compressed Image
              </a>
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default ImageCompress;

