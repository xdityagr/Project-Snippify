import inspect
from pyboxen import boxen
from colorama import Fore, Back, Style
from tabulate import tabulate
import difflib

class MatchParser:
    def iter_match(pattern:str, string:str, minimum_limit:int):
        pattern= list(pattern.lower())
        string = list(string.lower())
        if pattern != string:
            lim = minimum_limit
            same = [[idx, x] for idx, x in enumerate(string) if x in pattern and x != " "]
            
            indexes = [idx for idx, ele in same]
            consecutive = 0
            for x in range(len(indexes) - 1):
                if indexes[x] == indexes[x+1] -1:
                    consecutive += 1

            if consecutive>= minimum_limit:
                return True
            else:
                return False
        else:return True
        

class ArgumentParser:
    def range_parser(limits_string : str) -> list:
        """
        Parses a range separated by '-', ex: 1-10, 15-20
        (Made for selecting lines of code which the user wants to snippify.)
        RULES :
            1. limit1 (lower) < limit2(upper)
            2. No characters & alphabets are allowed.
            3. No negative range is allowed except -1, which will select all.
            4. More than one limit can be added, separated by commas.
            5. Positive INT can be used to select without range.
            Any other type of input will be neglected.
        """

        limits_string = limits_string.replace(' ', '')
        values= limits_string.split(',') # Gets every comma separaed value
        chars = "-~!@#$%^&*()<>:'{|?}+=_\\.;[]"

        for idx, val in enumerate(values):
            if val == '-1':
                values = [values[idx]]
                break
            elif val == '0':
                values = [values[0]]
                break
            elif '-' in val:
                if val.split('-')[0] == "" or val.split('-')[1] == "" or val.split('-')[0] in chars or val.split('-')[1] in chars or not val.split('-')[0].isdigit() :
                    values.pop(idx)

                elif int(val.split('-')[0]) > int(val.split('-')[1]):
                    values.pop(idx)

            else:
                if val.isdigit():
                    values[idx] = int(val)
                else: 
                    values.pop(idx)
                    
        return values



