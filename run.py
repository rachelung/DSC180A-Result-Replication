#!/usr/bin/env python

import sys
import json
import subprocess
from etl import preprocess
from et1 import plot_word_


def main(targets):

    if 'data' in targets:
        with open('data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        #get_data(**data_cfg)

    return


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)


subprocess.call("auto_phrase_data_acquisition.sh", shell=True)
