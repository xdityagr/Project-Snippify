![Alt text](https://github.com/xdityagr/Snippify/blob/main/assets/banner-snippify.png?raw=true "Banner Image")

# Project Snippify

**Snippify** is a Python library designed to simplify the creation, management, and usage of code snippets. With Snippify, you can save snippets of code, organize them efficiently, and retrieve them with ease. It provides an intuitive API and enhances the user experience by beautifully formatted tables and colored terminal output.

---

## Features :

- **List All Snippets**: View all saved snippets in a well-formatted table.
- **Snip Objects**: Snip Python objects (like classes) with detailed metadata such as title, author, version, and more.
- **Snip Code from Files**: Snip specific lines of code from files using a range selector.
- **Search and Open Snippets**: Search for snippets by title or unique ID and easily copy or open them.

---

## Installation :

Install Snippify and its dependencies using `pip`:

```bash
pip install Snippify
```
## Usage

### 1. Listing All Snippets

View all the snippets in a well-structured table format, complete with names and unique IDs. You can also quickly copy a snippet by selecting its index.

```python
from Snippify.core.snippet import Snippet

snippet_obj = Snippet()
snippet_obj.ListAll()
```
### 2. Snipping an Object (Class Example)
Snip any Python object (e.g., classes), while assigning metadata like title, author, and version. The version is auto-generated if not provided.

```python
class HelloWorld:
    def __init__(self) -> None: pass
    def say_hello(self) -> None: pass
    def say_goodbye(self) -> None: pass

snippet_obj.snipObject(HelloWorld, title="Hello World!", author="XYZ", version='3.12.4')
```

### 3. Snipping Code from a File
You can extract snippets from specific lines of code in a file by specifying ranges, such as 1-10, 15-20. If no file is specified, the current file is used.

```python
snippet_obj.snipCode(title="Test Code", author="XYZ", lines='1-10')
```

### 4. Searching and Opening Snippets
Search for snippets by title or unique ID (UID). If multiple results are found for a title, you will be prompted to select the correct one. You can then copy the snippet directly.

```python
snippet_obj.OpenSnippet(uid='bb8fa2ad80bf799465')
```


## Example Code
Here’s an example of how to create and list snippets using Snippify:

```
python
from Snippify.core.snippet import Snippet

snippet_obj = Snippet()

# List all snippets
snippet_obj.ListAll()

# Snip a class object
class HelloWorld:
    def __init__(self) -> None: pass

snippet_obj.snipObject(HelloWorld, title="Hello World!", author="XYZ")

# Snip specific lines from a file
snippet_obj.snipCode(title="Important Code", author="ABC", lines='5-15')

# Search for and open a snippet
snippet_obj.OpenSnippet(uid='12345abcd')
```

## License

This project is licensed under the [GPL License](LICENSE).

## Contact

For questions or feedback, please contact:

- **Email**: adityagaur.home@gmail.com
- **GitHub**: [xdityagr](https://github.com/xdityagr)

Enjoy using **Snippify!** Made with _<3_ In **India!**
