# GenDoc
 Generate a Markdown Documentation file from a Python Repository with DocStrings.

# Installation
```Python
pip install gendoc
--
pip3 install gendoc
```

# Use
GenDoc is a CLI based application using ArgParse. After installation, you can call the utility in any terminal application as follows: 
```
C:\...\foo> gendoc
```
Aditionaly, you can use the following flags in your terminal:

---
``--help`` | ``-h`` - Show a help dialog<br>
``--name`` | ``--n`` - Project Name (included in Docs) (not included if not provided)<br>
``--version`` | ``--v`` - Version Number (included in Docs) (Project Name required to use) (not included if not provided)<br>
``--files`` | ``--f`` - PATH to specific files you want to include in the generation (only pulls from these files) (defaults to all .py files in the current directory)<br>
``--dir`` | ``--d`` - PATH to the parent directory of the codebase (used only without --f) (defaults to all .py files in the current directory)<br>
``--output`` | ``--o`` - PATH to the output Markdown file (defaults to DOCS.md in current directory)<br>
``--emptyfunc`` | ``--e`` - Message for function without a DocString (enter 0 to exclude functions without a DocString entirely) (defaults to "*No documentation provided.*")<br>