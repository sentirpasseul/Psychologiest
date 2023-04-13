import pandas as pd
import numpy as np
import json
import requests
import urllib.request as ur
import os
import modin.pandas as mpd
import time
from transformers import pipeline
import sentiment
import analyzer
start_time = time.time()


#url = 'https://datasets-server.huggingface.co/first-rows?dataset=Den4ikAI%2Frussian_dialogues&config=Den4ikAI--russian_dialogues&split=train'
#ur.urlretrieve(url, 'dataset.json')

#ds = pd.read_json('src/dataset.jsonl', lines=True)
reviews = ''
#print("--- %s seconds ---" % (time.time() - start_time))
"""
with open('src/dataset.jsonl','r') as f:
    for line in f.readlines()[0:1000]:
        reviews += line
                                            #УВЕЛИЧИЛ СКОРОСТЬ ЧТЕНИЯ JSON Х3
ds = pd.read_json(reviews, lines=True)
"""
#pd.DataFrame.to_csv(ds, 'dataset.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
ds = pd.read_csv('dataset.csv')

#nds = ds[1::]

del ds['N']
ds.index +=1
#print(ds)

qstns_list = ds['question'].tolist()
answrs_list = ds['answer'].to_list()
#print(answrs_list)
#print(type(answrs_list))
#print(len(qstns_list))


#print(answrs_list)
q_ds = sentiment.tonality(qstns_list[130:140])
a_ds = sentiment.tonality(answrs_list[130:140])


#q_ds.reset_index()
#del a_ds[0]
#q_ds.to_csv('src/q_ds.csv')
#a_ds.to_csv('src/a_ds.csv')

#q_ds = pd.read_csv('src/q_ds.csv')
#q_ds.drop('Unnamed', axis=1)
#a_ds = pd.read_csv('src/a_ds.csv')

print('-'*50)
print("Таблица тональности вопросов:")
print('-'*50)
print(q_ds)
print('-'*50)

print()
print()

print('-'*50)
print("Таблица тональности ответов:")
print('-'*50)
print(a_ds)
print('-'*50)

answrs_interj = analyzer.Analyzer().getInterj(answrs_list[130:140])
qstns_interj = analyzer.Analyzer().getInterj(qstns_list[130:140])


def getFrequency(array: list):
    return np.sum(array)

freq_qstns = getFrequency(qstns_interj[130:140])
freq_answrs = getFrequency(answrs_interj[130:140])

#print(len(answrs_interj))

qstns_interj_ds = pd.DataFrame()
qstns_interj_ds['question'] = qstns_list
qstns_interj_ds['intj'] = qstns_interj

print('-'*50)
print("Таблица междометий в вопросах")
print('-'*50)
print(qstns_interj_ds[0:30])
print('-'*50)
print("Частота встречаемости междометий:", freq_qstns)
print('-'*50)
print("\n"*3)

answrs_interj_ds = pd.DataFrame()
answrs_interj_ds['answer'] = answrs_list
answrs_interj_ds['intj'] = answrs_interj
print('-'*50)
print("Таблица междометий в ответах")
print(answrs_interj_ds[0:30])
print('-'*50)
print("Частота встречаемости междометий:", freq_answrs)
print('-'*50)
print("\n"*3)


#print(qstns_interj_ds)
#print(q_ds)
#print(a_ds)
#print(len(q_neg))
#print(q_neu)
#print(q_pos)
#print(q_neg)

#ds['q_neu'] = q_neu
#ds['q_pos'] = q_pos
#ds['q_neg'] = q_neg

#ds['a_neu'] = [a_neu]
#ds['a_pos'] = [a_pos]
#ds['a_neg'] = [a_neg]

#print(ds)

#ds.insert('question', q_neg, 'answer')
#print(ds)

print("--- %s seconds ---" % (time.time() - start_time))
