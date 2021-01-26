# py-pdf-toc-bookmarks

## Python Development Environment

### conda

To create a new conda environment from the provided `environment.yml`:

```sh
conda env create -f environment.yml
```

Activate the environment:

```sh
conda activate pdf-toc
```

To update the environment with any changes to `environment.yml`:

```sh
conda env update pdf-toc -f environment.yml --prune
```

### venv

Create new virtual environment

```sh
python -m venv .venv
```

Activate the environment:

```sh
# Unix (bash)
source .venv/bin/activate
# Windows
.venv\Scripts\activate.bat
```

Install requirements with pip:

```sh
pip install -r requirements.txt
```

Update requirements:

```sh
pip install -r requirements.txt --upgrade
```

## Adding bookmarks to PDFs

Download [JPdfBookmarks](https://sourceforge.net/p/jpdfbookmarks)

This script does the work of creating a `*-bookmarks.txt` file for `JPdfBookmarks`. Each line is a bookmark and the hierarchy is made by tab characters (not spaces), in the format: `<Title of bookmark/target page[,FitType,TopOffset,LeftOffset]`

See `JPdfBookmarks`' documentation for details on running the CLI.

### Example execution of `jpdfbookmarks_cli`

```sh
(base) D:\_dev\_wsuv\wsu-textbooks\jpdfbookmarks-2.5.2>jpdfbookmarks_cli.exe -a ..\..\..\py-pdf-toc-bookmarks\cs-455_computer-networking-bookmarks.txt ..\2020-21_2-Spring\cs-455_computer-networking.pdf -o ..\2020-21_2-Spring\cs-455_computer-networking-wbookmarks.pdf
```
