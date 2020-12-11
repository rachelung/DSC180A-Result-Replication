import sys
import glob
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def get_data(outdir):
  """
  download data
  """
  df = pd.read_csv(outdir, header=None, sep='\n') # reads each line in as its own document
  return df

  

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
    
 #def read_train(datadir):
    #'''
    #Reads raw training data from disk.
    #(Would normally be more complicated!)
    #'''
    #fp = os.path.join(datadir, 'train.csv')
    #return pd.read_csv(fp)


#def read_test(datadir):
    #'''
    #Reads raw test data from disk.
    #(Would normally be more complicated!)
    #'''

    #fp = os.path.join(datadir, 'test.csv')
    #return pd.read_csv(fp)
    
  