class consoleParser:

    def snippet_format_parser(self,snippet_file_info : dict, snippet_info: dict) -> str:
        print('\n')
        print(boxen(snippet_info['snippet'], title="Your Snippet", subtitle="Snippify v0.1", subtitle_alignment="right", padding=1, color="yellow"))
        print("*"*69 + '\n')
        print(Fore.YELLOW + "Snippet Info:" + Fore.RESET)
        print(f"Title :'{snippet_file_info['name']}' , UID : '{snippet_file_info['uid']}'")
        print(f"Author : {snippet_info['snip_info']['author']}")
        print(f"Description : {snippet_info['snip_info']['description']}")
        print(f"Taken From : {snippet_info['snip_info']['taken-from']}")
        print(f"Date Created : {snippet_info['snip_info']['date-created']}")
        print(f"Python Version : {snippet_info['snip_info']['version']}")
        print("... \n")
        print(boxen("Type [C] to Copy Or [Q] to Quit", color="yellow"))
    
    def snippet_format_parser_view_only(self,snippet_file_info : dict, snippet_info: dict) -> str:
        print('\n')
        print(boxen(snippet_info['snippet'], title="Your Snippet", subtitle="Snippify v0.1", subtitle_alignment="right", padding=1, color="yellow"))
        print("*"*69 + '\n')
        print(Fore.YELLOW + "Snippet Info:" + Fore.RESET)
        print(f"Title :'{snippet_file_info['name']}' , UID : '{snippet_file_info['uid']}'")
        print(f"Author : {snippet_info['snip_info']['author']}")
        print(f"Description : {snippet_info['snip_info']['description']}")
        print(f"Taken From : {snippet_info['snip_info']['taken-from']}")
        print(f"Date Created : {snippet_info['snip_info']['date-created']}")
        print(f"Python Version : {snippet_info['snip_info']['version']}")
        print("... \n")

    def snippet_save_format_parser(self,snippet_file_info : dict, snippet_info: dict) -> str:
        print('\n')
        print(boxen(snippet_info['snippet'], title="Your Snippet is saved!", subtitle="Snippify v0.1", subtitle_alignment="right", padding=1, color="yellow"))
        print("*"*69 + '\n')
        print(Fore.YELLOW + "Snippet Info:" + Fore.RESET)
        print(f"Title :'{snippet_file_info['name']}' , UID : '{snippet_file_info['uid']}'")
        print(f"Author : {snippet_info['snip_info']['author']}")
        print(f"Description : {snippet_info['snip_info']['description']}")
        print(f"Taken From : {snippet_info['snip_info']['taken-from']}")
        print(f"Date Created : {snippet_info['snip_info']['date-created']}")
        print(f"Python Version : {snippet_info['snip_info']['version']}")
        print("... \n")
        print(boxen("Snippet Saved Successfully!", color="yellow"))
        
    def snippet_search_format_parser(self,search, snippets : list) -> str:
        print(Fore.YELLOW + "Snippify [v1.0], Search Info: " + Fore.RESET)
        print(f"Found {len(snippets)} results for your search '{search}' : ")
        tubular = []
        length = len(snippets)
        for idx, snippet in enumerate(snippets):
            ele = [idx+1, snippet['name'], snippet['uid']]
            tubular.append(ele)
        
        print(tabulate(tubular, headers=['Index', 'Title', 'UID'], tablefmt='rounded_grid', numalign='center'))
        notanswered = True
        while notanswered:
            inp = input("Please type the index to select the respective snippet [or Q to exit]: ")
            if inp.lower()=='q':
                return -1, None
            elif 0<int(inp) <= length:
                return snippets[int(inp)-1], inp
            else: 
                print("Try again, ", end="")


    def snippet_uid_search_format_parser(self,search, snippets : list) -> str:
        print(Fore.YELLOW + "Snippify [v1.0], Search Info: " + Fore.RESET)
        print(f"Found a match for your search '{search}' : ")
        tubular = []
        ele = [1, snippets[0]['name'], snippets[0]['uid']]
        tubular.append(ele)
        
        print(tabulate(tubular, headers=['Index', 'Title', 'UID'], tablefmt='rounded_grid', numalign='center'))
        print("Automatically copied to clipboard! ")
        # notanswered = True
        # while notanswered:
        #     inp = input("Please type the index to copy the respective snippet : ")
        #     if 0<int(inp) <= length:
        #         return snippets[int(inp)-1]
        #     else: print("Try again, ", end="")


    # s = [{"name":"HELLO WORLDDD", "uid" : "387b7712c54800c481"}, {"name":"TESTT             dkawTTTTTT", "uid" : "387b7712c54800c481"},{"name":"self.name", "uid" : "387b7712c54800c481"}]        
    # print(snippet_search_format_parser('Hello world', s))
        
    def snippet_not_found_search_format_parser(self, name):
        print(Fore.YELLOW + "Snippify [v1.0], Search Info: " + Fore.RESET)
        print(f"No match found for your search '{name}'")


    def snippet_all_search_format_parser(self, snippets):
        print(Fore.YELLOW + "Snippify [v1.0], Search Info: " + Fore.RESET)
        print(f"List of all of your snippets: ")
        tubular = []
        length = len(snippets)
        for idx, snippet in enumerate(snippets):
            if snippet['name'] == None:
                snippet['name'] = "None"
            ele = [idx+1, snippet['name'], snippet['uid']]
            tubular.append(ele)
        
        print(tabulate(tubular, headers=['Index', 'Title', 'UID'], tablefmt='rounded_grid', numalign='center'))
        notanswered = True
        while notanswered:
            inp = input("Please type the index to copy the respective snippet [or Q to exit]: ")
            if inp.lower()=='q':
                return -1

            elif 0<int(inp) <= length:

                return snippets[int(inp)-1]
            else: print("Try again, ", end="")


    def snippet_list_table_format_parser(self, snippets):
        tubular = []
        length = len(snippets)
        for idx, snippet in enumerate(snippets):
            if snippet['name'] == None:
                snippet['name'] = "None"
            ele = [idx+1, snippet['name'], snippet['uid']]
            tubular.append(ele)
        
        print(tabulate(tubular, headers=['Index', 'Title', 'UID'], tablefmt='rounded_grid', numalign='center'))

