import ast
import os

global voidDocStringMSG 
voidDocStringMSG = "*No documentation provided.*"

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
    retStr: str = f"## {filename}\n---\n" 

    # Getting file contents & initializing ast
    with open(filepath, 'r') as f:
        rawFile = f.read()
    file = ast.parse(rawFile)

    # Getting all function definitions and filling in DocStrings
    functions = [function for function in file.body 
                if isinstance(function, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef))]
        
    for function in functions:
        functionDocString = ast.get_docstring(function)
        retStr += f"### {function.name}\n{functionDocString if functionDocString is not None else voidDocStringMSG}"

    return retStr

print(extractDocStrings(r"C:\Programming\OffTime\cut-it\Cut-It\app.py"))