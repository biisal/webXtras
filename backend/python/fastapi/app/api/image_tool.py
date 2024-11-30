from typing import Dict
from fastapi import APIRouter , File , UploadFile , HTTPException
from fastapi.responses import StreamingResponse 
from PIL import Image
import io
router = APIRouter()

@router.post("/compress")
async def compress(image : UploadFile = File(...) , quality : int = 80 ) -> StreamingResponse:
    if image.content_type is None or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file")
    try:
        pil_image =Image.open(image.file)
        buffer = io.BytesIO()
        pil_image.save(buffer , pil_image.format , quality = quality)
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/jpeg")
    except Exception as e:
        print("Error compressing image:", e)
        raise HTTPException(status_code=500, detail="Failed to compress image!")


