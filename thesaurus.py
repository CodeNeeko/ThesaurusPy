import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches (w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes or n if no: " %get_close_matches(w, data.keys())[0])
        if yn == "y": 
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesnt exists, please double check it."
        else:
            return "We didnt understand your entry"
    else:
        return ("The word doesnt exists, please double check it.")

word=input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)