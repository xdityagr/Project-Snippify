class HelloWorld:
    def __init__(self) -> None:pass
    def say_hello(self) -> None:pass
    def say_goodbye(self) -> None:pass


# import statement 
from Snippify.core.snippet import Snippet

# Snippet commands

snippet_obj = Snippet()

# [1] Lists all snippets created with name and uid in a beautiful table
# also you can input the index number to  copy quickly
snippet_obj.ListAll()

# [2] Snip an object  ex: a class named HelloWorld
# you can give it a title, author, description, and a python version, it automatically generates the version if not given, with date created, taken_from (path), 
snippet_obj.snipObject(HelloWorld, title="Hello world!", author="XYZ", version='3.12.4')

# [3]  Snip code from a file 
#  known_args = set(['title', 'author', 'desciption', 'version', 'lines', 'file'])
# the argument lines is parsed as follows : 
#  a range separated by '-', ex: 1-10, 15-20
#         (Made for selecting lines of code which the user wants to snippify.)
#         RULES :
#             1. limit1 (lower) < limit2(upper)
#             2. No characters & alphabets are allowed.
#             3. No negative range is allowed except -1, which will select all.
#             4. More than one limit can be added, separated by commas.
#             5. Positive INT can be used to select without range.
#             Any other type of input will be neglected.


# if file is none, current file is taken

snippet_obj.snipCode( title="Test code", author="XYZ", lines='1-10')    

# [4]  Search/Open snippet from, title/uid or both. if similar titles found, fetches all the results with same title and prompts which one to choose from (for copying)
# if uid is provided, finds the exact entry of the snippet. with a display of the snippet itself, snippet info and a [C] for copy / [Q] for quit option, 
snippet_obj.OpenSnippet(uid='bb8fa2ad80bf799465')
