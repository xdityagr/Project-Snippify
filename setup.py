from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'Create, Save, Use Snippets Easily.'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="Snippify",
    version=VERSION,
    author="Aditya Gaur",
    author_email="adityagaur.home@gmail.com",
    
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['colorama','pyboxen','pynput','pyperclip','tabulate'],
)