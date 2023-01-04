"""
file: moremaths.py
----------------- 
2nd dummy module to test in-package imports. 
"""


import .complexmaths

def add_three(x):
    return complexmaths.add(x, 3)
