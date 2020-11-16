#!/usr/bin/env python

import sys
import json
import subprocess
from data import get_data
from features import preprocess


def main(targets):

    if 'data' in targets:
        with open('data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        get_data(**data_cfg)

    return

    if 'features' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        
        # preprocessing textfile; resulting dataframe
        preprocessed = preprocess(**data_cfg)
        
    if 'EDA' in targets:
        subprocess.call(["python", "create_EDA_notebook.py"])
        
    

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)


subprocess.call("auto_phrase_data_acquisition.sh", shell=True)
