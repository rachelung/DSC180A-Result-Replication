import nbformat as nbf
nb = nbf.v4.new_notebook()


Header = """\
# EDA For Input Corpus
This jupyter notebook serves to show the statistics regarding our input corpus, which is DBLP.5K by default"""

imports = """\
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import numpy as np
%matplotlib inline"""

change_path = """\
os.chdir("../")"""

read_json = """\
with open('config/input.json') as f:
    json_data = json.load(f)"""

read_in_file = """\
input_corpus = open(json_data['input'], 'r', encoding="utf8")  
Line_by_line = input_corpus.readlines()"""

obtain_stats_per_line = """\
#Obtaining the min, max, and average number of characters per line from the text corpus
max_char = 0
min_char = 1000
char_sum = 0
for line in Line_by_line:
    len_doc = len(line)
    char_sum += len_doc
    if len_doc > max_char:
        max_char = len_doc
    if len_doc < min_char:
        min_char = len_doc
print("Maximum number of characters per line is: " + str(max_char))
print("Minimum number of characters per line is: " + str(min_char))
print("Average number of characters per line is: " + str(char_sum/5000))
input_corpus.close()"""

obtain_stats_per_sentence = """\
#Obtaining the min, max, and average number of characters per sentence from the text corpus
input_corpus_again = open(json_data['input'], 'r', encoding='utf-8') 
Lines_total = input_corpus_again.read()
sentences = Lines_total.replace('\\n','').split('.')
avg_len_sent = 0
max_sent_len = 0
min_sent_len = 1000
for sentence in sentences:
    avg_len_sent += len(sentence)
    if len(sentence) > max_sent_len:
        max_sent_len = len(sentence)
    if len(sentence) < min_sent_len:
        min_sent_len = len(sentence)
print("Maximum number of characters per sentence is: " + str(max_sent_len))
print("Minimum number of characters per sentence is: " + str(min_sent_len))
print("Average number of characters per sentence is: " + str(avg_len_sent/len(sentences)))
input_corpus_again.close()"""

obtain_stats_words = """\
input_corpus_once_more = open(json_data['input'], 'r', encoding='utf-8')
Line_by_line = input_corpus_once_more.readlines()
all_words = []
for line in Line_by_line:
    split_doc = line.split()
    for word in split_doc:
        all_words.append(word)

print("Total number of words in input corpus is: " + str(len(all_words)))
input_corpus_once_more.close()"""

value_counts_of_words = """\
vals = pd.Series(all_words).value_counts()
vals

#Uncomment to see word count of rare words (less than 5 occurances)
#vals[vals < 5]"""

nb['cells'] = [nbf.v4.new_markdown_cell(Header),
               nbf.v4.new_code_cell(imports),
               nbf.v4.new_code_cell(change_path),
               nbf.v4.new_code_cell(read_json),
               nbf.v4.new_code_cell(read_in_file),
               nbf.v4.new_code_cell(obtain_stats_per_line),
               nbf.v4.new_code_cell(obtain_stats_per_sentence),
               nbf.v4.new_code_cell(obtain_stats_words),
               nbf.v4.new_code_cell(value_counts_of_words)]

with open('notebooks/input_EDA.ipynb', 'w', encoding="utf-8") as f:
    nbf.write(nb, f)
