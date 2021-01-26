
import re
from pathlib import Path
from typing import Iterable, List, Match, Tuple, Union

import pdfplumber


PDF_PATH = 'cs-455_computer-networking.pdf'
CHAPTER_PATTERN = "^(Chapter \\d)\\s+(.*)\\s+(\\d+)$"
CHAPTER_REGEX = re.compile(CHAPTER_PATTERN)
SECTION_PATTERN = "^(\\d(?:\\.\\d+)+)\\s+(.*)\\s+(\\d+)$"
SECTION_REGEX = re.compile(SECTION_PATTERN)
OTHER_PATTERN = "^(.*)\\s+(\\d+)$"
OTHER_REGEX = re.compile(OTHER_PATTERN)
TOC_START = 18
TOC_END = 24


# Level, Text, Page
TocEntry = Tuple[int, str, int]


def extract_line(line: str) -> Union[TocEntry, None]:
    if (match := CHAPTER_REGEX.match(line)) is not None:
        # Chapter n text page
        groups = match.groups()
        text = f'{groups[0]} {groups[1].strip()}'
        return (0, text, int(groups[2]))
    elif (match := SECTION_REGEX.match(line)) is not None:
        # a.b.c text page
        groups = match.groups()
        level = groups[0].count('.') + 1
        text = f'{groups[0]} {groups[1].strip()}'
        return (level, text, int(groups[2]))
    elif (match := OTHER_REGEX.match(line)) is not None:
        # text page
        groups = match.groups()
        return (1, groups[0].strip(), int(groups[1]))
    else:
        return None

    # match = CHAPTER_REGEX.match(line)
    # if match is not None:
    #     groups = match.groups()
    #     print(groups)
    # print(match)
    # print(f'"{line}"')


def extract_lines(page_text: str) -> List[TocEntry]:
    lines = []
    for line in page_text.strip().split('\n'):
        extracted = extract_line(line)
        if extracted is not None:
            lines.append(extracted)
    return lines


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


if __name__ == '__main__':
    create_toc_txt(PDF_PATH, range(TOC_START, TOC_END + 1))
