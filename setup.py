from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="GenDoc",
    version="0.1.0",
    description="",
    py_modules=["gendoc"],
    package_dir={'':'src'},
    install_requires = [
        "requests==2.25.1"
    ],
    url="https://github.com/http-samc/citer",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech",
    long_description=long_description,
    long_description_content_type='text/markdown'
)