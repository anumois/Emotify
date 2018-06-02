# -*- coding: utf-8 -*-

import datetime

from konlpy.tag import Twitter
twitter = Twitter()

class EmotifyElement:
    def __init__(self):
        self.Happy = 0
        self.Sad = 0
        self.Surprise = 0
        self.Anger = 0
        self.HappyKeyword = {}
        self.SadKeyword = {}
        self.SurpriseKeyword = {}
        self.AngerKeyword = {}

    def modHappy(self, _happy):
        self.Happy = _happy

    def modSad(self, _sad):
        self.Sad = _sad

    def modSurprise(self, _surprise):
        self.Surprise = _surprise

    def modAnger(self, _anger):
        self.Anger = _anger

    def addHappy(self, keyword, value):
        try:
            self.HappyKeyword[keyword] = value
        except KeyError:
            print("Error: No such Keyword")

    def addSad(self, keyword, value):
        try:
            self.SadKeyword[keyword] = value
        except KeyError:
            print("Error: No such Keyword")

    def addSurprise(self, keyword, value):
        try:
            self.SurpriseKeyword[keyword] = value
        except KeyError:
            print("Error: No such Keyword")

    def addAnger(self, keyword, value):
        try:
            self.AngerKeyword[keyword] = value
        except KeyError:
            print("Error: No such Keyword")

class EmotifyTimeList:
    def __init__(self):
        self.EmotifyTimeList = []

    def addElement(self, newElem):
        self.EmotifyTimeList.append(newElem)
            
class Emotify:
    def __init__(self):
        self.EmotifyList = []
        
    def addElement(self, newElem):
        self.EmotifyList.append(newElem)

pronouns = ['나', '너', '그', '놈', '그놈', '그녀', '그년', '년', '님', '것', '그것',
            '우리', '너희', '그들', '님들']
    
