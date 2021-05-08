# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import requests
import numpy as np
import re
import sys
import os


# %%
class piratey_speak:
    
    
    def __init__(self):
            print("To close, type: Exit")
            self.to_translate = ""
            self.piratey_mappings = {"Ahoy":["Hello","Hey"],"'n":"and",'be':['is','am','are'], 'aye':['yes','yup','yeah'],'me':'my','ye':'you','hearties':['friends','companions','buddies'],'lad':['young man','young male'],'matey':['friend','dude','bro','mate'],'bounty':['reward', 'prize']}
            while True:
                self.to_translate = input("Translate: ")
                if self.to_translate != "Exit":
                    self.translation = self.replace_lingo()
                    print('====> ',self.translation)
                else:
                    sys.exit()
                
        
    def replace_lingo(self):
        text = self.to_translate
        words = self.piratey_mappings
        text = re.findall(r"[\w']+|[.,!?;]", text)
        #print(text)
        #print(text)
        #print(words)
        items = list(words.items())
        #print(list(words.values()))
        for subtext in text:
            #print('subtext :', subtext)
            if subtext.endswith("ing"):
                text_matchin_location = np.where([subtext.endswith("ing") for subtext in text])[0][0]  # Hopefully the joke with the naming is ascertained here.. 
                text[text_matchin_location] = subtext.replace("ing","in'")
            for word in words.values():
                #print('entering loop.. current word : ', word)
                if not isinstance(word, list):
                    if word == subtext:
                        #subtext = keep_letters(subtext)
                        #print('allegedly ',word, ' is equal to ', subtext)
                        #print('list(words.values()) = ',list(words.values())[4])
                        match_location = np.where([word == value for value in list(words.values())])[0][0]
                        text_match_location = np.where([subtext == word for subtext in text])[0][0]
                        #print('text match : ',text_match_location)
                        #print('match location : ', match_location)
                        #print(list(words))
                        pirate_word = list(words)[match_location]
                        #print('pirate word : ',pirate_word)
                        #print('word : ',word)
                        #print(subtext)
                        text[text_match_location] = pirate_word
                else: 
                    if subtext in word:
                        #subtext = keep_letters(subtext)
                        word_location = np.where([subtext == option for option in word])[0][0]
                        word = word[word_location]
                        val_location = self.find_key_index(list(words.values()),subtext)
                        #print('val location = ',val_location)
                        #print('word locale : ', word_location)
                        #print('allegedly ',word, ' is equal to ', subtext)
                        #print('list(words.values()) = ',list(words.values()))
                        text_match_location = np.where([subtext == word for subtext in text])[0][0]
                        #print('text match : ',text_match_location)
                        #print('match location : ', match_location)
                        #print(list(words))
                        pirate_word = list(words)[val_location]
                        #print('pirate word : ',pirate_word)
                        #print('word : ',word)
                        #print(subtext)
                        text[text_match_location] = pirate_word
        full_text = " ".join(text)
        return full_text
    
    def find_key_index(self, keys, text):
        #print('keys : ', keys)
        #print('text to find : ', text)
        i=0
        for subkeys in keys:
            #print('i = ', i)
            #print('subkey = ',subkeys)
            if (text == subsubkey for subsubkey in subkeys):
                #print(np.where([text == subsubkey for subsubkey in subkeys])[0])
                if len(np.where([text == subsubkey for subsubkey in subkeys])[0]) > 0:
                    return i
                else:
                    i+=1
                
    

# %%
piratey_speak().translation

# %%
# To fix puncutuation: If next element isn't a letter, add it to the end of the last element

# %%
test = 123

# %%
thingthingthing='a'

# %%
