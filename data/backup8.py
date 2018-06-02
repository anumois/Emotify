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