# -*- coding: utf-8 -*-

Kangwon = ['강원', '도지사', '강릉', '고성', '동해', '삼척', '속초', '양구', '양양', '영월', '원주', '인제', '정선', '철원', '춘천', '태백', '평창', '홍천', '화천', '횡성']
Kyunggi = ['경기', '도지사', '가평', '고양', '과천', '광명', '광주', '구리', '군포', '김포', '남양주', '동두천', '부천', '성남', '수원', '시흥', '안산', '안성', '안양', '양주', '양평', '여주', '연천', '오산', '용인', '의왕', '의정부', '이천', '파주', '평택', '포천', '하남', '화성']
Kyungnam = ['경남','도지사', '거제', '거창', '고성', '김해', '남해', '밀양', '사천', '산청', '양산', '의령', '진주', '창녕', '창원', '통영', '하동', '함안', '함양', '합천']
Kyungbuk = ['경북', '도지사', '경산', '경주', '고령', '구미', '군위', '김천', '문경', '봉화', '상주', '성주', '안동', '영덕', '영양', '영주', '영천', '예천', '울릉', '울진', '의성', '청도', '청도', '청송', '칠곡', '포항']
Jeonnam = ['전남', '도지사', '강진', '고흥', '곡성', '광양', '구례', '나주', '담양', '목포', '무안', '보성', '순천', '신안', '여수', '영광', '영암', '완도', '장성', '장흥', '진도', '함평', '해남', '화순']
Jeonbuk = ['전북','도지사', '고창', '군산', '김제', '남원', '무주', '부안', '순창', '완주', '익산', '임실', '장수', '전주', '정읍', '진안']
Chungnam = ['충남', '도지사', '계룡', '공주', '금산', '논산', '당진', '보령', '부여', '서산', '서천', '아산', '예산', '천안', '청양', '태안', '홍성']
Chungbuk = ['충북', '도지사', '괴산', '단양', '보은', '영동', '옥천', '음성', '제천', '증평', '진천', '청주', '충주']
Jeju = ['제주', '특별자치도지사']
Kwangju = ['광주', '광역시장']
Daegu = ['대구', '광역시장', '달성']
Daejeon = ['대전','광역시장']
Busan = ['부산','광역시장', '기장']
Seoul = ['서울','특별시장']
Ulsan = ['울산', '광역시장', '울주']
Incheon = ['인천', '광역시장', '강화', '옹진']
Sejong = ['세종', '특별자치시장']

LocationList = [Kangwon, Kyunggi, Kyungnam, Kyungbuk, Jeonnam, Jeonbuk, Chungnam, Chungbuk, Jeju, Kwangju, Daegu, Daejeon, Busan, Seoul, Ulsan, Incheon, Sejong]
dbDate = [[(4, 16)],
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
              [(5, 22)],
              [(5, 23)],
              [(5, 24)],
              [(5, 25)],
              [(5, 26)],
              [(5, 27)],
              [(5, 28)],
              [(5, 29)],
              ]

import datetime
import operator
from visual.models import EmotifyElement, EmotifyTimeList, EmotifyDictEntry, EmotifyDictionary, EmotifyLocationList
from visual.models import HappyEmotifyTweet, SadEmotifyTweet, SurpriseEmotifyTweet, AngerEmotifyTweet
from django.core.exceptions import ObjectDoesNotExist
from konlpy.tag import Twitter
twitter = Twitter()

class cEmotifyElement:
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

class cEmotifyTimeList:
    def __init__(self):
        self.arrEmotifyTimeList = []

    def addElement(self, newElem):
        self.arrEmotifyTimeList.append(newElem)

class cEmotify:
    def __init__(self):
        self.EmotifyList = []

    def addElement(self, newElem):
        self.EmotifyList.append(newElem)

pronouns = ['그놈', '그녀', '그년', '그것', '우리', '너희', '그들', '님들']

f = open("data/politician.txt", "r", -1, "utf-8")
keywords = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    keywords.append(line)
f.close()

emotify = cEmotify()

