# -*- coding: utf-8 -*-
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
import csv


# %%
class piratey_speak:
    
    
    def __init__(self):
            print("To close, type: Exit\n\n\n")
            self.to_translate = ""
            self.present_participles = self.get_present_participles()
            self.piratey_mappings = {"fer":"for","o'":"of","'ere":"here","Ahoy":["hello","hey","yo"],"'n":"and",'be':['is','am','are'], 'aye':['yes','yup','yeah'],'me':'my','ye':'you','hearties':['friends','companions','buddies'],'lad':['young man','young male'],'matey':['friend','dude','bro','mate'],'bounty':['reward', 'prize']}
            while True:
                self.to_translate = input("\nTranslate: ")
                if self.to_translate != "Exit":
                    self.translation = self.replace_lingo()
                    print('\n====> ',self.translation)
                else:
                    sys.exit()
    
    
    def get_present_participles(self):
        present_participles = set()
        with open("verbs-all.csv", "r",encoding = 'ISO-8859–1') as f:
            reader = csv.reader(f)
            contents = list(reader)
        for i in range(len(contents)):
            current = contents[i][0].split("\t")
            current = [vals.rstrip() for vals in current]
            present_participles.add(current[-1])
        present_participles.add("having")
        present_participles.add("being")
        return present_participles        
        
    def replace_lingo(self):
        text = self.to_translate
        words = self.piratey_mappings
        text = re.findall(r"[\w']+|[.,!?;]", text)
        items = list(words.items())
        present_participles = self.present_participles
        for subtext in text:
            if subtext.lower() in present_participles:
                text_matchin_location = np.where([subtext.endswith("ing") for subtext in text])[0][0]  # Hopefully the joke with the naming is ascertained here.. 
                text[text_matchin_location] = subtext.replace("ing","in'")
            if subtext.endswith('ingly'):
                text_matchin_location = np.where([subtext.endswith("ingly") for subtext in text])[0][0]  # Hopefully the joke with the naming is ascertained here.. 
                text[text_matchin_location] = subtext.replace("ingly","in'ly")
            for word in words.values():
                if not isinstance(word, list):
                    if word.lower() == subtext.lower():
                        match_location = np.where([word == value for value in list(words.values())])[0][0]
                        text_match_location = np.where([subtext.lower() == word.lower() for subtext in text])[0][0]
                        pirate_word = list(words)[match_location]
                        if subtext[0].isupper():
                            pirate_word = pirate_word.capitalize()
                            text[text_match_location] = pirate_word
                        else:
                            text[text_match_location] = pirate_word
                else: 
                    if subtext.lower() in [words.lower() for words in word]:
                        word_location = np.where([subtext.lower() == option.lower() for option in word])[0][0]
                        word = word[word_location]
                        val_location = self.find_key_index(list(words.values()),subtext.lower())
                        text_match_location = np.where([subtxt.lower() == word.lower() for subtxt in text])[0][0]
                        pirate_word = list(words)[val_location]
                        if subtext[0].isupper():
                            pirate_word = pirate_word.capitalize()
                            text[text_match_location] = pirate_word
                        else:
                            text[text_match_location] = pirate_word                        
        #print('Text before fixed: ', text)
        text = self.fix_punctuation(text)
        #print('Fixed text: ', text)
        full_text = " ".join(text)
        return full_text
    
    def find_key_index(self, keys, text):
        i=0
        for subkeys in keys:
            if (text == subsubkey for subsubkey in subkeys):
                if len(np.where([text == subsubkey for subsubkey in subkeys])[0]) > 0:
                    return i
                else:
                    i+=1
                    
    def fix_punctuation(self, translated):
        fixed_array = []
        for i in range(len(translated)):
            #print('Current str: ',translated[i])
            #print('i = ',i)
            if i < len(translated)-1:
                if (not translated[i+1].isalpha() and "'" not in translated[i+1]):
                    #print(translated[i+1], ' is not a word.')
                    new_str = str(translated[i]) + str(translated[i+1])
                    #print('New string: ',new_str)
                    fixed_array.append(new_str)
                else:
                    if translated[i].isalpha() or "'" in translated[i]: # Words contain apostrophes
                        fixed_array.append(translated[i])
            else:
                    if translated[i].isalpha() or "'" in translated[i]: 
                        fixed_array.append(translated[i])
                
        return fixed_array
            
                
    

# %%
piratey_speak().translation
