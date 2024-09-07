import inspect, types, traceback
from Snippify.__builtins.__errors import RequiredArgumentMissing, WrongArgumentFormat
from Snippify.__builtins.__snip_utils import SerializedSnipSave, SerializedSnipOpen
from Snippify.__builtins.__parsers import ArgumentParser
from Snippify.core.settings import SNIPPETS_DATA_FILEPATH, SNIPPETS_FOLDER_PATH
from datetime import date
import sys

class Snippet:
    def snipObject(self, object, **kwargs):
        known_args = set(['title', 'author', 'desciption', 'version'])
        extra_args = set(kwargs) - known_args
        if extra_args:
            raise ValueError('Unknown argument names: %r' % extra_args)

        title = kwargs['title'] if 'title' in kwargs else None
        author = kwargs['author'] if 'author'  in kwargs else None
        today = date.today()
        date_created = today.strftime("%B %d, %Y")
        description = kwargs['description'] if 'description'  in kwargs else None
        taken_from = inspect.getsourcefile(object)
        version = kwargs['version'] if 'version' in kwargs else str(sys.version)
        # tags , to be implemented
        if not title:
            raise RequiredArgumentMissing('title', 'Title of your snippet')
        
        snippet_info = {"title": title, "description":description, "author": author, "date-created":date_created, "taken-from":taken_from, 'version':version}

        if inspect.isclass(object) | inspect.isfunction(object):
            snippet = inspect.getsource(object)

        snippet_info = {"title": title, "description":description, "author": author, "date-created":date_created, "taken-from":taken_from, 'version':version}

        SerializedSnipSave(title, snippet_info, snippet)

        

    def snipCode(self, **kwargs ):
        known_args = set(['title', 'author', 'desciption', 'version', 'lines', 'file'])
        extra_args = set(kwargs) - known_args
        if extra_args:
            raise ValueError('Unknown argument names: %r' % extra_args)

        title = kwargs['title'] if 'title' in kwargs else None
        author = kwargs['author'] if 'author'  in kwargs else None
        today = date.today()
        date_created = today.strftime("%B %d, %Y")
        description = kwargs['description'] if 'description'  in kwargs else None
        # taken_from = inspect.getsourcefile(object)
        version = kwargs['version'] if 'version' in kwargs else None

        lines = kwargs['lines'] if 'lines' in kwargs else None
        stack = traceback.extract_stack()
        file = kwargs['file'] if 'file' in kwargs else stack[-2].filename
        taken_from = file

        if not lines:
            raise RequiredArgumentMissing('lines',' Range of selected lines to snippet ')
        if not title:
            raise RequiredArgumentMissing('title', 'Title of your snippet')
        
        with open(file, 'r', encoding='UTF-8') as fl:
            self.read_lines = fl.readlines()
            self.length = len(self.read_lines)

        line_values = ArgumentParser.range_parser(lines)
        self.content = ""

        if len(line_values) == 0: raise WrongArgumentFormat('lines', 'Argument value formed in an invalid format, or is None.')
        
        for idx, value in enumerate(line_values):

            if value == '-1':
                self.content = self.content.join(self.read_lines[:])
            elif value == '0':
                self.content = self.content.join(self.read_lines[0])

            elif not "-" in str(value) and str(value) != "0":
                self.content = self.content + '\n' + self.read_lines[value - 1]
 
            else:                
                self.lower_lim = int(value.split('-')[0]) - 1 if int(value.split('-')[0]) > 0 else int(value.split('-')[0])
                self.upper_lim = int(value.split('-')[1])
                if not self.content == "":
                    self.content = self.content + "\n" + "".join(self.read_lines[self.lower_lim:self.upper_lim])
                else: 
                    self.content = self.content + "".join(self.read_lines[self.lower_lim:self.upper_lim])
        
        
        snippet_info = {"title": title, "description":description, "author": author, "date-created":date_created, "taken-from":taken_from, 'version':version}
        SerializedSnipSave(title, snippet_info, self.content)


    def OpenSnippet(self, title=None, uid=None):
        self.search_name = title if title else None
        self.search_uid = uid if uid else None

        if not self.search_name and not self.search_uid:
            raise RequiredArgumentMissing(missing='name/uid', context='Provide UID or title of the Snippet to find it.')
        
        Opener = SerializedSnipOpen()
        if self.search_uid: 
            Opener.ByUid(self.search_uid)
        else:
            Opener.SearchByName(name=self.search_name)
    
    def ListAll(self,):
        Opener = SerializedSnipOpen()
        Opener.all()
        return 
            

    # def OpenWithIdentifier(self, uid):
    #     Opener = SerializedSnipOpen()
    #     Opener.ByUid(uid)

    # def SearchBy(self, name=None, date_created=None, author=None, taken_from=None):
    #     pass


            
