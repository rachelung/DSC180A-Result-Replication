import sys
import glob
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def n_gram(document, n):
  """ creates n-grams for specified n length of a document """
  string = document.split(" ")
  return pd.Series([string[i:i+n] for i in range(len(string))])

def plot_word_freq(dataframe):
  return plt.plot(dataframe['num_words'])

def plot_sentence_freq(dataframe):
  return plt.plot(dataframe['num_sentences'])
