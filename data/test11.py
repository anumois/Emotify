# -*- coding: utf-8 -*-

Kangwon = ['����', '������', '����', '��', '����', '��ô', '����', '�籸', '���', '����', '����', '����', '����', 'ö��', '��õ', '�¹�', '��â', 'ȫõ', 'ȭõ', 'Ⱦ��']
Kyunggi = ['���', '������', '����', '���', '��õ', '����', '����', '����', '����', '����', '������', '����õ', '��õ', '����', '����', '����', '�Ȼ�', '�ȼ�', '�Ⱦ�', '����', '����', '����', '��õ', '����', '����', '�ǿ�', '������', '��õ', '����', '����', '��õ', '�ϳ�', 'ȭ��']
Kyungnam = ['�泲','������', '����', '��â', '��', '����', '����', '�о�', '��õ', '��û', '���', '�Ƿ�', '����', 'â��', 'â��', '�뿵', '�ϵ�', '�Ծ�', '�Ծ�', '��õ']
Kyungbuk = ['���', '������', '���', '����', '���', '����', '����', '��õ', '����', '��ȭ', '����', '����', '�ȵ�', '����', '����', '����', '��õ', '��õ', '�︪', '����', '�Ǽ�', 'û��', 'û��', 'û��', 'ĥ��', '����']
Jeonnam = ['����', '������', '����', '����', '�', '����', '����', '����', '���', '����', '����', '����', '��õ', '�ž�', '����', '����', '����', '�ϵ�', '�强', '����', '����', '����', '�س�', 'ȭ��']
Jeonbuk = ['����','������', '��â', '����', '����', '����', '����', '�ξ�', '��â', '����', '�ͻ�', '�ӽ�', '���', '����', '����', '����']
Chungnam = ['�泲', '������', '���', '����', '�ݻ�', '���', '����', '����', '�ο�', '����', '��õ', '�ƻ�', '����', 'õ��', 'û��', '�¾�', 'ȫ��']
Chungbuk = ['���', '������', '����', '�ܾ�', '����', '����', '��õ', '����', '��õ', '����', '��õ', 'û��', '����']
Jeju = ['����', 'Ư����ġ������']
Kwangju = ['����', '��������']
Daegu = ['�뱸', '��������', '�޼�']
Daejeon = ['����','��������']
Busan = ['�λ�','��������', '����']
Seoul = ['����','Ư������']
Ulsan = ['���', '��������', '����']
Incheon = ['��õ', '��������', '��ȭ', '����']
Sejong = ['����', 'Ư����ġ����']

LocationList = [Kangwon, Kyunggi, Kyungnam, Kyungbuk, Jeonnam, Jeonbuk, Chungnam, Chungbuk, Jeju, Kwangju, Daegu, Daejeon, Busan, Seoul, Ulsan, Incheon, Sejong]

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

pronouns = ['��', '��', '��', '��', '�׳�', '�׳�', '�׳�', '��', '��', '��', '�װ�',
            '�츮', '����', '�׵�', '�Ե�']
    
f = open("politician.txt", "r", -1, "utf-8")
keywords = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    keywords.append(line)
f.close()

emotify = Emotify()

