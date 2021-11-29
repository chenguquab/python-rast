from pathlib import Path
import json
from difflib import get_close_matches


data = Path("data.json").read_text()
words_list = json.loads(data)

def get_user_input():
    word = input("please enter a word: ")
    return word

def search_in_dictionary(w):
    try:
        meanings = words_list[w]
        for meaning in meanings:
            print(meaning)
    except:
        

word = get_user_input()        
search_in_dictionary(word)