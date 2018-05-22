from django.db import models

# Create your models here.

class EmotifyTimeList(models.Model):
    ETLMonth = models.IntegerField(default = 0)
    ETLDay = models.IntegerField(default = 0)
    def __str__(self):
        return str(self.ETLMonth) + "월" + str(self.ETLDay) + "일"
class EmotifyLocationList(models.Model):
    ELLLocation1 = models.CharField(max_length = 50)
    ELLLocation2 = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.ELLLocation1) + " " + str(self.ELLLocation2)

class EmotifyElement(models.Model):
    EEHappy = models.IntegerField(default=0)
    EESad = models.IntegerField(default=0)
    EESurprise = models.IntegerField(default=0)
    EEAnger = models.IntegerField(default=0)

    EEDate = models.ForeignKey('EmotifyTimeList', on_delete=models.CASCADE)
    EELocation = models.ForeignKey('EmotifyLocationList', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.EELocation.ELLLocation1) + " " + str(self.EELocation.ELLLocation2) + " " + str(self.EEDate.ETLMonth) + "월" + str(self.EEDate.ETLDay) + "일"
#1: Happy, 2: Sad, 3: Surprise, 4: Anger
class EmotifyDictionary(models.Model):
    EDName = models.CharField(max_length = 50, default = 'NULL')
    EDType = models.IntegerField(default = 0)
    EDElement = models.ForeignKey('EmotifyElement', on_delete = models.CASCADE)
    def __str__(self):
        return self.EDName

class EmotifyDictEntry(models.Model):
    EDEContainer = models.ForeignKey('EmotifyDictionary', db_index=True, on_delete = models.CASCADE)
    EDEKey       = models.CharField(max_length=240, db_index=True)
    EDEValue     = models.IntegerField(default=0, db_index=True)
    def __str__(self):
        return self.EDEContainer.EDName

class EmotifyTweet(models.Model):
    ETContainer = models.ForeignKey('EmotifyDictEntry', on_delete = models.CASCADE)
    ETText = models.CharField(max_length=300, db_index=True)
    def __str__(self):
        return str(self.ETContainer)
