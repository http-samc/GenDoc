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
    functions: list = []
    retStr: str = f"## {filename}\n---\n" 

    # Getting file contents & initializing ast
    with open(filepath, 'r') as f:
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
            retStr += f"### {node.name}\n"
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"
            continue
            
        # Explicitly handling for Classes

        # Adding top-level name & DocString
        className = node[0].name
        classDocString = ast.get_docstring(node[0])
        retStr += f"### {className}\n"
        retStr += f"{classDocString if classDocString is not None else voidDocStringMSG}\n"

        del node[0] # Removing top-level ClassDef, only iterating through class' nodes
        for function in node:
            functionDocString = ast.get_docstring(function)
            retStr += f"#### ``{className}``: {function.name}\n" # adding class name in function def w/ nested emphasis
            retStr += f"{functionDocString if functionDocString is not None else voidDocStringMSG}\n"


    return retStr

print(extractDocStrings(r"C:\Programming\OffTime\cut-it\Cut-It\app.py"))