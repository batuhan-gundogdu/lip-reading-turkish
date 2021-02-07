    # -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:25:10 2020

@author: benan

This script arranges the filenames of new videos
Just run inside the relevant folder 
"""

import os
here = os.getcwd() + "\\"
turkish_dict = {"ü" :"u","ç":"c", "ı":"i", "ö":"o", "ş":"s", "'":" ","ğ":"g","-":"","__":"_","i̇":"i" }

def under_scored_lower(word):
    underscored = word.replace(" ", "_")
    lowered_underscored = underscored.lower()
    return lowered_underscored

def letter_changer(word_):
    word = word_
#import string
    for old, new in turkish_dict.items():
        word = word.replace(old,new)
    new_word = word
    return new_word

def total_arrangement(path):
    lhere = os.listdir(path)

    for word in lhere:
        
        if word[-3:] == "mp4":    

            under_scored_lowered = under_scored_lower(word)
            new_word = letter_changer(under_scored_lowered)            
            os.rename(path + word, path + new_word) 
	      
total_arrangement(here)

