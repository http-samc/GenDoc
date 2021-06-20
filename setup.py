from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="GenDoc",
    version="0.0.95",
    description="Generate a Markdown Documentation file from a Python Repository with DocStrings.",
    url="https://github.com/http-samc/GenDoc",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = ["gen_doc"],
    entry_points = {
        'console_scripts': [
            'gendoc=gen_doc.main:main'
        ]
    },
    classifiers = [
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English"
    ]
)