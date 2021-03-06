# DSC180A-Result-Replication

WIP

Original Autophrase: https://github.com/shangjingbo1226/AutoPhrase \
Lecture: https://docs.google.com/presentation/d/11G4jnAL88mJGUB1rnjOupDGj3wRoSCSAV8kriX_J3RY/edit?usp=sharing \
Report: https://docs.google.com/document/d/1hiMhx4a7hAWtOkaTgXeq9mJtb7TsjOXE6ypZMtc4J4I/edit

# Description of Checkpoint 1 - Code Portion
From: https://dsc-capstone.github.io/assignments/quarter-1-replication/#checkpoint-1 \
Code Portion:

Your code should be turned in via GitHub. It should:

- conform to the template structure discussed in lecture,
- contain a rudimentary data ingestion pipeline,
- include documentation both in your README.md, describing the purpose of the code, its contents, and how to run it.
- be runnable runnable via the command python run.py data. Include a data-params.json file in the config directory, which specifies any data-input locations. If your data-ingestion requires data that is on your local computer, include a copy of the data in your domain’s /teams directory on the DSMLP server and include that location in your data-params.json.

# (Checkpoint 1) Guidelines as established by project mentor:

1. Related work: Try to summarize the lecture and fuse it together with AutoPhrase's related work. Paraphrase is required. Plagiarization is not allowed.

2. Run.py: Try to use it to parse the config file, which may contain some model names, data file names/urls, .... You can download the necessary files and generate a new bash file for your purpose. And then, use the python command-line to call it.

3. You may consider use git submodule to incorporate the AutoPhrase repo into your repo.

4. For the DBLP.5k.txt, it is there in the AutoPhrase repo. For the DBLP.txt, you just need to revise the input filename, the bash script will help you download it automatically.

5. You may find docker helpful and we may need to talk to Aaron about the C++/Java things.

6. For the report, we don't expect a very long writeup. Try to be concise and complete.

7. You are only asked to play with AutoPhrase and compare the two runs using DBLP.5k.txt and DBLP.txt. No other baselines are required. These two runs are expected to be significantly different.

For both the Report and Code Portion, write in a Canvas comment listing what tasks each group member was responsible for.
site: https://dsc-capstone.github.io/assignments/quarter-1-replication/#checkpoint-1

# (Checkpoint 2) Guidelines as established by project mentor:

1. Incorporate data cleaning code into your pipeline, if relevant. You can do some extra cleanings than the ones already there in AutoPhrase.

2. Develop code that generates analysis/figures for EDA.

3. Implement the methods that generate results. Here, you are asked to generate some bash script and call it to leverage AutoPhrase.

# (Final) Guidelines as established by project mentor:
1. Try to randomly pick 100 multi-word phrases whose scores are greater than 0.5. Manually check them and see what's the percentage of high-quality phrases.

2. Since these 100 multi-word phrases can be ranked by their scores, please plot a precision-recall curve too.

3. Try to run the word2vec code on the phrasal segmentation results to obtain phrase embedding. 

4. Pick 3 high-quality phrases from your previous annotations in step 1, run a similarity search among all multi-word phrases whose scores are greater than 0.5, and report the top-5 results. Comment on the results. 

# run.py
Running run.py (via python run.py) simply runs the bash script file auto_phrase_data_acquisition.sh

# auto_phrase_data_acquisition.sh
This file identifies the current folder that houses the data for use later (in this case, it is hard-coded to data/raw folder). This folder currently holds some data already (DBLP.5K.txt) but this bash script also downloads some additional data (DBLP.txt) to this same folder. 

### Responsibilites
Rachel Ung developed the Github repo, including all folders, run.py, and README.md; restyled report portion in LaTeX.\
Vincent Le developed the raw report portion of Checkpoint 1, added auto_phrase_data_acquisition.sh, edited run.py and README.md

