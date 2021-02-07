    # -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:25:10 2020

@author: benan

This script arranges the filenames of new videos
Just run inside the relevant folder 
"""

import os
here = os.getcwd() + "\\"
turkish_dict = {"ü" :"u","ç":"c", "ı":"i", "ö":"o", "ş":"s", "'":" ","ğ":"g" }

def under_scored_lower(word):
    underscored = word.replace(" ", "_")
    lowered_underscored = underscored.lower()
    return lowered_underscored
counter = 1  
def letter_changer(word_):
    word = word_
#import string
    for old, new in turkish_dict.items():
        word = word.replace(old,new)
    new_word = word
    return new_word

def total_arrangement(path):
    lhere = os.listdir(path)
    counter = 1
    for word in lhere:
        
        if os.path.isdir(path + word):    
            
            under_scored_lowered = under_scored_lower(word)
            new_word = letter_changer(under_scored_lowered)            
            os.rename(path + word, path + str(counter) +"_" + new_word) 
            counter += 1
total_arrangement(here)

#lhere = os.listdir(here)
#counter = 1
#for word in lhere:
#    
#    if os.path.isdir(here + word):
#        counter += 1
#        under_scored_lowered = under_scored_lower(word)
#        new_word = letter_changer(under_scored_lowered)            
#        os.rename(here + word, here + str(counter) +"_" + new_word) 
