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

import argparse
import ast
import os
from typing import Union

def extractDocStrings(filepath: str, parent: str = None, classSections: bool = False,
        methodSections: bool = False, funcSections: bool = False, fileHeaders: bool = False,
        fence: bool = False, voidDocStringMSG: bool = "*No description provided*",
        excludeDocless: bool = False) -> Union[str, None]:
    """Uses the ast module to extract DocStrings
    from a Python file.

    Args:
        filepath (str): path to a Python file (*precondition: filepath is a valid .py file*)

        parent (str): the top-level directory to use. Defaults to None.

        classSections (bool): create collapsible sections for classes. Defaults to False.

        methodSections (bool): create collapsible sections for class methods. Defaults to False.

        funcSections (bool): create collapsible sections for functions. Defaults to False.

        fileHeaders (bool): add filename and relative path before it's classes and functions. Defaults to False.

        fence (bool): surround each DocString in a markdown code fence with Python formatting. Defaults to False.

        voidDocStringMSG (bool): the function DocString if it does not have one. Defaults to "*No description provided.*".

        excludeDocless (bool): whether or not to exclude functions that do not have a DocString. Defaults to False.

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
    relPath = os.path.relpath(filepath, start = parent).replace('\\', '/') # literal relative path
    relPathFormatted = relPath.replace('/', '.').replace('.py', '') # pythonic implementation for path

    functions: list = []
    retStr: str = f"## [{relPathFormatted}.py](/{relPath})\n---\n" if fileHeaders else ""

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
            if fence and functionDocString: functionDocString = f"```Python\n{functionDocString}\n```"

            if functionDocString is None and excludeDocless: continue
            retStr += f"### {relPathFormatted}.`{node.name}` [function]\n"

            if funcSections and functionDocString: retStr += "<details style='color: #333333'><summary>Details</summary>\n\n" # Opening Function section
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"
            if funcSections and functionDocString: retStr += "</details>" # Closing Function section
            continue

        # Explicitly handling for Classes

        # Getting top-level name & DocString
        className = node[0].name
        classDocString = ast.get_docstring(node[0])

        # Checking for superclasses
        inherits = "inherits: "
        for base in node[0].bases:
            inherits += f"`{base.id}`, "

        # If no superclasses were found, omit the inherits str
        if inherits == "inherits: ":
            retStr += f"### {relPathFormatted}.`{className}` [class]\n"

        # If we found a superclass, trim the extra ", " and add a closing "]" -> append
        else:
            inherits = inherits[:-2]
            retStr += f"### {relPathFormatted}.`{className}` [class] [{inherits}]\n"

        if classDocString is None and not excludeDocless:
            retStr += f"{voidDocStringMSG}\n"

        elif classDocString:
            retStr += f"{classDocString}\n"

        if classSections: retStr += "<details style='color: #333333'><summary>Methods</summary><p>\n\n" # Opening Class section

        del node[0] # Removing top-level ClassDef, only iterating through class' nodes
        for function in node:
            functionDocString = ast.get_docstring(function)
            if fence and functionDocString: functionDocString = f"```Python\n{functionDocString}\n```"


            if functionDocString is None and excludeDocless: continue
            retStr += f"#### {className}.`{function.name}`\n" # adding class name in function def w/ nested emphasis

            if methodSections and functionDocString: retStr += "<details style='color: #333333'><summary>Details</summary><p>\n\n" # Opening Class Method section
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"
            if methodSections and functionDocString: retStr += "</p></details>\n\n" # Closing Class Method section

        if classSections: retStr += "</p></details>\n\n" # Closing Class section

    return retStr

def getPythonFiles(parent: str = None) -> list:
    """Gets all .py files in the current directory & filters with the standard .gitignore

    Args:
        parent (str): the top-level directory to use. Defaults to None.

    Returns:
        list: a list of str objects representing a path to a .py file
    """
    # major folders to exclude
    exclude = ['.git', '.vscode', 'env', 'Lib', 'site-packages', 'build', 'dist', 'output']
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
                print(f"Excluding {file} because it is not a valid file.")
                del args.files[i]
                i -= 1

    # Using all files in supplied directory
    else:
        args.files = getPythonFiles(args.dir)

    # Starting markdown header
    markdown = f"`{args.name}`" if args.name else ""
    markdown += f" **{args.version}**" if (args.name and args.version) else markdown
    markdown += "\n" if (args.name or args.version) else ""

    # Validating output file if supplied
    if args.output and not args.output.endswith('.md'):
        args.output += '.md'

    # Creating default output file if not supplied
    elif not args.output:
        args.output = 'DOCS.md'

    # Adding omission indicator for DocString-less functions
    excludeDocless = True if isinstance(args.emptyFunc, str) and args.emptyFunc.isnumeric() else False

    # Adding individual file's markdowns if they contain functions
    for file in args.files:
        fileMarkdown = extractDocStrings(file, parent = args.dir, classSections = args.classSections,
            methodSections = args.methodSections, funcSections = args.funcSections,
            fileHeaders = args.fileHeaders, fence = args.codeFence,
            voidDocStringMSG = args.emptyFunc, excludeDocless = excludeDocless)
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
    parser.add_argument("--emptyFunc", "--e",
        type=str,
        help="Message for function without a DocString (enter 0 to exclude functions without a DocString entirely) (defaults to \"*No documentation provided.*\")")
    parser.add_argument("--classSections", "--cs",
        action="store_true",
        default=False,
        help="Add collapseable sections for classes (not generated if not called)")
    parser.add_argument("--methodSections", "--ms",
        action="store_true",
        default=False,
        help="Add collapseable sections for class methods (not generated if not called)")
    parser.add_argument("--funcSections", "--fs",
        action="store_true",
        default=False,
        help="Add collapseable sections for functions (not generated if not called)")
    parser.add_argument("--fileHeaders", "--fh",
        action="store_true",
        default=False,
        help="Add file name & relative path above it's classes and functions (not generated if not called)")
    parser.add_argument("--codeFence", "--cf",
        action="store_true",
        default=False,
        help="Surround all DocStrings in a Python markdown code fence (not generated if not called)")
    args = parser.parse_args()

    # Calling main() and logging exceptions
    try:
        GenDoc(args)
        print("Generated Successfully.")
    except Exception as e:
        print(f"Error Generating Docs: {e}")

if __name__ == "__main__":
    main()