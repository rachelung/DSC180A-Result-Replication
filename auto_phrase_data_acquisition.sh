#!/bin/bash
# In effect, the commands below check to see if we're running in a Docker container--in that case, the (default) 
# "data" and "models" directories will have been renamed, in order to avoid conflicts with mounted directories 
# with the same names.
#
# DATA_DIR is the default directory for reading data files.  Because this directory contains not only the default
# dataset, but also language-specific files and "BAD_POS_TAGS.TXT", in most cases it's a bad idea to change it.
# However, when this script is run from a Docker container, it's perfectly fine for the user to mount an external
# directory called "data" and read the corpus from there, since the directory holding the language-specific files
# and "BAD_POS_TAGS.txt" will have been renamed to "default_data".
if [ -d "default_data" ]; then
    DATA_DIR=${DATA_DIR:- default_data}
else
    DATA_DIR=${DATA_DIR:- data/raw}
fi

# RAW_TRAIN is the input of AutoPhrase, where each line is a single document.
DEFAULT_TRAIN=${DATA_DIR}/EN/DBLP.5K.txt
RAW_TRAIN=${RAW_TRAIN:- $DEFAULT_TRAIN}

green=`tput setaf 2`
reset=`tput sgr0`

echo ${green}===Downloading Toy Dataset===${reset}
curl http://dmserv2.cs.illinois.edu/data/DBLP.txt.gz --output ${DATA_DIR}/EN/DBLP.txt.gz
gzip -d ${DATA_DIR}/EN/DBLP.txt.gz -f
