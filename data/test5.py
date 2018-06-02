# -*- coding: utf-8 -*

import codecs
with codecs.open("부산기장군수.txt", encoding='utf-8') as f:
    data_test = [line.split('\t') for line in f.read().splitlines()]
    
print(len(data_test))
