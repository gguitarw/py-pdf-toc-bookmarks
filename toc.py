
from pathlib import Path
from typing import List, Tuple, Union
import pdfplumber

PDF_PATH = 'cs-455_computer-networking.pdf'
TOC_START = 18
TOC_END = 24


def extract_lines(page_text: str) -> List[str]:
    for line in page_text.strip().split('\n'):
        print(f'"{line}"')
    return ['a']


def extract_toc(pdf_path, toc_range):
    toc_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(toc_range):
            page = pdf.pages[page_num]
            text = page.extract_text()
            toc_lines.extend(extract_lines(text))

        # page_num = pdf.pages[toc_start]
        # print(first_page.chars[0])

        # toc_text = page_num.extract_text()
        # print(toc_text)
        # for line in toc_text.strip().split('\n'):
        #     print(f'"{line}"')

        # toc_table = toc_page.extract_tables()
        # print(toc_table)

    return toc_lines


def create_toc_txt(pdf_path: Union[str, Path], toc_range: Tuple[int, int]):
    toc = extract_toc(pdf_path, toc_range)
    print(toc)


if __name__ == '__main__':
    create_toc_txt(PDF_PATH, (TOC_START, TOC_END + 1))
