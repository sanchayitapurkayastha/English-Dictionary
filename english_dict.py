import json
from difflib import get_close_matches

data=json.load(open("data.json")) #data is a dict

def meaning(w):
    w=w.lower() #for case senstivity
    if w in data:   return data[w]
    elif w.title() in data:  return data[w.title()] #for proper nouns
    elif w.upper() in data: return data[w.upper()] #for acronyms
    elif len(get_close_matches(w,data.keys()))>0: #for spelling mistake
        yes_no=input("Did you mean '%s'? Enter Y for yes or N for no:" %get_close_matches(w,data.keys())[0])
        yes_no=yes_no.upper() #if user enters 'y' & 'n' in lower case instead of upper
        if yes_no=="Y" or yes_no=='YES': return data[get_close_matches(w,data.keys())[0]]
        elif yes_no=="N" or yes_no=='NO':  return "The word doesn't exists. Please double check it."
        else:   return "Not valid input."
    else:   return "The word doesn't exists. Please double check it." #for wrong input entered

print("\n\t\t\t\t WELCOME TO SANCHAYITA'S DICTIONARY\n")
word=input("Enter word:")
meaning=meaning(word)
if type(meaning) is list:
    for l in meaning:  print("-",l) #for proper presentation of data to the user
else:   print(meaning)
