# GenDoc

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fe0fd43e86524234bf0baf11e1061511)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=http-samc/GenDoc&amp;utm_campaign=Badge_Grade) [![PyPI version](https://badge.fury.io/py/GenDoc.svg)](https://badge.fury.io/py/GenDoc) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![platform: independent](https://img.shields.io/endpoint?url=https%3A%2F%2Fapi.jsonbin.io%2Fb%2F6042e0a7121bf907dd96fa4a%2F13)

 - Generate a Markdown Documentation file from a Python Repository with DocStrings.
 - Pure 🐍 implementation with no external packages
 - *Tiny* Tech Stack: os, ast, argparse, typing

## Installation
Use **pip** in your terminal to install GenDoc. The commands are listed below:
|Windows|Linux|MacOS|
|---|---|---|
|`pip install gendoc`|`pip3 install gendoc`|`pip3 install gendoc`|

## Use
**GenDoc** is a CLI based application. After installation, you can call the utility in any terminal application as follows:
|Windows|Linux|MacOS|
|---|---|---|
`C:\> gendoc`|`user@ubuntu:~$ gendoc`|`mac:~ user$ gendoc`|
- In all of these cases, you should be using **`cd`** to set your terminal directory to your project folder - otherwise you'll have to use the `--files` or `--dir` commands to specify your Python programs in order to avoid generating documentation for every single `.py` file on your computer!

##### You can also use any of the following flags in your terminal to customize your output (optional):

---
|Flag(s)|Value|Description|
|  ---  |  ---  | --- |
|`--help`, `-h`|`{None}`|Show a help dialog|
|`--name`, `--n`|`{str}`|**Project Name** (included in Docs) (not included if not provided)|
|`--version`, `--v`|`{str}`|**Version Number** (included in Docs) (_Project Name_ required to use) (not included if not provided)|
|`--files`, `--f`|`{str} {str (opt)} ...`|PATH to specific files you want to include in the Doc generation (separate by a single space if adding multiple files) (only pulls from these files) (defaults to all `.py` files in the current directory)|
|`--dir`, `--d`|`{str}`|PATH to the parent directory of the codebase (defaults to all `.py` files in the current directory)|
|`--output`, `--o`|`{str}`|PATH to the output Markdown file (defaults to DOCS.md in current directory)|
|`--emptyfunc`, `--e`|`"{str}"`|Message for function without a DocString (enter multiple words surrounded by "Quotes") (accepts markdown syntax) (defaults to "*No documentation provided.*")|
|`--classSections`, `--cs`|`{None}`|Add collapseable sections for classes (not generated if not called)|
|`--methodSections`, `--ms`|`{None}`|Add collapseable sections for class methods (not generated if not called)|
|`--funcSections`, `--fs`|`{None}`|Add collapseable sections for functions (not generated if not called)|
|`--fileHeaders`, `--fh`|`{None}`|Add file name & relative path above it's classes and functions (creates GitHub-safe clickable link) (not generated if not called)|
|`--codeFence`, `--cf`|`{None}`|Surround all DocStrings in a Python markdown code fence (not generated if not called)|
### Notes:
- Use either `--files` or `--dir`, never both
  - `--dir` is used to change the directory and then scrape all files within it
  - `--files` is used to specify specific files to scrape (not the entire directory)
  - If you'd like to scrape specific files in a separate directory, simply use `--files` with their absolute PATHs
- Anytime a PATH is requested, it does **not** need to be in the current directory, **both** relative and absolute PATHs are accepted
- If you'd like to exclude any functions that do **not** have their own DocString, you can use the `--emptyfunc` flag and pass in the value **`0`**
- The current default behavior is to exclude any files that do **not** contain any functions or classes
- Clickable links generated with `--fileHeaders` might break if you are using a different directory with the `--dir` flag or placing `DOCS.md` in a different directory with the `--output` flag
- If you aren't using markdown-styled DocStrings, passing the `--codeFence` flag will help auto-emphasize Python keywords, such as str, int, class, etc.

## Future Development
**GenDoc** was developed to be a simple, plug-and-play package. However, due to the level of styling customization required for many projects' documentation, an additional html-based API is being developed so developers can use their own external stylesheets.

PRs are welcome, and please contact [Samarth Chitgopekar](mailto:sam@chitgopekar.tech) for any questions, comments, or concerns.

---
<body>
  <p style="background-color: #E3E3E3; border: 8px solid #E3E3E3; border-radius: 5px; line-height:200%;">
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Python</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">DocStrings</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Generate DocStrings</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Python Markdown DocStrings</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">DocStrings to Markdown</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Documentation Generator</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">DocStrings Markdown</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Elegant Docs</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Module Doc Generator</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Pure Python</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">DocString Scraper</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Python Doc Generator</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">PyPI DocString Generator</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Markdown Docs</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Easy API Documentation Generator</a>
    <a style="border: 4px solid #121212; background-color: #121212; color: #d8e5e6; border-radius: 5px;">Package Doc Generator</a>
  </p>
</body>