for keyword in keywords:
    ETL = cEmotifyTimeList()
    anger_tweets = {}
    fear_tweets = {}
    happy_tweets = {}
    sad_tweets = {}

    keyword_lst = keyword.split('"')
    lst_name = keyword_lst[-2][1:]

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
                  [(5, 22)],
                  [(5, 23)],
                  [(5, 24)],
                  [(5, 25)],
                  [(5, 26)],
                  [(5, 27)],
                  [(5, 28)],
                  [(5, 29)],
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
                  [(5, 22)],
                  [(5, 23)],
                  [(5, 24)],
                  [(5, 25)],
                  [(5, 26)],
                  [(5, 27)],
                  [(5, 28)],
                  [(5, 29)],
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
                  [(5, 22)],
                  [(5, 23)],
                  [(5, 24)],
                  [(5, 25)],
                  [(5, 26)],
                  [(5, 27)],
                  [(5, 28)],
                  [(5, 29)],
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
                  [(5, 22)],
                  [(5, 23)],
                  [(5, 24)],
                  [(5, 25)],
                  [(5, 26)],
                  [(5, 27)],
                  [(5, 28)],
                  [(5, 29)],
                  ]

    name = keyword.split('"')[1]

    loc1 = ''
    loc2 = ''

    if '대통령' in name:
        loc1 = '전국'
        loc2 = '대통령'
    else:
        for Loc1 in LocationList:
            if Loc1[0] in name:
                for Loc2 in Loc1[1:]:
                    if Loc2 in name:
                        loc1 = Loc1[0]
                        loc2 = Loc2
                        break
                break

    name_anger = "data/" + name + "_anger.txt"
    name_fear = "data/" + name + "_fear.txt"
    name_happy = "data/" + name + "_happy.txt"
    name_sad = "data/" + name + "_sad.txt"

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
        EE = cEmotifyElement()
        day = anger_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modAnger(EE.Anger + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    if len(word) > 1:
                        count = EE.AngerKeyword.get(word, 0)
                        EE.addAnger(word, count + n_tweets)
                        lst = anger_tweets.get(word, [])
                        if len(lst) < 5:
                            if lst_name in text:
                                if not text in lst:
                                    lst.append(text)
                        anger_tweets[word] = lst

        day = fear_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modSurprise(EE.Surprise + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    if len(word) > 1:
                        count = EE.SurpriseKeyword.get(word, 0)
                        EE.addSurprise(word, count + n_tweets)
                        lst = fear_tweets.get(word, [])
                        if len(lst) < 5:
                            if lst_name in text:
                                if not text in lst:
                                    lst.append(text)
                        fear_tweets[word] = lst

        day = happy_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modHappy(EE.Happy + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    if len(word) > 1:
                        count = EE.HappyKeyword.get(word, 0)
                        EE.addHappy(word, count + n_tweets)
                        lst = happy_tweets.get(word, [])
                        if len(lst) < 5:
                            if lst_name in text:
                                if not text in lst:
                                    lst.append(text)
                        happy_tweets[word] = lst

        day = sad_date[i]
        lines = day[1:]
        if len(lines) > 0:
            for line in lines:
                n_tweets = 1 + int(line[1])
                EE.modSad(EE.Sad + n_tweets)
                text = line[0]
                words = twitter.nouns(text)
                for word in words:
                    if len(word) > 1:
                        count = EE.SadKeyword.get(word, 0)
                        EE.addSad(word, count + n_tweets)
                        lst = sad_tweets.get(word, [])
                        if len(lst) < 5:
                            if lst_name in text:
                                if not text in lst:
                                    lst.append(text)
                        sad_tweets[word] = lst

        for pronoun in pronouns:
            if pronoun in EE.AngerKeyword:
                del EE.AngerKeyword[pronoun]
            if pronoun in EE.SurpriseKeyword:
                del EE.SurpriseKeyword[pronoun]
            if pronoun in EE.HappyKeyword:
                del EE.HappyKeyword[pronoun]
            if pronoun in EE.SadKeyword:
                del EE.SadKeyword[pronoun]


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

        if '도지사' in keyword_lst[1]:
            if '도지사' in EE.AngerKeyword:
                del EE.AngerKeyword['도지사']
            if '도지사' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['도지사']
            if '도지사' in EE.HappyKeyword:
                del EE.HappyKeyword['도지사']
            if '도지사' in EE.SadKeyword:
                del EE.SadKeyword['도지사']
            if '지사' in EE.AngerKeyword:
                del EE.AngerKeyword['지사']
            if '지사' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['지사']
            if '지사' in EE.HappyKeyword:
                del EE.HappyKeyword['지사']
            if '지사' in EE.SadKeyword:
                del EE.SadKeyword['지사']

        if '시장' in keyword_lst[1]:
            if '시장' in EE.AngerKeyword:
                del EE.AngerKeyword['시장']
            if '시장' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['시장']
            if '시장' in EE.HappyKeyword:
                del EE.HappyKeyword['시장']
            if '시장' in EE.SadKeyword:
                del EE.SadKeyword['시장']

        if '군수' in keyword_lst[1]:
            if '군수' in EE.AngerKeyword:
                del EE.AngerKeyword['군수']
            if '군수' in EE.SurpriseKeyword:
                del EE.SurpriseKeyword['군수']
            if '군수' in EE.HappyKeyword:
                del EE.HappyKeyword['군수']
            if '군수' in EE.SadKeyword:
                del EE.SadKeyword['군수']

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

    for pronoun in pronouns:
        if pronoun in anger_tweets:
            del anger_tweets[pronoun]
        if pronoun in fear_tweets:
            del fear_tweets[pronoun]
        if pronoun in happy_tweets:
            del happy_tweets[pronoun]
        if pronoun in sad_tweets:
            del sad_tweets[pronoun]

    i = 1
    while len(keyword_lst) > i:
        nouns = twitter.nouns(keyword_lst[i])
        for noun in nouns:
            if noun in anger_tweets:
                del anger_tweets[noun]
            if noun in fear_tweets:
                del fear_tweets[noun]
            if noun in happy_tweets:
                del happy_tweets[noun]
            if noun in sad_tweets:
                del sad_tweets[noun]
        i = i + 2

    if '도지사' in keyword_lst[1]:
        if '도지사' in anger_tweets:
            del anger_tweets['도지사']
        if '도지사' in fear_tweets:
            del fear_tweets['도지사']
        if '도지사' in happy_tweets:
            del happy_tweets['도지사']
        if '도지사' in sad_tweets:
            del sad_tweets['도지사']
        if '지사' in anger_tweets:
            del anger_tweets['지사']
        if '지사' in fear_tweets:
            del fear_tweets['지사']
        if '지사' in happy_tweets:
            del happy_tweets['지사']
        if '지사' in sad_tweets:
            del sad_tweets['지사']

    if '시장' in keyword_lst[1]:
        if '시장' in anger_tweets:
            del anger_tweets['시장']
        if '시장' in fear_tweets:
            del fear_tweets['시장']
        if '시장' in happy_tweets:
            del happy_tweets['시장']
        if '시장' in sad_tweets:
            del sad_tweets['시장']

    if '군수' in keyword_lst[1]:
        if '군수' in anger_tweets:
            del anger_tweets['군수']
        if '군수' in fear_tweets:
            del fear_tweets['군수']
        if '군수' in happy_tweets:
            del happy_tweets['군수']
        if '군수' in sad_tweets:
            del sad_tweets['군수']

    if lst_name in anger_tweets:
        del anger_tweets[lst_name]
    if lst_name in fear_tweets:
        del fear_tweets[lst_name]
    if lst_name in happy_tweets:
        del happy_tweets[lst_name]
    if lst_name in sad_tweets:
        del sad_tweets[lst_name]

    if loc1 in anger_tweets:
        del anger_tweets[loc1]
    if loc1 in fear_tweets:
        del fear_tweets[loc1]
    if loc1 in happy_tweets:
        del happy_tweets[loc1]
    if loc1 in sad_tweets:
        del sad_tweets[loc1]
    if loc2 in anger_tweets:
        del anger_tweets[loc2]
    if loc2 in fear_tweets:
        del fear_tweets[loc2]
    if loc2 in happy_tweets:
        del happy_tweets[loc2]
    if loc2 in sad_tweets:
        del sad_tweets[loc2]

    emotify.addElement((loc1, loc2, ETL, anger_tweets, fear_tweets, happy_tweets, sad_tweets))
print('Finished Emotify DS')


for date in dbDate:
    print(date)
    try:
        ETL = EmotifyTimeList.objects.get(ETLMonth = date[0][0], ETLDay = date[0][1])
    except ObjectDoesNotExist:
        ETL = EmotifyTimeList(ETLMonth = date[0][0], ETLDay = date[0][1])
        ETL.save()

print('Finished ETL')

for ETL in emotify.EmotifyList:
    try:
        ELL = EmotifyLocationList.objects.get(ELLLocation1 = ETL[0], ELLLocation2 = ETL[1])
    except ObjectDoesNotExist:
        ELL = EmotifyLocationList(ELLLocation1 = ETL[0], ELLLocation2 = ETL[1])
        ELL.save()

print('Finished ELL')

for Element in emotify.EmotifyList:
    try:
        ELL = EmotifyLocationList.objects.get(ELLLocation1 = Element[0], ELLLocation2 = Element[1])
    except ObjectDoesNotExist:
        print('no such ELL')
        continue

    for tweetKey in Element[3].keys():
        for tweet in Element[3][tweetKey]:
            ET = HappyEmotifyTweet(ETContainer = ELL, ETKey = tweetKey, ETText = tweet)
            ET.save()
    for tweetKey in Element[4].keys():
        for tweet in Element[4][tweetKey]:
            ET = SadEmotifyTweet(ETContainer = ELL, ETKey = tweetKey, ETText = tweet)
            ET.save()
    for tweetKey in Element[5].keys():
        for tweet in Element[5][tweetKey]:
            ET = SurpriseEmotifyTweet(ETContainer = ELL, ETKey = tweetKey, ETText = tweet)
            ET.save()
    for tweetKey in Element[6].keys():
        for tweet in Element[6][tweetKey]:
            ET = AngerEmotifyTweet(ETContainer = ELL, ETKey = tweetKey, ETText = tweet)
            ET.save()

    iteration = 0
    for eE in Element[2].arrEmotifyTimeList:
        try:
            ETL = EmotifyTimeList.objects.get(ETLMonth = dbDate[iteration][0][0], ETLDay = dbDate[iteration][0][1])
        except ObjectDoesNotExist:
            print('no such ETL')
            iteration = iteration + 1
            continue
        EE = EmotifyElement(EEHappy = eE.Happy, EESad = eE.Sad, EESurprise = eE.Surprise, EEAnger = eE.Anger, EEDate = ETL, EELocation = ELL)
        EE.save()

        HaDict = EmotifyDictionary(EDName = (Element[0] + Element[1]) + 'Happy',EDType = 1, EDElement = EE)
        SaDict = EmotifyDictionary(EDName = (Element[0] + Element[1]) + 'Sad',EDType = 2, EDElement = EE)
        SuDict = EmotifyDictionary(EDName = (Element[0] + Element[1]) + 'Surprise',EDType = 3, EDElement = EE)
        AnDict = EmotifyDictionary(EDName = (Element[0] + Element[1]) + 'Angry',EDType = 4, EDElement = EE)
        
        HaDict.save()
        SaDict.save()
        SuDict.save()
        AnDict.save()
        
        sorted_HaKeyword = sorted(eE.HappyKeyword.items(), key=operator.itemgetter(1), reverse = True)
        sorted_SaKeyword = sorted(eE.SadKeyword.items(), key=operator.itemgetter(1), reverse = True)
        sorted_SuKeyword = sorted(eE.SurpriseKeyword.items(), key=operator.itemgetter(1), reverse = True)
        sorted_AnKeyword = sorted(eE.AngerKeyword.items(), key=operator.itemgetter(1), reverse = True)
        for i in range(15):
            if len(sorted_HaKeyword) > i:
                newHaDictVal = EmotifyDictEntry(EDEKey = sorted_HaKeyword[i][0], EDEValue = sorted_HaKeyword[i][1], EDEContainer = HaDict)
                newHaDictVal.save()
            if len(sorted_SaKeyword) > i:
                newSaDictVal = EmotifyDictEntry(EDEKey = sorted_SaKeyword[i][0], EDEValue = sorted_SaKeyword[i][1], EDEContainer = SaDict)
                newSaDictVal.save()
            if len(sorted_SuKeyword) > i:
                newSuDictVal = EmotifyDictEntry(EDEKey = sorted_SuKeyword[i][0], EDEValue = sorted_SuKeyword[i][1], EDEContainer = SuDict)
                newSuDictVal.save()
            if len(sorted_AnKeyword) > i:
                newAnDictVal = EmotifyDictEntry(EDEKey = sorted_AnKeyword[i][0], EDEValue = sorted_AnKeyword[i][1], EDEContainer = AnDict)
                newAnDictVal.save() 
            
        iteration = iteration + 1
