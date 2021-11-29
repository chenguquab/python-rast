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
        similar_words = get_close_matches(w, words_list.keys(), n=5, cutoff=0.85)
        result = input("are you searching for the meaning of {}? if yes press Y. ".format(similar_words[0]))
        if result.lower == "y":
            search_in_dictionary(similar_words[0])
        else:
            print("search has no result")

word = get_user_input()        
search_in_dictionary(word)