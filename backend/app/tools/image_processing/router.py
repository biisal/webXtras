from typing import Dict
from loguru import logger
from fastapi import APIRouter , File , UploadFile , HTTPException, Form
from fastapi.responses import StreamingResponse


from app.tools.image_processing.model import (
    ImageCompressRequest,
    ImageResizeRequest,
)
from app.tools.image_processing.utils import (
    compress_image, 
    resize_image
)

router = APIRouter()

@router.post("/compress")
async def compress(image : UploadFile = File(...),
    quality: int= Form(80, ge=1, description="Quality of the pdf file in percentage."),
) -> Dict[str, int | str]:
    
    """
    **Compress an image to the specified quality.**

    `Parameters`:
    - **image**: UploadFile - The image file to be compressed. Must be a valid image format (e.g., JPEG, PNG).
    - **quality**: - Quality of the compressed image in percentage.

    `Returns`:
    - **Dict[str, int | str]**: A JSON response containing the size of the original and compressed images and the quality of the compressed image.
    """
    
    if image.content_type is None or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file")
    try:
        data:dict[str, int | str] = await compress_image(image, quality)
        return data
    except Exception as e:
        logger.error(f"Error compressing image: {e=}")
        raise HTTPException(status_code=500, detail="Failed to compress image!")
    
@router.post("/resize")
async def resize(image : UploadFile = File(...) ,
    width: int= Form(612, ge=1, description="Width of resized image in pixels."),
    height: int= Form(792, ge=1, description="Height of resized image in pixels."),
    ) -> StreamingResponse:
    """
    **Resize an image to the specified width and height.**

    `Parameters`:
    - **image**: UploadFile - The image file to be compressed. Must be a valid image format (e.g., JPEG, PNG).
    - **width**: - Width of resized image in pixels.
    - **height**: - Height of resized image in pixels.

    `Returns`:
    - **StreamingResponse**: A response stream containing the resized image file.
    """

    if image.content_type is None or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file")
    
    if not width or not height:
        raise HTTPException(status_code=400, detail="Please provide both width and height in px")
    
    try:
        size = (width, height)
        buffer = resize_image(image, size)
        return StreamingResponse(buffer, media_type="image/jpeg")
    except Exception as e:
        logger.error(f"Error resizing image: {e=}")
        raise HTTPException(status_code=500, detail="Failed to resize image!")