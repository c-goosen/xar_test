from __future__ import absolute_import, division, print_function, unicode_literals

import os

from setuptools import setup

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    with open(os.path.join(CURRENT_DIR, "README.md"), "r") as ld_file:
        return ld_file.read()


setup(
    name="xar_test",
    version="0.0.0",
    description="Test",
    author="Nick Terrell",
    author_email="terrelln@fb.com",
    license="BSD",
    packages=["xar_test", "xar_test.submodule"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "test = xar_test.test:main",
            "subtest = xar_test.submodule.test:main",
        ],
    },
)
