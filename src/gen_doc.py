import ast
import os

import argparse
from typing import List

global voidDocStringMSG, excludeDocless
voidDocStringMSG = "*No documentation provided.*"
excludeDocless = False

def extractDocStrings(filepath: str) -> str:
    """Uses the `ast` module to extract DocStrings
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
    """

    filename: str = os.path.basename(filepath)
    functions: list = []
    retStr: str = f"## {filename}\n---\n" 

    # Getting file contents & initializing ast
    with open(rf"{filepath}", 'r', encoding='utf-8') as f:
        rawFile = f.read()
    file = ast.parse(rawFile)

    # Getting all function definitions and filling in DocStrings
    for node in file.body:

        # Adding regular & async functions
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            functions.append(node)
            continue

        # Filtering out non-functions
        if not isinstance(node, ast.ClassDef):
            continue

        # Explicitly handling for Classes (stores class data)
        class_: list = []

        # Adding top-level Class definition
        class_.append(node) 

        # Iterating through the class' nodes
        for subnode in node.body:
            # Adding only class functions
            class_.append(subnode) if isinstance(subnode, (ast.FunctionDef, ast.AsyncFunctionDef)) else ...
        
        # Adding structured class list to functions list
        functions.append(class_)

    for node in functions:
        if not isinstance(node, list):
            functionDocString = ast.get_docstring(node)
            if functionDocString is None and excludeDocless: continue
            retStr += f"### {node.name}\n"
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"
            continue
            
        # Explicitly handling for Classes

        # Adding top-level name & DocString
        className = node[0].name
        classDocString = ast.get_docstring(node[0])
        retStr += f"### {className}\n"
        if classDocString is None and excludeDocless: ...
        else:
            retStr += f"{classDocString if classDocString is not None else voidDocStringMSG}\n"

        del node[0] # Removing top-level ClassDef, only iterating through class' nodes
        for function in node:
            functionDocString = ast.get_docstring(function)
            if functionDocString is None and excludeDocless: continue
            retStr += f"#### ``{className}``: {function.name}\n" # adding class name in function def w/ nested emphasis
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"


    return retStr

def getPythonFiles(dir: str = None) -> list:
    """Gets all .py files in the current directory & filters with the standard .gitignore

    Args:
        dir (str): the top-level directory to use. Defaults to None.

    Returns:
        list: a list of str objects representing a path to a .py file
    """

    exclude = ['.git', '.vscode', 'env', 'Lib', 'site-packages']
    dir = os.getcwd() if dir is None else dir

    retList = []
    
    for root, dirs, files in os.walk(dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file.endswith(".py"):
                retList.append(os.path.join(root, file))

    return retList

def GenDoc(args) -> None:
    """Converts parsed arguments into logic for targeting Python
    files (validates them) and generating/writing to the target
    output file.

    Args:
        args (Namespace): arguments from ArgParser
    """
    
    if args.f:
        for i, file in enumerate(args.f):
            args.f[i] = rf"{args.f[i]}"
            if not file.endswith('.py') or not os.path.exists(file): 
                del args.f[i]
                i -= 1
    else:
        args.f = getPythonFiles(args.d)
    
    markdown = f"``{args.n}``" if args.n else ""
    markdown += f" **{args.v}**\n" if (args.n and args.v) else markdown

    if args.o and not args.o.endswith('.md'):
        args.o += '.md'
    if not args.o:
        args.o = 'DOCS.md'

    if args.e: voidDocStringMSG = args.e
    if isinstance(args.e, str) and args.e.isnumeric():
        global excludeDocless
        excludeDocless = True

    for file in args.f:
        markdown += extractDocStrings(file)
    
    with open(args.o, 'w') as f:
        f.write(markdown)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markdown Documentation file from a Python Repository with DocStrings.")
    parser.add_argument("--n", type=str, help="Project Name (included in Docs)")
    parser.add_argument("--v", type=str, help="Version Number (included in Docs) (Project Name required to use)")
    parser.add_argument("--f", type=os.path.abspath, nargs="+", help="PATH to files you want to include in the generation")
    parser.add_argument("--d", type=os.path.abspath, help="PATH to the parent directory of the codebase (used only without --f)")
    parser.add_argument("--o", type=os.path.abspath, help="PATH to the output Markdown file")
    parser.add_argument("--e", type=str, help="Message for function without a DocString (enter 0 to exclude functions without a DocString entirely)")
    args = parser.parse_args()
    GenDoc(args)