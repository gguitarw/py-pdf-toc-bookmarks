
import re
from pathlib import Path
from typing import Iterable, List, Tuple, Union

import pdfplumber


PDF_PATH = 'cs-455_computer-networking.pdf'
PATTERN = "^(\\d(?:\\.\\d)+)\\s+(.*)\\s+(\\d+)$"
REGEX = re.compile(PATTERN)
TOC_START = 18
TOC_END = 24


TocEntry = Tuple[str, str, int]


def extract_lines(page_text: str) -> List[TocEntry]:
    for line in page_text.strip().split('\n'):
        match = REGEX.match(line)
        if match is not None:
            groups = match.groups()
            print(groups)
        # print(match)
        # print(f'"{line}"')


def extract_toc(pdf_path, toc_pages: Iterable[int]):
    toc_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in toc_pages:
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


def create_toc_txt(pdf_path: Union[str, Path], toc_pages: Iterable[int]):
    toc = extract_toc(pdf_path, toc_pages)
    print(toc)


if __name__ == '__main__':
    create_toc_txt(PDF_PATH, range(TOC_START, TOC_END + 1))
