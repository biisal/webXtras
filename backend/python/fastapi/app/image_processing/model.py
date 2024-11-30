from pydantic import BaseModel

class ImageCompressRequest(BaseModel):
    quality: int = 80

class ImageResizeRequest(BaseModel):
    width: int = 80
    height: int = 80