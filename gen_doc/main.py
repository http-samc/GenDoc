"""
 main.py 5/6/2021

 MIT License

 Copyright (c) 2021 http-samc

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
"""

import os
import ast
import argparse
from typing import Union

global voidDocStringMSG, excludeDocless
voidDocStringMSG = "*No documentation provided.*"
excludeDocless = False

def extractDocStrings(filepath: str) -> Union[str, None]:
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

        None: Used to signal the ommittance of the file from the docs,
        only returned when no functions were found
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
            if isinstance(subnode, (ast.FunctionDef, ast.AsyncFunctionDef)):
                class_.append(subnode)

        # Adding structured class list to functions list
        functions.append(class_)

    if len(functions) == 0:
        return None

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

        if classDocString is None and not excludeDocless:
            retStr += f"{voidDocStringMSG}\n"

        elif classDocString:
            retStr += f"{classDocString}\n"

        del node[0] # Removing top-level ClassDef, only iterating through class' nodes
        for function in node:
            functionDocString = ast.get_docstring(function)
            if functionDocString is None and excludeDocless: continue
            retStr += f"#### ``{className}``: {function.name}\n" # adding class name in function def w/ nested emphasis
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"

    return retStr

def getPythonFiles(parent: str = None) -> list:
    """Gets all .py files in the current directory & filters with the standard .gitignore

    Args:
        parent (str): the top-level directory to use. Defaults to None.

    Returns:
        list: a list of str objects representing a path to a .py file
    """
    # major folders to exclude
    exclude = ['.git', '.vscode', 'env', 'Lib', 'site-packages', 'build', 'dist']
    parent = os.getcwd() if parent is None else parent

    retList = []

    for root, dirs, files in os.walk(parent):
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
    # Using only user supplied files
    if args.files:
        # Validating supplied files
        for i, file in enumerate(args.files):
            args.files[i] = rf"{args.files[i]}"
            if not file.endswith('.py') or not os.path.exists(file):
                del args.files[i]
                i -= 1

    # Using all files in supplied directory
    else:
        args.files = getPythonFiles(args.dir)

    # Starting markdown header
    markdown = f"``{args.name}``" if args.name else ""
    markdown += f" **{args.version}**" if (args.name and args.version) else markdown

    # Validating output file if supplied
    if args.output and not args.output.endswith('.md'):
        args.output += '.md'

    # Creating default output file if not supplied
    elif not args.output:
        args.output = 'DOCS.md'

    # Adding custom missing DocString message if supplied
    global voidDocStringMSG
    if args.emptyfunc: voidDocStringMSG = args.emptyfunc

    # Adding omission indicator for DocString-less functions
    if isinstance(args.emptyfunc, str) and args.emptyfunc.isnumeric():
        global excludeDocless
        excludeDocless = True

    # Adding individual file's markdowns if they contain functions
    for file in args.files:
        fileMarkdown = extractDocStrings(file)
        markdown += fileMarkdown if isinstance(fileMarkdown, str) else ""

    # Writing to output file
    with open(args.output, 'w') as f:
        f.write(markdown)

def main() -> None:
    "Creates argument parser and calls GenDoc"
    parser = argparse.ArgumentParser(
        description="Generate a Markdown Documentation file from a Python Repository with DocStrings.")
    parser.add_argument("--name", "--n",
        type=str,
        help="Project Name (included in Docs) (not included if not provided)")
    parser.add_argument("--version", "--v",
        type=str,
        help="Version Number (included in Docs) (Project Name required to use) (not included if not provided)")
    parser.add_argument("--files", "--f",
        type=os.path.abspath,
        nargs="+",
        help="PATH to specific files you want to include in the Doc generation (only pulls from these files) (defaults to all .py files in the current directory)")
    parser.add_argument("--dir", "--d",
        type=os.path.abspath,
        help="PATH to the parent directory of the codebase (used only without --f) (defaults to all .py files in the current directory)")
    parser.add_argument("--output", "--o",
        type=os.path.abspath,
        help="PATH to the output Markdown file (defaults to DOCS.md in current directory)")
    parser.add_argument("--emptyfunc", "--e",
        type=str,
        help="Message for function without a DocString (enter 0 to exclude functions without a DocString entirely) (defaults to \"*No documentation provided.*\")")

    args = parser.parse_args()

    # Calling main() and logging exceptions
    try:
        GenDoc(args)
        print("Generated Successfully.")
    except Exception as e:
        print(f"Error Generating Docs: {e}")

if __name__ == "__main__":
    main()