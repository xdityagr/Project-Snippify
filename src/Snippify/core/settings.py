from pathlib import Path
import os, json

SNIPPETS_FOLDER_PATH = f"{Path.home()}/snippets/"
SNIPPETS_DATA_FILEPATH = f"{SNIPPETS_FOLDER_PATH}.snippets.json"

def init():
    if not os.path.exists(SNIPPETS_FOLDER_PATH):
        os.mkdir(SNIPPETS_FOLDER_PATH)

    if not os.path.exists(SNIPPETS_DATA_FILEPATH):
        temp = {"saved_snippets" : []}
        with open(SNIPPETS_DATA_FILEPATH, 'a') as file:  
            json.dump(temp, file, indent=4)


init()
