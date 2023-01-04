"""
file: moremaths.py
----------------- 
2nd dummy module to test in-package imports. 
"""


from test_minimal_python_package import complexmaths

def add_three(x):
    return complexmaths.add(x, 3)
