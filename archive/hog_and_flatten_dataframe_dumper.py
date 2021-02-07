# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




import numpy as np
from skimage.filters import prewitt,sobel,scharr,gaussian
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import os
from skimage import data
import matplotlib.pyplot as plt
from PIL import Image
from IPython import display
import time
from skimage.feature import hog
import joblib
import pandas as pd
#%capture

hog_set=[]

dataset_dir = "frames"

terms = os.listdir(dataset_dir)
print(len(terms))
flt_img_list = []
for term in terms:
    if not term.startswith('.'):
        print(term)
        class_file=os.path.join(dataset_dir,term)
        frames=os.listdir(class_file)
        for frame in frames:
            img_name=os.path.join(class_file,frame)
            img = Image.open(img_name)
            flat_img = np.array(img).flatten()
            flt_img_list.append(flat_img)
            # display.display(img)
            # display.clear_output(wait=True)            
            fd = hog(img)
            hog_set.append(fd)
hog_set[0].shape
df_hog = pd.DataFrame(hog_set)
df_hog.to_csv("hog_dataframe.csv")
#%%
df = pd.DataFrame(flt_img_list)
df.to_csv("flatten_dataframe.csv")
#%%


