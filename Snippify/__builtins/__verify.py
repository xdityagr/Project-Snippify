from Snippify.__builtins.__data import __data__
from Snippify.__builtins.__parsers import MatchParser, consoleParser
from Snippify.__builtins.__errors import RequiredArgumentMissing
import os
from colorama import Fore, Back, Style

VERIFY_TYPES = ["SCREATE", "SREMOVE"]

s = __data__()
console = consoleParser()

class VerifySequence:
    def _creationSequenceVerification(self, snippet, snippet_filedata):
        VerifyObj = Verify()
        Verified= False

        retr, retr_data = VerifyObj.isNotEntryAlreadyExists(snippet_filedata['name'])
        if retr:
            if not VerifyObj.isTooLong(snippet['snippet']):
                if not VerifyObj.isAvailable(snippet_filedata['name'], snippet_filedata['uid']):
                    Verified = True
                else:   
                    VerifyObj.Prompt(header="Snippify v0.1, Creation Verification", message=f"Snippet already exists.") 
            else:
                VerifyObj.Prompt(header="Snippify v0.1, Creation Verification", message=f"Snippet too long. [0 < Length < 5000]")
                
        elif not retr :
            if retr_data[0] != []:
                VerifyObj.Prompt(header="Snippify v0.1, Creation Verification", message=f"Snippets found with similar titles, Would you like to continue? : \n")
                console.snippet_list_table_format_parser(retr_data[0])
                yes = VerifyObj.Prompt("\n [y/N] : ", input_required=True)
                if yes:
                    if not VerifyObj.isTooLong(snippet['snippet']):
                        if not VerifyObj.isAvailable(snippet_filedata['name'], snippet_filedata['uid']):
                            Verified = True
                        else:
                            VerifyObj.Prompt(header="Snippify v0.1, Creation Verification", message=f"Snippet already exists.")
                            
                    else:
                            VerifyObj.Prompt(header="Snippify v0.1, Creation Verification", message=f"Snippet too long. [0 < Length < 5000]")
                            
            elif retr_data[1]:
                VerifyObj.Prompt(header="Snippify v0.1, Creation Verification", message=f"Snippet found with same title :\n")
                console.snippet_list_table_format_parser(retr_data[1])
                VerifyObj.Prompt(message=f"Please try again with a different title.")


        if Verified: 
            return True
        else: 
            return False




    def _createdSequenceVerification(self, snippet, snippet_filedata):
        pass

class Verify:
    def Prompt(self, message, header=None, input_required=False):
        if header:
            print(Fore.YELLOW + header + Fore.RESET)
            
        if input_required:
            notanswered = True
            while notanswered:
                inp = input(message)
                if inp.lower() != "y" and inp.lower()!="n":
                    print("Try again, ", end="")
                else:
                    if inp.lower() == "y" :
                        return True
                    elif inp.lower() =="n":
                        return False
                    
        else:
            print(message)
        


    def isAvailable(self, name=None, uid=None):
        crr_name = name if name else None
        crr_uid = uid if uid else None
        if not crr_name or not crr_uid: raise RequiredArgumentMissing("INTERNAL ERROR : entry[]", "Missing Snippet Information.")
        fdata = s._return_snippet_filedata()
        located = None
        
        for element in fdata:
            if f"{crr_uid}.snip" in element['saved_path'] and crr_name == element['name']:
                located = element['saved_path']
        if located:
            if os.path.exists(located):
                return True
            else: return False
        else: return False


    def isNotEntryAlreadyExists(self, name:str) -> bool:

        snippets = s._return_all_snippets()
        crr_name = name if name else None
        if not crr_name: raise RequiredArgumentMissing("INTERNAL ERROR : entry[]", "Missing Snippet Information.")

        similiar = []
        same = []
        for idx, snippet in enumerate(snippets):
            if crr_name != snippet['name']:
                if MatchParser.iter_match(crr_name, snippet['name'], 4):
                    similiar.append(snippet)
            else:
                same.append(snippet)

        if similiar != [] or same != []:
            return False, (similiar, same)
        else:
            return True, None
        

    def isTooLong(self, string:str) -> bool:
        max_snippet_length = 5000
        if len(string)>=max_snippet_length:return True
        else: return False


    # def isValidUID(self, uid):
    #     chars = 'abcdefghijklmnopqrstuwxyz1234567890'
    #     length = 9
    #     # uid = list(uid)
    #     if len(uid) == length:
    #         print(chars.find(uid))
    #         if 
                    


# p= PerformCheck(function=None, params=None)
# p.isValidUID("a")
    
# print(Verify().isEntryAlreadyExists("new"))