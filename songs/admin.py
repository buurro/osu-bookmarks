from django.contrib import admin
from .models import Song, BeatmapSet, Beatmap


admin.site.register(Song)
admin.site.register(BeatmapSet)
admin.site.register(Beatmap)
