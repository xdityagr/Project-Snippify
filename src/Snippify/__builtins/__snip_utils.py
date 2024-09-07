import pickle , binascii, os, json
from Snippify.core.settings import SNIPPETS_DATA_FILEPATH, SNIPPETS_FOLDER_PATH, init
from Snippify.__builtins.__parsers import *
from Snippify.__builtins.__verify import VerifySequence
import pynput
from pynput.keyboard import Key, Listener
import pyperclip

from colorama import Fore, Back, Style

ConsoleParser = consoleParser()

class SerializedSnipSave:
    init()
    def __init__(self, name=None, snippet_info=None, snippet=None):
        self.snippet_info = snippet_info
        self.name= name
        self.snippet = snippet
        self.to_save = {"snip_info": self.snippet_info, "snippet":snippet}  
        # snippets_folder = str(os.path.dirname(os.path.abspath('snippets'))) + "/snippets" # can be customised 

        current_key = self.generate_key()
        filename = SNIPPETS_FOLDER_PATH+f"{current_key}.snip"
        self.uid_data = {"name":self.name, "uid" : current_key, "saved_path":filename}

        seq = VerifySequence()
        retr = seq._creationSequenceVerification(snippet=self.to_save, snippet_filedata=self.uid_data)
        if retr:
            with open(filename, 'wb') as file: 
                pickle.dump(self.to_save, file) 

            with open(SNIPPETS_DATA_FILEPATH, 'r') as file:   
                loaded = json.load(file)
                loaded['saved_snippets'].append(self.uid_data)
            
            with open(SNIPPETS_DATA_FILEPATH, 'w') as file:  
                json.dump(loaded, file, indent=4)

            ConsoleParser.snippet_save_format_parser(self.uid_data, self.to_save)
        else:
            print("Verification Unsucessful, " + Fore.RED + "Quitting.. " + Fore.RESET)
            quit()

    def generate_key(self):
        return str(binascii.hexlify(os.urandom(9)).decode())


class Copy:
    def __init__(self, snippet):
        self.snippet = snippet
        self.run_copy_loop()

    def on_press(self,key):
        pass
      
    def on_release(self,key):
        if key == Key.esc or key.char == 'q':
            return False
        elif key.char == 'c':
            pyperclip.copy(self.snippet)
            print('[Copied to clipboard!]')

    def run_copy_loop(self):
        while True:
            with Listener(on_press = self.on_press, on_release = self.on_release) as listener:                                    
                listener.join()
                break
                    


class SerializedSnipOpen:
    def ByUid(self,uid):
        with open(SNIPPETS_DATA_FILEPATH, 'r') as file:   
            loaded = json.load(file)
            self.saved_snippets = loaded['saved_snippets']
        
        selected = None
        for idx, snips in enumerate(self.saved_snippets):
            if snips['uid'] == uid:
                selected = (idx, snips)
        if selected:
            file = selected[1]['saved_path']
            with open(file, 'rb') as fl: 
                loaded_snippet = pickle.load(fl)
            self.snippet = loaded_snippet['snippet']
            ConsoleParser.snippet_format_parser(snippet_file_info=selected[1], snippet_info=loaded_snippet)   
            Copy(self.snippet)

        else:
            ConsoleParser.snippet_not_found_search_format_parser(uid)



    def SearchByName(self, name):
        found = []
        with open(SNIPPETS_DATA_FILEPATH, 'r') as file:   
            loaded = json.load(file)
            self.saved_snippets = loaded['saved_snippets']

        for idx, snips in enumerate(self.saved_snippets):
            """
            MAKE MORE ADVANCED SEARCH...
            """
            if MatchParser.iter_match(name, snips['name'], 4):
                found.append(snips)
            # if str(name) in str(snips['name']):
            #     found.append(snips)
        if len(found)>0:
            if len(found)==1:
                ConsoleParser.snippet_uid_search_format_parser(name, found)
                to_copy = found[0]
            else:
                select, inp = ConsoleParser.snippet_search_format_parser(name, found)
                if inp!=None:
                    print(f"Selected [{inp}], ")
                    while True:
                        inp = input("Would you like to view its information or copy it? [i/C] : ")
                        if inp.lower() != "i" and inp.lower()!="c":
                            print("Try again, ", end="")
                        else:
                            if inp.lower() == "i" :
                                file = select['saved_path']
                                with open(file, 'rb') as fl: 
                                    loaded_snippet = pickle.load(fl)
                                snippet = loaded_snippet
                                ConsoleParser.snippet_format_parser_view_only(snippet_file_info=select, snippet_info=snippet)
                                to_copy = -1
                                break
                            elif inp.lower() =="c":
                                to_copy =  select
                                print("Copied to Clipboard!")
                                break
                else:to_copy=-1
                
            if to_copy!= -1:
                file = to_copy['saved_path']
                with open(file, 'rb') as fl: 
                    loaded_snippet = pickle.load(fl)
                self.snippet = loaded_snippet['snippet']

                pyperclip.copy(self.snippet)
            else:
                quit()
        else:
            ConsoleParser.snippet_not_found_search_format_parser(name)

    def all(self):
        found = []
        with open(SNIPPETS_DATA_FILEPATH, 'r') as file:   
            loaded = json.load(file)
            self.saved_snippets = loaded['saved_snippets']

        for snips in self.saved_snippets:
            found.append(snips)
        if len(found)> 0:
            to_copy =  ConsoleParser.snippet_all_search_format_parser(found)
            if to_copy!= -1:
                print("Copied to Clipboard!")
                file = to_copy['saved_path']
                with open(file, 'rb') as fl: 
                    loaded_snippet = pickle.load(fl)
                self.snippet = loaded_snippet['snippet']

                pyperclip.copy(self.snippet)
            else:
                quit()
        else:
            print(Fore.YELLOW + "Snippify [v1.0], Search Info: " + Fore.RESET)
            print("No Snippet created yet, Get started now!" )