''''f = open("politician.txt", "r", -1, "utf-8")
keywords = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    keywords.append(line)
f.close()

for keyword in keywords:'''
if True:
    ETL = EmotifyTimeList()
    
    anger_date = [[(4, 16)],
                  [(4, 17)],
                  [(4, 18)],
                  [(4, 19)],
                  [(4, 20)],
                  [(4, 21)],
                  [(4, 22)],
                  [(4, 23)],
                  [(4, 24)],
                  [(4, 25)],
                  [(4, 26)],
                  [(4, 27)],
                  [(4, 28)],
                  [(4, 29)],
                  [(4, 30)],
                  [(5, 1)],
                  [(5, 2)],
                  [(5, 3)],
                  [(5, 4)],
                  [(5, 5)],
                  [(5, 6)],
                  [(5, 7)],
                  [(5, 8)],
                  [(5, 9)],
                  [(5, 10)],
                  [(5, 11)],
                  [(5, 12)],
                  [(5, 13)],
                  ]
    fear_date = [[(4, 16)],
                  [(4, 17)],
                  [(4, 18)],
                  [(4, 19)],
                  [(4, 20)],
                  [(4, 21)],
                  [(4, 22)],
                  [(4, 23)],
                  [(4, 24)],
                  [(4, 25)],
                  [(4, 26)],
                  [(4, 27)],
                  [(4, 28)],
                  [(4, 29)],
                  [(4, 30)],
                  [(5, 1)],
                  [(5, 2)],
                  [(5, 3)],
                  [(5, 4)],
                  [(5, 5)],
                  [(5, 6)],
                  [(5, 7)],
                  [(5, 8)],
                  [(5, 9)],
                  [(5, 10)],
                  [(5, 11)],
                  [(5, 12)],
                  [(5, 13)],
                  ]
    happy_date = [[(4, 16)],
                  [(4, 17)],
                  [(4, 18)],
                  [(4, 19)],
                  [(4, 20)],
                  [(4, 21)],
                  [(4, 22)],
                  [(4, 23)],
                  [(4, 24)],
                  [(4, 25)],
                  [(4, 26)],
                  [(4, 27)],
                  [(4, 28)],
                  [(4, 29)],
                  [(4, 30)],
                  [(5, 1)],
                  [(5, 2)],
                  [(5, 3)],
                  [(5, 4)],
                  [(5, 5)],
                  [(5, 6)],
                  [(5, 7)],
                  [(5, 8)],
                  [(5, 9)],
                  [(5, 10)],
                  [(5, 11)],
                  [(5, 12)],
                  [(5, 13)],
                  ]
    sad_date = [[(4, 16)],
                  [(4, 17)],
                  [(4, 18)],
                  [(4, 19)],
                  [(4, 20)],
                  [(4, 21)],
                  [(4, 22)],
                  [(4, 23)],
                  [(4, 24)],
                  [(4, 25)],
                  [(4, 26)],
                  [(4, 27)],
                  [(4, 28)],
                  [(4, 29)],
                  [(4, 30)],
                  [(5, 1)],
                  [(5, 2)],
                  [(5, 3)],
                  [(5, 4)],
                  [(5, 5)],
                  [(5, 6)],
                  [(5, 7)],
                  [(5, 8)],
                  [(5, 9)],
                  [(5, 10)],
                  [(5, 11)],
                  [(5, 12)],
                  [(5, 13)],
                  ]
    
    name = '대통령'
    
    name_anger = name + "_anger.txt"
    name_fear = name + "_fear.txt"
    name_happy = name + "_happy.txt"
    name_sad = name + "_sad.txt"
    
    import codecs
    with codecs.open(name_anger, encoding='utf-8') as f:
        anger_data = [line.split('\t') for line in f.read().splitlines()]
    import codecs
    with codecs.open(name_fear, encoding='utf-8') as f:
        fear_data = [line.split('\t') for line in f.read().splitlines()]
    import codecs
    with codecs.open(name_happy, encoding='utf-8') as f:
        happy_data = [line.split('\t') for line in f.read().splitlines()]
    import codecs
    with codecs.open(name_sad, encoding='utf-8') as f:
        sad_data = [line.split('\t') for line in f.read().splitlines()]
    
    if len(anger_data) != 0:
        for line in anger_data:
            dt = datetime.datetime.strptime(line[2], "%Y-%m-%d %H:%M")
            for day in anger_date:
                if day[0] == (dt.month, dt.day):
                    day.append(line)
                    break
                
    if len(fear_data) != 0:
        for line in fear_data:
            dt = datetime.datetime.strptime(line[2], "%Y-%m-%d %H:%M")
            for day in fear_date:
                if day[0] == (dt.month, dt.day):
                    day.append(line)
                    break
                
    if len(happy_data) != 0:
        for line in happy_data:
            dt = datetime.datetime.strptime(line[2], "%Y-%m-%d %H:%M")
            for day in happy_date:
                if day[0] == (dt.month, dt.day):
                    day.append(line)
                    break
                
    if len(sad_data) != 0:
        for line in sad_data:
            dt = datetime.datetime.strptime(line[2], "%Y-%m-%d %H:%M")
            for day in sad_date:
                if day[0] == (dt.month, dt.day):
                    day.append(line)
                    break
    
    n_dates = len(anger_date)
    for i in range(n_dates):
        EE = EmotifyElement()
        day = anger_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modAnger(EE.Anger + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    count = EE.AngerKeyword.get(word, 0)
                    EE.addAnger(word, count + n_tweets)
                    
        day = fear_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modSurprise(EE.Surprise + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    count = EE.SurpriseKeyword.get(word, 0)
                    EE.addSurprise(word, count + n_tweets)
                    
        day = happy_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modHappy(EE.Happy + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    count = EE.HappyKeyword.get(word, 0)
                    EE.addHappy(word, count + n_tweets)
                    
        day = sad_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modSad(EE.Sad + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    count = EE.SadKeyword.get(word, 0)
                    EE.addSad(word, count + n_tweets)
        
        for pronoun in pronouns:
            if pronoun in EE.AngerKeyword:
                del EE.AngerKeyword[pronoun]
            if pronoun in EE.SurpriseKeyword:
                del EE.SurpriseKeyword[pronoun]
            if pronoun in EE.HappyKeyword:
                del EE.HappyKeyword[pronoun]
            if pronoun in EE.SadKeyword:
                del EE.SadKeyword[pronoun]
                    
        ETL.addElement(EE)
        
print(ETL.EmotifyTimeList[0].Anger, ETL.EmotifyTimeList[1].Anger)
print(ETL.EmotifyTimeList[0].Surprise, ETL.EmotifyTimeList[1].Surprise)
print(ETL.EmotifyTimeList[0].Happy, ETL.EmotifyTimeList[1].Happy)
print(ETL.EmotifyTimeList[0].Sad, ETL.EmotifyTimeList[1].Sad)

import operator
sorted_freq = sorted(ETL.EmotifyTimeList[0].AngerKeyword.items(), key=operator.itemgetter(1), reverse = True)

anger_frequency = open("test0.txt", 'w', -1, "utf-8")

for t in sorted_freq:
    anger_frequency.write(t[0] + '\t' + str(t[1]) + '\n')
    
anger_frequency.close()

sorted_freq = sorted(ETL.EmotifyTimeList[1].AngerKeyword.items(), key=operator.itemgetter(1), reverse = True)

anger_frequency = open("test1.txt", 'w', -1, "utf-8")

for t in sorted_freq:
    anger_frequency.write(t[0] + '\t' + str(t[1]) + '\n')
    
anger_frequency.close()

sorted_freq = sorted(ETL.EmotifyTimeList[0].HappyKeyword.items(), key=operator.itemgetter(1), reverse = True)

anger_frequency = open("test2.txt", 'w', -1, "utf-8")

for t in sorted_freq:
    anger_frequency.write(t[0] + '\t' + str(t[1]) + '\n')
    
anger_frequency.close()