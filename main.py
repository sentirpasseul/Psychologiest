import pandas as pd
import numpy as np
import json
import requests
import urllib.request as ur
import os
import modin.pandas as mpd
import time
import pymorphy2
start_time = time.time()
morph = pymorphy2.MorphAnalyzer()


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
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1200)
pd.set_option('max_colwidth', None)
ds = pd.read_csv('dataset.csv')[0:30] #Временно указал 30 первых строчек, чтобы не убить процессор

#nds = ds[1::]

del ds['N']
ds.index +=1

ds_quests = ds['question']
ds_answer = ds['answer']
ds_relevance = ds['relevance']

for row in ds_quests:
        msg = str(row).split()
        ar_parse = []
        for word in range(len(msg)):
            #ar_parse.append(w)
            print(morph.parse(msg[word]))

print(ds_quests.describe())


print("--- %s seconds ---" % (time.time() - start_time))
