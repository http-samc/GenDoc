## main.py
---
### extractDocStrings
Uses the `ast` module to extract DocStrings
from a Python file. 

Args:
    filepath (str): path to a Python file
    (*precondition: filepath is a valid .py file*)
    

Returns:
    str: A markdown-ready string containing the filename,
    and function name + DocString pairs in 
    the following format:

    ## <filename>
    ---
    ### <function name>
    <function DocString>
    ...

    tuple: Contains 1 item, the markdown-ready string, if no functions were found;
    used to signal an ommitance of this file
### getPythonFiles
Gets all .py files in the current directory & filters with the standard .gitignore

Args:
    dir (str): the top-level directory to use. Defaults to None.

Returns:
    list: a list of str objects representing a path to a .py file
### GenDoc
Converts parsed arguments into logic for targeting Python
files (validates them) and generating/writing to the target
output file.

Args:
    args (Namespace): arguments from ArgParser
### main
Creates argument parser and calls GenDoc
