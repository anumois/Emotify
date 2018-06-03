# -*- coding: utf-8 -*-

import re
import numpy as np
import codecs
with codecs.open("train_data_non_EMOJI.txt", encoding='utf-8') as f:
    data = [line.split('\t') for line in f.read().splitlines()]

X = list(zip(*data))[0]
y = np.array(list(zip(*data))[1], dtype=int)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from konlpy.tag import Twitter

twitter = Twitter()
model1 = Pipeline([
    ('vect', CountVectorizer(tokenizer=twitter.morphs)), 
    ('mb', MultinomialNB()),
    ])
model1.fit(X, y)

import codecs
with codecs.open("test_data_non_EMOJI.txt", encoding='utf-8') as f:
    data_test = [line.split('\t') for line in f.read().splitlines()]

name = "test_data_non_EMOJI"

name_anger = name + "_anger.txt"
name_fear = name + "_fear.txt"
name_happy = name + "_happy.txt"
name_sad = name + "_sad.txt"
anger_result = open(name_anger, 'w', -1, "utf-8")
fear_result = open(name_fear, 'w', -1, "utf-8")
happy_result = open(name_happy, 'w', -1, "utf-8")
sad_result = open(name_sad, 'w', -1, "utf-8")

X_test = list(zip(*data_test))[0]
e_predict = model1.predict(X_test)
    
i = 0
for line in data_test:
    if e_predict[i] == 0:
        anger_result.write(line[0] + '\t' + line[1] + '\n')
    elif e_predict[i] == 1:
        fear_result.write(line[0] + '\t' + line[1] + '\n')
    elif e_predict[i] == 2:
        happy_result.write(line[0] + '\t' + line[1] + '\n')
    elif e_predict[i] == 3:
        sad_result.write(line[0] + '\t' + line[1] + '\n')
    i = i + 1
        
anger_result.close()
fear_result.close()
happy_result.close()
sad_result.close()