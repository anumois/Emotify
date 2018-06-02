class EmotifyElement:
    Happy = 0
    Sad = 0
    Surprise = 0
    Anger = 0
    HappyKeyword = {}
    SadKeyword = {}
    SurpriseKeyword = {}
    AngerKeyword = {}
    
    def __init__(self, _happy=0, _sad=0, _surprise=0, _anger=0, _haKey={}, _saKey={}, _suKey={}, _anKey={}):
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
    def __init__(self):
        self.EmotifyTimeList = []

    def addElement(self, newElem):
        self.EmotifyTimeList.append(newElem)
            
class Emotify:
    def __init__(self):
        self.EmotifyList = []
        
    def addElement(self, newElem):
        self.EmotifyList.append(newElem)
            
emotify = Emotify()
emotify.addElement(1)
print(emotify.EmotifyList)