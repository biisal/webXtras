import io
from typing import List
from PIL import Image
from fastapi import UploadFile
import base64

def format_size(size):
    calculated_size: float = round(size / (1024 * 1024), 2)
    return f"{calculated_size * 1024} KB" if calculated_size < 1 else f"{calculated_size} MB"


async def compress_image(image : UploadFile, quality: int) -> dict[str , int | str ]:
    with io.BytesIO(await image.read()) as temp_file:
            pil_image = Image.open(temp_file)
            original_size = image.file.seek(0, io.SEEK_END)
            image.file.seek(0)
            buffer = io.BytesIO()
            pil_image.save(buffer, format=pil_image.format, quality=quality)
            buffer.seek(0)
            compressed_size = len(buffer.getvalue()) 
            compressed_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            compressed_url = f"data:image/{pil_image.format.lower() if pil_image.format else 'jpeg'};base64,{compressed_base64}"
            image.file.seek(0)
            image.file.truncate()
            data ={
                "original_size": format_size(original_size),
                "compressed_size": format_size(compressed_size),
                "quality": quality,
                "compressed_url": compressed_url
            }
    return data

def resize_image(image, size: tuple[int, int]) -> io.BytesIO:
    pil_image = Image.open(image.file)
    resized_img = pil_image.resize(size, Image.Resampling.LANCZOS)
    buffer = io.BytesIO()
    resized_img.save(buffer , pil_image.format)
    buffer.seek(0)

    return buffer