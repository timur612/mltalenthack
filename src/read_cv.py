from spire.doc.common import *
from spire.doc import *

from PyPDF2 import PdfReader


def read_cv(doc_path: str) -> str:
    doc_type = doc_path.split(".")[0]

    extracted_text = ""
    if doc_type == "docx" or doc_type == "doc":
        doc = Document()
        doc.LoadFromFile(doc_path)
        extracted_text = doc.GetText()

    elif doc_type == "pdf":
        pdf = PdfReader(doc_path)

        for i in range(len(pdf.pages)):
            extracted_text += pdf.pages[i].extract_text()

    return extracted_text
