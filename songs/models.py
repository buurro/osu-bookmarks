from django.db import models


class BeatmapSet(models.Model):
    osu_beatmapset_id = models.CharField(max_length=20)
    artist = models.TextField()
    title = models.TextField()
    creator = models.TextField()

    @property
    def url(self):
        return "https://osu.ppy.sh/beatmapsets/" + self.osu_beatmapset_id


class Beatmap(models.Model):
    osu_beatmap_id = models.CharField(max_length=20)
    mode = models.CharField(max_length=1)
    version = models.TextField()
    beatmapset = models.ForeignKey(BeatmapSet, null=True, on_delete=models.CASCADE)

    @property
    def url(self):
        return "https://osu.ppy.sh/beatmaps/" + self.osu_beatmap_id


class Song(models.Model):
    osu_user_id = models.TextField(max_length=20)
    beatmapset = models.ForeignKey(BeatmapSet, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
