'''
etl.py contains functions for use by other processes
'''
import sys
import glob
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def parse_arguments():
    """
    Parse the argument list and return a list
    of filenames.
    """
    # make sure additional arguments or flags have
    # been provided by the user
    if len(sys.argv) == 1:
        # why the program will not continue
        print("Not enough arguments have been provided")
        # how this can be corrected
        print("Usage: python gdp_plots.py <filenames>")
        print("Options:")
        print("-a : plot all gdp data sets in current directory")

    # check for -a flag in arguments
    if "-a" in sys.argv:
        filenames = glob.glob("*gdp*.csv")
    else:
        filenames = sys.argv[1:]

    return filenames
  
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
  
def create_plot(filename):
    """
    Creates a plot for the specified
    data file.
    """
    # read data into a pandas dataframe and transpose
    data = data.T
    
    # create a plot the transposed data
    ax = data.plot( title = filename )
    
    # set some plot attributes
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Per Capita")
    # set the x locations and labels
    ax.set_xticks( range(len(data.index)) )
    ax.set_xticklabels( data.index, rotation = 45 )
    
    # display the plot
    plt.show()

def n_gram(document, n):
  """ creates n-grams for specified n length of a document """
  string = document.split(" ")
  return pd.Series([string[i:i+n] for i in range(len(string))])
  


def plot_word_freq(dataframe):
  return plt.plot(dataframe['num_words'])

def plot_sentence_freq(dataframe):
  return plt.plot(dataframe['num_sentences'])


  
  
  
  
  
