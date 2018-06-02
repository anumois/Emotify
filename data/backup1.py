# -*- coding: utf-8 -*-

import numpy as np
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

model1 = joblib.load('model1.pkl')

import codecs
with codecs.open("대통령.txt", encoding='utf-8') as f:
    data_test = [line.split('\t') for line in f.read().splitlines()]

X_test = list(zip(*data_test))[0]

emotion = model1.predict(X_test)

result = open("result.txt", 'w', -1, "utf-8")

i = 0
for e in emotion:
    result.write(data_test[i][0] + '\t' + str(e) + '\n')
    i = i + 1
    
result.close()