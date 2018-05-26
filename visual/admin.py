from django.contrib import admin
from .models import EmotifyElement, EmotifyTimeList, EmotifyDictEntry, EmotifyDictionary, EmotifyLocationList
from .models import HappyEmotifyTweet, SadEmotifyTweet, SurpriseEmotifyTweet, AngerEmotifyTweet
admin.site.register(EmotifyElement)
admin.site.register(EmotifyTimeList)
admin.site.register(EmotifyDictEntry)
admin.site.register(EmotifyDictionary)
admin.site.register(EmotifyLocationList)
admin.site.register(HappyEmotifyTweet)
admin.site.register(SadEmotifyTweet)
admin.site.register(SurpriseEmotifyTweet)
admin.site.register(AngerEmotifyTweet)

# Register your models here.
