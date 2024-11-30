from loguru import logger
from fastapi import APIRouter , File , UploadFile , HTTPException, Form
from fastapi.responses import StreamingResponse

from app.pdf_processing.utils import (
    extract_text_from_pdf
)

router = APIRouter()

@router.post("/extract_text")
async def extract_pdf_text(
    file: UploadFile = File(...),
    page_number: int= Form(..., ge=0, description="Page number to extract text from (0-based index)."),
):
    """
    **Extract text from a specific page of a PDF file**.

    `Parameters`:
    - **file**: UploadFile - The uploaded PDF file.\n
    - **page_number**: - Contains the page number to extract text from.\n

    `Returns`:
    - Extracted text as a JSON response.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid PDF.")


    try:
        pdf_bytes = await file.read()
        extracted_text = extract_text_from_pdf(pdf_bytes, page_number)

        return {
            "message": "Text extracted successfully.",
            "page_number": page_number,
            "extracted_text": extracted_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
    