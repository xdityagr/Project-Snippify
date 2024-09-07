from Snippify.core.settings import SNIPPETS_DATA_FILEPATH, SNIPPETS_FOLDER_PATH, init
from Snippify.__builtins.__parsers import *
import json

class __data__:
    def purge(self):
        import shutil
        shutil.rmtree(SNIPPETS_FOLDER_PATH)
        print(Fore.RED + f"Snippify [v1.0], ALL DATA PATHS & DATA FILE PURGED. [{SNIPPETS_FOLDER_PATH}] & [{SNIPPETS_DATA_FILEPATH}] " + Fore.RESET)


    def clean(self, ):
        self.purge()
        init()

    def recreate(self):
        init()

    def _return_all_snippets(self) -> list:
        found = []
        
        with open(SNIPPETS_DATA_FILEPATH, 'r') as file:   
            loaded = json.load(file)
            self.saved_snippets = loaded['saved_snippets']

        for snips in self.saved_snippets:
            found.append(snips)

        return found
    

    def _return_snippet_filedata(self) -> list:
        with open(SNIPPETS_DATA_FILEPATH, 'r') as file:   
            loaded = json.load(file)
            self.saved_snippets = loaded['saved_snippets']

        return self.saved_snippets