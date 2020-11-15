import sys
import glob
import os
from zipfile import ZipFile
from env_setup import auth
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def preprocess(text_file):
  """
  takes in a text_file to reformat file into a pandas dataframe
  """
  df = pd.read_csv(text_file, header=None, sep='\n') # reads each line in as its own document
  df[0] = df[0].apply(lambda w: w.lower()) # makes all words lowercase
  df['listed'] = df[0].apply(lambda x: x.split(" ")) # changes representation from string -> list of strings
  df['num_words'] = df['listed'].apply(len) # words per document
  df['num_sentences'] = df[0].apply(lambda x: x.count('.')) # sentences per document, number of periods
  return df

def get_data(outdir):
  """
  download data
  """
  

# for kaggle (?)
# try:
    #import kaggle
# except OSError:
    # credentials not yet set
    # auth()
    # import kaggle
    

#def get_data(outdir):
    #'''
    #download and unzip titanic data from Kaggle.
    #'''
    #kaggle.api.authenticate()
    #kaggle.api.competition_download_files(
        #'titanic', 
       # path=outdir
    #)

    # unzip output
    #p = os.path.join(outdir, 'titanic.zip')
    #with ZipFile(fp) as zf:
        #zf.extractall(outdir)

    # remove zip file
    #os.remove(fp)

    #return read_train(outdir)
    
  
