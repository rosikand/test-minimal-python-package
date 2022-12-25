"""
file: example.py
----------------- 
Example python module. 
"""

from markdown import markdown


def test_module():
	print("This module is working!")


def print_with_markdown(text):
	print(markdown("**bold**"))
