import io
from PIL import Image

def compress_image(image, quality: int) -> io.BytesIO:
    pil_image = Image.open(image.file)
    buffer = io.BytesIO()
    pil_image.save(buffer , pil_image.format , quality = quality)
    buffer.seek(0)

    return buffer

def resize_image(image, size: [int, int]) -> io.BytesIO:
    pil_image = Image.open(image.file)
    resized_img = pil_image.resize(size, Image.ANTIALIAS)

    buffer = io.BytesIO()
    resized_img.save(buffer , pil_image.format)
    buffer.seek(0)

    return buffer