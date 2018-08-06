from xar_test.bar import bar
from .foo import foo

def main():
    foo()
    bar()
    print("xar_test.submodule.test:main")