for keyword in keywords:
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
                  [(5, 14)],
                  [(5, 15)],
                  [(5, 16)],
                  [(5, 17)],
                  [(5, 18)],
                  [(5, 19)],
                  [(5, 20)],
                  [(5, 21)],
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
                  [(5, 14)],
                  [(5, 15)],
                  [(5, 16)],
                  [(5, 17)],
                  [(5, 18)],
                  [(5, 19)],
                  [(5, 20)],
                  [(5, 21)],
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
                  [(5, 14)],
                  [(5, 15)],
                  [(5, 16)],
                  [(5, 17)],
                  [(5, 18)],
                  [(5, 19)],
                  [(5, 20)],
                  [(5, 21)],
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
                  [(5, 14)],
                  [(5, 15)],
                  [(5, 16)],
                  [(5, 17)],
                  [(5, 18)],
                  [(5, 19)],
                  [(5, 20)],
                  [(5, 21)],
                  ]
    
    name = keyword.split('"')[1]
    
    loc1 = ''
    loc2 = ''
    
    if '�����' in name:
        loc1 = '����'
        loc2 = '�����'
    else:
        for Loc1 in LocationList:
            if Loc1[0] in name:
                for Loc2 in Loc1[1:]:
                    if Loc2 in name:
                        loc1 = Loc1[0]
                        loc2 = Loc2
                        break
                break
    
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
                    value = EE.AngerKeyword.get(word, (0, []))
                    new_cnt = value[0]
                    new_cnt = new_cnt + n_tweets
                    new_lst = value[1]
                    if len(new_lst) < 5:
                        if not text in new_lst:
                            new_lst.append(text)
                    EE.addAnger(word, (new_cnt, new_lst))
                    
        day = fear_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modSurprise(EE.Surprise + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    value = EE.SurpriseKeyword.get(word, (0, []))
                    new_cnt = value[0]
                    new_cnt = new_cnt + n_tweets
                    new_lst = value[1]
                    if len(new_lst) < 5:
                        if not text in new_lst:
                            new_lst.append(text)
                    EE.addSurprise(word, (new_cnt, new_lst))
                    
        day = happy_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modHappy(EE.Happy + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    value = EE.HappyKeyword.get(word, (0, []))
                    new_cnt = value[0]
                    new_cnt = new_cnt + n_tweets
                    new_lst = value[1]
                    if len(new_lst) < 5:
                        if not text in new_lst:
                            new_lst.append(text)
                    EE.addHappy(word, (new_cnt, new_lst))
                    
        day = sad_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modSad(EE.Sad + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    value = EE.SadKeyword.get(word, (0, []))
                    new_cnt = value[0]
                    new_cnt = new_cnt + n_tweets
                    new_lst = value[1]
                    if len(new_lst) < 5:
                        if not text in new_lst:
                            new_lst.append(text)
                    EE.addSad(word, (new_cnt, new_lst))
        
        for pronoun in pronouns:
            if pronoun in EE.AngerKeyword:
                del EE.AngerKeyword[pronoun]
            if pronoun in EE.SurpriseKeyword:
                del EE.SurpriseKeyword[pronoun]
            if pronoun in EE.HappyKeyword:
                del EE.HappyKeyword[pronoun]
            if pronoun in EE.SadKeyword:
                del EE.SadKeyword[pronoun]
                
        keyword_lst = keyword.split('"')
        i = 1
        while len(keyword_lst) > i:
            nouns = twitter.nouns(keyword_lst[i])
            for noun in nouns:
                if noun in EE.AngerKeyword:
                    del EE.AngerKeyword[noun]
                if noun in EE.SurpriseKeyword:
                    del EE.SurpriseKeyword[noun]
                if noun in EE.HappyKeyword:
                    del EE.HappyKeyword[noun]
                if noun in EE.SadKeyword:
                    del EE.SadKeyword[noun]
            i = i + 2
            
        if '������' in keyword_lst[1]:
            if '������' in EE.AngerKeyword:
                del EE.AngerKeyword['������']
            if '������' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['������']
            if '������' in EE.HappyKeyword:
                del EE.HappyKeyword['������']
            if '������' in EE.SadKeyword:
                del EE.SadKeyword['������']
            if '����' in EE.AngerKeyword:
                del EE.AngerKeyword['����']
            if '����' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['����']
            if '����' in EE.HappyKeyword:
                del EE.HappyKeyword['����']
            if '����' in EE.SadKeyword:
                del EE.SadKeyword['����']
                
        if '����' in keyword_lst[1]:
            if '����' in EE.AngerKeyword:
                del EE.AngerKeyword['����']
            if '����' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['����']
            if '����' in EE.HappyKeyword:
                del EE.HappyKeyword['����']
            if '����' in EE.SadKeyword:
                del EE.SadKeyword['����']
                
        if '����' in keyword_lst[1]:
            if '����' in EE.AngerKeyword:
                del EE.AngerKeyword['����']
            if '����' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['����']
            if '����' in EE.HappyKeyword:
                del EE.HappyKeyword['����']
            if '����' in EE.SadKeyword:
                del EE.SadKeyword['����']
        
        fst_name = keyword_lst[-2][0]
        lst_name = keyword_lst[-2][1:]
        if fst_name in EE.AngerKeyword:
            del EE.AngerKeyword[fst_name]
        if fst_name in EE.SurpriseKeyword:
            del EE.SurpriseKeyword[fst_name]
        if fst_name in EE.HappyKeyword:
            del EE.HappyKeyword[fst_name]
        if fst_name in EE.SadKeyword:
            del EE.SadKeyword[fst_name]
        if lst_name in EE.AngerKeyword:
            del EE.AngerKeyword[lst_name]
        if lst_name in EE.SurpriseKeyword:
            del EE.SurpriseKeyword[lst_name]
        if lst_name in EE.HappyKeyword:
            del EE.HappyKeyword[lst_name]
        if lst_name in EE.SadKeyword:
            del EE.SadKeyword[lst_name]
        
        if loc1 in EE.AngerKeyword:
            del EE.AngerKeyword[loc1]
        if loc1 in EE.SurpriseKeyword:
            del EE.SurpriseKeyword[loc1]
        if loc1 in EE.HappyKeyword:
            del EE.HappyKeyword[loc1]
        if loc1 in EE.SadKeyword:
            del EE.SadKeyword[loc1]
        if loc2 in EE.AngerKeyword:
            del EE.AngerKeyword[loc2]
        if loc2 in EE.SurpriseKeyword:
            del EE.SurpriseKeyword[loc2]
        if loc2 in EE.HappyKeyword:
            del EE.HappyKeyword[loc2]
        if loc2 in EE.SadKeyword:
            del EE.SadKeyword[loc2]
        
                    
        ETL.addElement(EE)
        
    emotify.addElement((loc1, loc2, ETL))
    
print(emotify.EmotifyList[157][2].EmotifyTimeList[1].AngerKeyword)