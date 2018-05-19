from django.contrib import admin
from .models import EmotifyElement, EmotifyTimeList, EmotifyDictEntry, EmotifyDictionary, EmotifyLocationList
admin.site.register(EmotifyElement)
admin.site.register(EmotifyTimeList)
admin.site.register(EmotifyDictEntry)
admin.site.register(EmotifyDictionary)
admin.site.register(EmotifyLocationList)

# Register your models here.
