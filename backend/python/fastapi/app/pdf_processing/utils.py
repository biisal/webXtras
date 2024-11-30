import pymupdf
from fastapi import HTTPException

def extract_text_from_pdf(pdf_bytes, page_number) -> str:
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