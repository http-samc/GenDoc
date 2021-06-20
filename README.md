# GenDoc
 Generate a Markdown Documentation file from a Python Repository with docstrings.

# Installation
```Python
pip install gendoc
--
pip3 install gendoc
```

# Use
GenDoc is a CLI based application using ArgParse. After installation, you can use any of the following flags in your terminal:

``--n`` -> Project Name (included in Docs)
``--v`` -> Version Number (included in Docs) (Project Name required to use)
``--f`` -> PATH to files you want to include in the generation
``--d`` -> PATH to the parent directory of the codebase (used only without --f)
``--o`` -> PATH to the output Markdown file
``--e`` -> Message for function without a DocString (enter 0 to exclude functions without a DocString entirely)