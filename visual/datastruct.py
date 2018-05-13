class EmotifyElement:
    Happy = 0
    Sad = 0
    Surprise = 0
    Anger = 0
    HappyKeyword = {}
    SadKeyword = {}
    SurpriseKeyword = {}
    AngerKeyword = {}
    Date = 0
    def __init__(self, _happy=0, _sad=0, _surprise=0, _anger=0, _haKey={}, _saKey={}, _suKey={}, _anKey={}, _date):
        self.Happy = _happy
        self.Sad = _sad
        self.Surprise = _surprise
        self.Anger = _anger

        self.HappyKeyword = _haKey
        self.SadKeyword = _saKey
        self.SurpriseKeyword = _suKey
        self.AngerKeyword = _anKey

    def modHappy(self, _happy):
        self.Happy = _happy

    def modSad(self, _sad):
        self.Sad = _sad

    def modSurprise(self, _surprise):
        self.Surprise = _surprise

    def modAnger(self, _anger):
        self.Anger = _anger

    # mode = True : convert the value
    # mode = False : add to the value
    def addHappy(self, keyword, mode=True, value=0):
        try:
            if mode == True:
                self.HappyKeyword[keyword] = value
            else:
                self.HappyKeyword[keyword] = self.HappyKeyword[keyword] + value
        except KeyError:
            print("Error: No such Keyword")

    def addSad(self, keyword, mode=True, value=0):
        try:
            if mode == True:
                self.SadKeyword[keyword] = value
            else:
                self.SadKeyword[keyword] = self.SadKeyword[keyword] + value
        except KeyError:
            print("Error: No such Keyword")

    def addSurprise(self, keyword, mode=True, value=0):
        try:
            if mode == True:
                self.SurpriseKeyword[keyword] = value
            else:
                self.SurpriseKeyword[keyword] = self.SurpriseKeyword[keyword] + value
        except KeyError:
            print("Error: No such Keyword")

    def addAnger(self, keyword, mode=True, value=0):
        try:
            if mode == True:
                self.AngerKeyword[keyword] = value
            else:
                self.AngerKeyword[keyword] = self.AngerKeyword[keyword] + value
        except KeyError:
            print("Error: No such Keyword")

class EmotifyTimeList:
    MAX_TIME = 10

    def __init__(self):
        self.EmotifyList = []

    def addElement(self, newElem):
        if len(self.EmotifyList) < 10:
            self.EmotifyList.append(newElem)
        else:
            del self.EmotifyList[0]
            self.EmotifyList.append(newElem)
            
# 지역 코드
# 전국               0
# 서울특별시           1
# 대전광역시           2
# 대구광역시           3
# 부산광역시           4
# 인천광역시           5
# 울산광역시           6
# 세종특별자치시        7
# 경기도              8
# 강원도              9
# 충청북도            10
# 충청남도            11
# 전라북도            12
# 전라남도            13
# 경상북도            14
# 경상남도            15
# 제주특별자치도        16
class Emotify:
    EmotifyList = []
    def __init__(self):
        for i in range(16):
            ETL = EmotifyTimeList()
            EmotifyList.append(ETL)
