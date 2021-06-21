# GenDoc
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
``PS C:\users\...\foo> gendoc``<br>
Aditionaly, you can use the following flags in your terminal:

---
``--help`` | ``-h`` Show a help dialog<br>
``--name`` | ``--n`` **Project Name** (included in Docs) (not included if not provided)<br>
``--version`` | ``--v`` **Version Number** (included in Docs) (_Project Name_ required to use) (not included if not provided)<br>
``--files`` | ``--f`` PATH to specific files you want to include in the Doc generation (only pulls from these files) (defaults to all .py files in the current directory)<br>
``--dir`` | ``--d`` PATH to the parent directory of the codebase (used only without --f) (defaults to all .py files in the current directory)<br>
``--output`` | ``--o`` PATH to the output Markdown file (defaults to DOCS.md in current directory)<br>
``--emptyfunc`` | ``--e`` Message for function without a DocString (enter **0** to exclude functions without a DocString entirely) (defaults to "*No documentation provided.*")<br>

## Future Development
**GenDoc** was developed to be a simple, plug-and-play package. However, due to the level of styling customization required for many projects' documentation, an additional html-based API is being developed so developers can use their own external stylesheets.

PRs are welcome, and please contact [Samarth Chitgopekar](mailto:sam@chitgopekar.tech) for any questions, comments, or concerns.