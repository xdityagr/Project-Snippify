""""
Snippify v1.0.1
Created By: Aditya Gaur
Example 1 :
"""

class HelloWorld:
    def __init__(self) -> None:pass
    def say_hello(self) -> None:pass
    def say_goodbye(self) -> None:pass


# import statement 
from Snippify.core.snippet import Snippet

# Snippet commands

snippet_obj = Snippet()

# [1] Lists all snippets created with Name and UID in a beautiful table
# also you can input the index number to the snippet copy quickly: 
snippet_obj.ListAll()

# [2] Snip an object  ex: a class named HelloWorld :
# Known args : title, author, description, version | it automatically addes in the version (python version) if not given, with date created, taken_from (source path) :
snippet_obj.snipObject(HelloWorld, title="Hello world!", author="XYZ", version='3.12.4')

# [3]  Snip code from a file 
#  Known args = 'title', 'author', 'desciption', 'version', 'lines', 'file' (if file is None, current file is taken as source)
# The argument 'lines' has parsing rules are as follows : 
# -> It should be range separated by '-', ex: 1-10, 15-20 (Made for selecting lines of code which the user wants to snippify.)
# -> limit1 (lower) < limit2 (upper)
# -> No characters & alphabets are allowed.
# -> No negative range is allowed except -1, which will select all.
# -> More than one limit can be added, separated by commas.
# -> Positive INT can be used to select without range.
# -> Any other type of input will be neglected.

snippet_obj.snipCode( title="Test code", author="XYZ", lines='1-10')    

# [4]  Search/Open snippet from, Title/UID or both. if similar titles found, fetches all the results with same title and prompts which one to choose from (for copying)
# if UID is provided, finds the exact entry of the snippet. with a display of the snippet itself, snippet info and a [C] for copy / [Q] for quit option :
snippet_obj.OpenSnippet(uid='bb8fa2ad80bf799465')

