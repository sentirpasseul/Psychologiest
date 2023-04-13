from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import fasttext
import re
import string
import numpy as np
from prepocess import Preprocess

import pandas as pd

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'src/fasttext-social-network-model.bin'


def isNone(number):
    if number is None:
        return 0
    else: return number

def getNeu(sentiment):
    return sentiment.get('neutral')

def getPos(sentiment):
    return sentiment.get('positive')

def getNeg(sentiment):
    return sentiment.get('negative')

def getSeries(array: list):
    return pd.Series(array)


def tonality(text_list: list):
    #fasttext.FastText.eprint = lambda x: None
    FastTextSocialNetworkModel.MODEL_PATH = 'src/fasttext-social-network-model.bin'

    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    text_list = Preprocess().prepSent(text_list)
    for sentence in text_list:
        tokens = tokenizer.split(sentence)

    results = model.predict(text_list, k=2)


    #for sentence in text_list:
    #print(len(results))
    #print("RES:", results)
    neu_list = list()
    neg_list = list()
    pos_list = list()


    for sentence, sentiment in zip(text_list, results):
        #if sentence != string.digits:

        # Анализ Тональности предложения
        neu = isNone(sentiment.get('neutral'))
        pos = isNone(sentiment.get('positive'))
        neg = isNone(sentiment.get('negative'))
        neu_list.append(neu)
        pos_list.append(pos)
        neg_list.append(neg)


        """
        print(sentence, '\n',
             'neutral = ', neu, '\n',
             'positive = ', pos, '\n'
             'negative = ', neg, '\n'
             )
        """
    ds = pd.DataFrame()
    ds['sentence'] = text_list
    ds['neu_list'] = neu_list
    ds['pos_list'] = pos_list
    ds['neg_list'] = neg_list

    return ds


