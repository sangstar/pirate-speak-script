<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


=======
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
>>>>>>> master
import requests
import numpy as np
import re
import sys
import os


<<<<<<< HEAD
# In[ ]:


=======
# %%
>>>>>>> master
class piratey_speak:
    
    
    def __init__(self):
<<<<<<< HEAD
            ESC = "\x1b"
            self.to_translate = ""
            self.piratey_mappings = {"'n":"and",'be':['is','am'], 'aye':['yes','yup','yeah'],'me':'my','ye':'you','hearties':['friends','companions','buddies'],'lad':['young man','young male'],'mate':['friend','dude','bro'],'bounty':['reward', 'prize']}
=======
            print("To close, type: Exit")
            self.to_translate = ""
            self.piratey_mappings = {"Ahoy":["Hello","Hey"],"'n":"and",'be':['is','am','are'], 'aye':['yes','yup','yeah'],'me':'my','ye':'you','hearties':['friends','companions','buddies'],'lad':['young man','young male'],'matey':['friend','dude','bro','mate'],'bounty':['reward', 'prize']}
>>>>>>> master
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
<<<<<<< HEAD
        #print(text)
        #print(text)
        #print(words)
        items = list(words.items())
        #print(list(words.values()))
        for subtext in text:
            #print('subtext :', subtext)
=======
        items = list(words.items())
        for subtext in text:
>>>>>>> master
            if subtext.endswith("ing"):
                text_matchin_location = np.where([subtext.endswith("ing") for subtext in text])[0][0]  # Hopefully the joke with the naming is ascertained here.. 
                text[text_matchin_location] = subtext.replace("ing","in'")
            for word in words.values():
<<<<<<< HEAD
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
=======
                if not isinstance(word, list):
                    if word == subtext:
                        match_location = np.where([word == value for value in list(words.values())])[0][0]
                        text_match_location = np.where([subtext == word for subtext in text])[0][0]
                        pirate_word = list(words)[match_location]
                        text[text_match_location] = pirate_word
                else: 
                    if subtext in word:
                        word_location = np.where([subtext == option for option in word])[0][0]
                        word = word[word_location]
                        val_location = self.find_key_index(list(words.values()),subtext)
                        text_match_location = np.where([subtext == word for subtext in text])[0][0]
                        pirate_word = list(words)[val_location]
                        text[text_match_location] = pirate_word
        #print('Text before fixed: ', text)
        text = self.fix_punctuation(text)
        #print('Fixed text: ', text)
>>>>>>> master
        full_text = " ".join(text)
        return full_text
    
    def find_key_index(self, keys, text):
<<<<<<< HEAD
        #print('keys : ', keys)
        #print('text to find : ', text)
        i=0
        for subkeys in keys:
            #print('i = ', i)
            #print('subkey = ',subkeys)
            if (text == subsubkey for subsubkey in subkeys):
                #print(np.where([text == subsubkey for subsubkey in subkeys])[0])
=======
        i=0
        for subkeys in keys:
            if (text == subsubkey for subsubkey in subkeys):
>>>>>>> master
                if len(np.where([text == subsubkey for subsubkey in subkeys])[0]) > 0:
                    return i
                else:
                    i+=1
<<<<<<< HEAD
                
    


# In[ ]:


piratey_speak().translation

=======
                    
    def fix_punctuation(self, translated):
        fixed_array = []
        for i in range(len(translated)-1):
            #print('Current str: ',translated[i])
            if (not translated[i+1].isalpha() and "'" not in translated[i+1]):
                #print(translated[i+1], ' is not a word.')
                new_str = str(translated[i]) + str(translated[i+1])
                #print('New string: ',new_str)
                fixed_array.append(new_str)
            else:
                if translated[i].isalpha() or "'" in translated[i]: # Words contain apostrophes
                    fixed_array.append(translated[i])
        return fixed_array
            
                
    

# %%
piratey_speak().translation

# %%
# To fix puncutuation: If next element isn't a letter, add it to the end of the last element

# %%
>>>>>>> master
