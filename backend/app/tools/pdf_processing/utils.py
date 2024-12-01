import pymupdf
from fastapi import HTTPException

def extract_text_from_pdf(pdf_bytes, page_number) -> str:
    """
    Extract text from a specific page of a PDF document.

    Parameters:
    - pdf_bytes: The bytes of the PDF file to be processed.
    - page_number: The page number from which to extract text (0-based index).

    Returns:
    - The extracted text from the specified page as a string.

    Raises:
    - HTTPException: If the provided page number exceeds the number of pages in the PDF.
    """
    pdf_document = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        
    if page_number > pdf_document.page_count:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid page number. The PDF has {pdf_document.page_count} pages."
        )

    page = pdf_document[page_number]
    extracted_text = page.get_text("text")
    
    pdf_document.close()
    return extracted_text