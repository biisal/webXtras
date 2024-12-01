import asyncio
from typing import Dict, Any
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
import io
import base64
import logging
logger = logging.getLogger(__name__)

router = APIRouter()

def format_size(size_in_bytes):
    calculated_size: float = round(size_in_bytes / (1024 * 1024), 2)
    return f"{calculated_size * 1024} KB" if calculated_size < 1 else f"{calculated_size} MB"

@router.post("/compress", response_model=None)  # Disable response model generation
async def compress(image: UploadFile = File(...), quality: int = 80) -> Dict[str, Any]:
    if image.content_type is None or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file")
    try:
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
    except Exception as e:
        logger.error(f"Failed to compress image: {e}")
        raise HTTPException(status_code=500, detail="Failed to compress image!")
