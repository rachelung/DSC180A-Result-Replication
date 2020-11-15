'''
etl.py contains functions for use by other processes
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def n_gram(document, n):
  ''' creates n-grams for specified n length of a document '''
  string = document.split(" ")
  return pd.Series([string[i:i+n] for i in range(len(string))])
  
def preprocess(text_file):
  ''' takes in a text_file to reformat file into a pandas dataframe'''
  df = pd.read_csv(text_file, header=None, sep='\n') # reads each line in as its own document
  df[0] = df[0].apply(lambda w: w.lower()) # makes all words lowercase
  df['listed'] = df[0].apply(lambda x: x.split(" ")) # changes representation from string -> list of strings
  df['num_words'] = df['listed'].apply(len) # words per document
  df['num_sentences'] = df[0].apply(lambda x: x.count('.')) # sentences per document, number of periods
  return df

def plot_word_freq(dataframe):
  return plt.plot(dataframe['num_words'])

def plot_sentence_freq(dataframe):
  return plt.plot(dataframe['num_sentences'])


  
  
  
  
  
