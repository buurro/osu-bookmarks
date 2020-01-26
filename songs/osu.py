import requests
import json

from urllib.parse import urlparse
from .models import BeatmapSet, Beatmap
from .settings import OSU_API_KEY


class Api:

    base_url = "https://osu.ppy.sh/api/"

    @classmethod
    def __make_request(self, endpoint="", **kwargs):
        url = self.base_url + endpoint
        data = {
            "k": OSU_API_KEY
        }
        for k in kwargs:
            data[k] = kwargs[k]
        resp = requests.get(url, params=data)
        return resp

    @classmethod
    def get_beatmap(self, beatmap_id=None, beatmapset_id=None):
        endpoint = "get_beatmaps"
        beatmap = {}
        if beatmap_id:
            resp = self.__make_request(endpoint, b=beatmap_id)
        elif beatmapset_id:
            resp = self.__make_request(endpoint, s=beatmapset_id)
        if resp and resp.status_code == 200:
            beatmaps = json.loads(resp.text)
            if beatmaps:
                beatmap = beatmaps[0]
        return beatmap

    @classmethod
    def get_user(self, user_name=None, user_id=None):
        endpoint = "get_user"
        user = {}
        if user_name:
            resp = self.__make_request(endpoint, u=user_name, type="string")
        elif user_id:
            resp = self.__make_request(endpoint, u=user_id, type="id")

        if resp and resp.status_code == 200:
            users = json.loads(resp.text)
            if users:
                user = users[0]

        return user


class Utils:

    @classmethod
    def get_beatmapset(self, url):
        beatmapset_eps = ['beatmapsets']
        beatmap_eps = ['beatmaps', 'b']

        path = urlparse(url).path
        path = path.split('/')
        if len(path) < 3:
            return None
        endpoint = path[1]
        beat_id = path[2]

        bm = None
        beatmapset = None
        beatmap = None

        if endpoint in beatmapset_eps:
            try:
                beatmapset = BeatmapSet.objects.get(osu_beatmapset_id=beat_id)
                return beatmapset
            except BeatmapSet.DoesNotExist:
                bm = Api.get_beatmap(beatmapset_id=beat_id)

        elif endpoint in beatmap_eps:
            try:
                beatmap = Beatmap.objects.get(osu_beatmap_id=beat_id)
                return beatmap.beatmapset
            except Beatmap.DoesNotExist:
                bm = Api.get_beatmap(beatmap_id=beat_id)
                try:
                    beatmapset = BeatmapSet.objects.get(
                        osu_beatmapset_id=bm["beatmapset_id"]
                    )
                except BeatmapSet.DoesNotExist:
                    pass

        else:
            return None

        if not bm:
            return None

        if not beatmapset:
            beatmapset = BeatmapSet(
                osu_beatmapset_id=bm["beatmapset_id"],
                artist=bm["artist"],
                title=bm["title"],
                creator=bm["creator"]
            )
            beatmapset.save()

        beatmap = Beatmap(
            osu_beatmap_id=bm["beatmap_id"],
            mode=bm["mode"],
            version=bm["version"],
            beatmapset=beatmapset
        )
        beatmap.save()

        return beatmapset

    @classmethod
    def get_user_id(self, user_name):
        user_info = Api.get_user(user_name=user_name)
        if not user_info:
            return None
        user_id = user_info["user_id"]
        return user_id
