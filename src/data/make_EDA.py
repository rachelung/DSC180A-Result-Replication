import pandas as pd
def chars_per_line(text_read_lines):
    return_dict = {}
    list_of_num_chars = []
    for line in text_read_lines:
        list_of_num_chars.append(len(line))
    return_dict['max_per_line'] = max(list_of_num_chars)
    return_dict['min_per_line'] = min(list_of_num_chars)
    return_dict['avg_per_line'] = sum(list_of_num_chars)/len(text_read_lines)
    return_dict['list_of_nums'] = list_of_num_chars
    return return_dict

def sent_per_line(text_read_lines):
    return_dict = {}
    list_of_nums = []
    for line in text_read_lines:
        dissected_line = line.split('.')
        list_of_nums.append(len(dissected_line))
    return_dict['max_sent_per_line'] = max(list_of_nums)
    return_dict['min_sent_per_line'] = min(list_of_nums)
    return_dict['avg_sent_per_line'] = sum(list_of_nums)/len(list_of_nums)
    return return_dict

def chars_per_sentence(text_read):
    return_dict = {}
    sentences = text_read.replace('\n','').split('.')
    list_of_num_chars = []
    for sentence in sentences:
        list_of_num_chars.append(len(sentence))
    return_dict['max_per_sent'] = max(list_of_num_chars)
    return_dict['min_per_sent'] = min(list_of_num_chars)
    return_dict['avg_per_sent'] = sum(list_of_num_chars)/len(sentences)
    return_dict['list_of_nums'] = list_of_num_chars
    return return_dict

def chars_per_sentence_adj(text_read):
    return_dict = {}
    sentences = text_read.replace('.\n.\n','.').split('.')
    list_of_num_chars = []
    list2 = []
    for sentence in sentences:
        list_of_num_chars.append(len(sentence))
    list2 = list_of_num_chars
    return_dict['max_per_sent'] = max(list2)
    return_dict['min_per_sent'] = min(list2)
    return_dict['avg_per_sent'] = sum(list2)/len(list2)
    return_dict['list_of_nums'] = list2
    return return_dict

def total_words_in_corpus(text_read_lines):
    dict_results = {}
    all_words = []
    for line in text_read_lines:
        split_doc = line.split()
        for word in split_doc:
            all_words.append(word)
    dict_results['len_all_words'] = len(all_words)
    dict_results['unique'] = pd.Series(all_words).value_counts()
    return dict_results
