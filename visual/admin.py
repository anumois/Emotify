from django.contrib import admin
from .models import EmotifyElement, EmotifyTimeList, EmotifyDictEntry, EmotifyDictionary, EmotifyLocationList, EmotifyTweet
admin.site.register(EmotifyElement)
admin.site.register(EmotifyTimeList)
admin.site.register(EmotifyDictEntry)
admin.site.register(EmotifyDictionary)
admin.site.register(EmotifyLocationList)
admin.site.register(EmotifyTweet)

# Register your models here.
