# py-pdf-toc-bookmarks

## Adding bookmarks to PDFs

Download [JPdfBookmarks](https://sourceforge.net/p/jpdfbookmarks)

This script does the work of creating a `*-bookmarks.txt` file for `JPdfBookmarks`. Each line is a bookmark and the hierarchy is made by tab characters (not spaces), in the format: `<Title of bookmark/target page[,FitType,TopOffset,LeftOffset]`

See `JPdfBookmarks`' documentation for details on running the CLI.

### Example execution of `jpdfbookmarks_cli`

```sh
(base) D:\_dev\_wsuv\wsu-textbooks\jpdfbookmarks-2.5.2>jpdfbookmarks_cli.exe -a ..\..\..\py-pdf-toc-bookmarks\cs-455_computer-networking-bookmarks.txt ..\2020-21_2-Spring\cs-455_computer-networking.pdf -o ..\2020-21_2-Spring\cs-455_computer-networking-wbookmarks.pdf
```
