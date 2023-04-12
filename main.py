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
print(ds)

qstns_list = ds['question'].tolist()
answrs_list = ds['answer'].to_list()
#print(type(answrs_list))
#print(len(qstns_list))


#print(answrs_list)
q_neg, q_pos, q_neu = sentiment.tonality(qstns_list)
a_neg, a_pos, a_neu = sentiment.tonality(answrs_list)


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

print(ds)

#ds.insert('question', q_neg, 'answer')
#print(ds)

print("--- %s seconds ---" % (time.time() - start_time))
