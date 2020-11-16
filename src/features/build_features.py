import sys
import glob
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def preprocess(df):
  """
  takes in a pandas dataframe, applying some preprocessing
  """
  df[0] = df[0].apply(lambda w: w.lower()) # makes all words lowercase
  df['listed'] = df[0].apply(lambda x: x.split(" ")) # changes representation from string -> list of strings
  df['num_words'] = df['listed'].apply(len) # words per document
  df['num_sentences'] = df[0].apply(lambda x: x.count('.')) # sentences per document, number of periods
  return df
