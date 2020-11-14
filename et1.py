import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
'''
etl.py contains functions for use by other processes
'''
def n_gram(document, n):
  ''' creates n-grams for specified n length of a document '''
  string = document.split(" ")
  return pd.Series([string[i:i+n] for i in range(len(string))])
  
def preprocess(text_file):
  ''' takes in a text_file to reformat file into a pandas dataframe'''
  df = pd.read_csv(text_file, header=None, sep='\n') # reads each line in as its own document
  df[0] = df[0].apply(lambda w: w.str.lower()) # makes all words lowercase
  df['listed'] = df[0].apply(lambda x: x.str.split(" ")) # changes representation from string -> list of strings
  df['length'] = df['listed'].apply(len) # adds length of document 
  return df
  
  
  
