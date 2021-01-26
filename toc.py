
import pdfplumber

pdf_path = 'cs-455_computer-networking.pdf'
toc_start = 18
toc_end = 24

with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[toc_start]
    # print(first_page.chars[0])
    first_text = first_page.extract_text()
    print(first_text)
