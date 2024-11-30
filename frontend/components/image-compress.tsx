"use client";

import { useState, ChangeEvent, useTransition } from "react";
import { useImage } from "@/hooks/use-image";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import Image from "next/image";
import { Loader2 } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";



const ImageCompress = () => {
  const { compress, compressedImage, error } = useImage();
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [quality, setQuality] = useState<number>(50);
  const [isPending, startTransition] = useTransition();
  const { toast } = useToast();

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
      startTransition(async () => {
        try {
          const image_data = await compress(selectedImage, quality);
          if (image_data?.compressed_url)
            toast({
              title: "Image compressed successfully",
              description: "Your image has been compressed and is ready for download.",
            });
          else
            toast({
              title: error as string,
              description: "There was an error compressing your image. Please try again.",
              variant: "destructive",
            });
        } catch (error) {
          console.error("Error compressing image:", error);
          toast({
            title: error as string,
            description: "There was an error compressing your image. Please try again.",
            variant: "destructive",
          });
        }
      });
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
        <Button onClick={handleCompress} disabled={!selectedImage || isPending}>
          {isPending ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Compressing...
            </>
          ) : (
            "Compress Image"
          )}
        </Button>
        {compressedImage && (
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Compressed Image</h3>
            <div className="max-w-full h-60 relative">
              <Image
                src={compressedImage.compressed_url}
                alt="Compressed"
                fill
                className="rounded-md object-cover"
              />
            </div>
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <p className="font-medium">Original Size</p>
                <p>{compressedImage.original_size}</p>
              </div>
              <div>
                <p className="font-medium">Compressed Size</p>
                <p>{compressedImage.compressed_size}</p>
              </div>
              <div>
                <p className="font-medium">Quality</p>
                <p>{compressedImage.quality}%</p>
              </div>
            </div>
            <Button asChild className="w-full">
              <a
                href={compressedImage.compressed_url}
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

