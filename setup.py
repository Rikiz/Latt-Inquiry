"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ["./main.py"]
DATA_FILES = ['form.ui', "form.py", "init.py", "utils"]
OPTIONS = {"includes" : ["PyQt5", "pandas", "requests", "image", "cython"]}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
