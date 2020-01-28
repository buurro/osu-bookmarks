from django.db import models


class BeatmapSet(models.Model):
    osu_beatmapset_id = models.CharField(max_length=20)
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)

    @property
    def url(self):
        return "https://osu.ppy.sh/beatmapsets/" + self.osu_beatmapset_id

    def __str__(self):
        return "\"{} - {}\" by {}".format(self.artist, self.title, self.creator)


class Beatmap(models.Model):
    osu_beatmap_id = models.CharField(max_length=20)
    mode = models.CharField(max_length=1)
    version = models.CharField(max_length=100)
    beatmapset = models.ForeignKey(BeatmapSet, null=True, on_delete=models.CASCADE)

    @property
    def url(self):
        return "https://osu.ppy.sh/beatmaps/" + self.osu_beatmap_id

    def __str__(self):
        return "{} - {} [{}]".format(
            self.beatmapset.artist,
            self.beatmapset.title,
            self.version
            )


class Song(models.Model):
    osu_user_id = models.TextField(max_length=20)
    beatmapset = models.ForeignKey(BeatmapSet, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.osu_user_id, self.beatmapset)
