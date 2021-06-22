# GenDoc

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fe0fd43e86524234bf0baf11e1061511)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=http-samc/GenDoc&amp;utm_campaign=Badge_Grade)[![PyPI version](https://badge.fury.io/py/GenDoc.svg)](https://badge.fury.io/py/GenDoc)

 - Generate a Markdown Documentation file from a Python Repository with DocStrings.
 - Pure 🐍 implementation with no external packages
 - *Tiny* Tech Stack: os, ast, argparse, typing

## Installation
```Python
pip install gendoc
--
pip3 install gendoc
```

## Use
**GenDoc** is a CLI based application. After installation, you can call the utility in any terminal application as follows:
`PS C:\users\...\foo> gendoc`<br>
Additionaly, you can use the following flags in your terminal:

---
|Flag(s)    |Description   |
|  ---  |  ---  |
|`--help`, `-h`|Show a help dialog|
|`--name`, `--n`|**Project Name** (included in Docs) (not included if not provided)|
|`--version`, `--v`|**Version Number** (included in Docs) (_Project Name_ required to use) (not included if not provided)|
|`--files`, `--f`|PATH to specific files you want to include in the Doc generation (only pulls from these files) (defaults to all `.py` files in the current directory)|
|`--dir`, `--d`|PATH to the parent directory of the codebase (defaults to all `.py` files in the current directory)|
|`--output`, `--o`|PATH to the output Markdown file (defaults to DOCS.md in current directory)|
|`--emptyfunc`, `--e`|Message for function without a DocString (enter multiple words surrounded by "Quotes") (accepts markdown syntax) (defaults to "*No documentation provided.*")|
|`--classSections`, `--cs`|Add collapseable sections for classes (not generated if not called)|
|`--methodSections`, `--ms`|Add collapseable sections for class methods (not generated if not called)|
|`--funcSections`, `--fs`|Add collapseable sections for functions (not generated if not called)|
|`--fileHeaders`, `--fh`|Add file name & relative path above it's classes and functions (creates GitHub-safe clickable link) (not generated if not called)|
### Notes:
- Use either `--files` or `--dir`, never both
  - `--dir` is used to change the directory and then scrape all files within it
  - `--files` is used to specify specific files to scrape (not the entire directory)
  - If you'd like to scrape specific files in a separate directory, simply use `--files` with their absolute PATHs
- `--files` can take in multiple file parameters, simply enter a space between each one
- Anytime a PATH is requested, it does **not** need to be in the current directory, **both** relative and absolute PATHs are accepted
- If you'd like to exclude any functions that do **not** have their own DocString, you can use the `--emptyfunc` flag and pass in the value **`0`**
- The current default behavior is to exclude any files that do **not** contain any functions or classes
- Clickable links generated with `--fileHeaders` might break if you are using a different directory or placing `DOCS.md` in a nested directory

## Future Development
**GenDoc** was developed to be a simple, plug-and-play package. However, due to the level of styling customization required for many projects' documentation, an additional html-based API is being developed so developers can use their own external stylesheets.

PRs are welcome, and please contact [Samarth Chitgopekar](mailto:sam@chitgopekar.tech) for any questions, comments, or concerns.