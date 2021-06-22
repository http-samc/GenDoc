Here's an example of what GenDoc can produce - *everything below the line was generated with the following command **in the termial***:
**Long Syntax:** `gendoc --name GenDoc --version 1.0.0 --funcSections --codeFence --files gen_doc/main.py --fileHeader`<br>**Short Syntax:** `gendoc --n GenDoc --v 1.0.0 --fs --cf --f gen_doc/main.py --fh`
* **NOTE** that this does not use all the [available flags](/README.md)
---

`GenDoc` **1.0.0**
## [gen_doc.main.py](/gen_doc/main.py)
---
### gen_doc.main.`extractDocStrings` [function]
<details style='color: #333333'><summary>Details</summary>

```Python
Uses the ast module to extract DocStrings
from a Python file.

Args:
    filepath (str): path to a Python file (*precondition: filepath is a valid .py file*)

    parent (str): the top-level directory to use. Defaults to None.

    classSections (bool): create collapsible sections for classes. Defaults to False.

    methodSections (bool): create collapsible sections for class methods. Defaults to False.

    funcSections (bool): create collapsible sections for functions. Defaults to False.

    fileHeaders (bool): add filename and relative path before it's classes and functions. Defaults to False.

    fence (bool): surround each DocString in a markdown code fence with Python formatting. Defaults to False.

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
```
</details>### gen_doc.main.`getPythonFiles` [function]
<details style='color: #333333'><summary>Details</summary>

```Python
Gets all .py files in the current directory & filters with the standard .gitignore

Args:
    parent (str): the top-level directory to use. Defaults to None.

Returns:
    list: a list of str objects representing a path to a .py file
```
</details>### gen_doc.main.`GenDoc` [function]
<details style='color: #333333'><summary>Details</summary>

```Python
Converts parsed arguments into logic for targeting Python
files (validates them) and generating/writing to the target
output file.

Args:
    args (Namespace): arguments from ArgParser
```
</details>### gen_doc.main.`main` [function]
<details style='color: #333333'><summary>Details</summary>

```Python
Creates argument parser and calls GenDoc
```
</details>