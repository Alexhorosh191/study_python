import turtle

def read_index():
    with open(str("index.txt"), 'r') as f:
        py_obj = f.read()
        turtle.write(py_obj)

    """with open(("3_read_index.py"), "a") as f:
        f.write(py_obj)
"""

read_index()
