import strawberry

from typing import Optional, List
from django.urls import reverse
from .models import Song
from .types import Song as SongType
from .osu import Utils as OsuUtils
from .views import user_songs


@strawberry.type
class SongQuery:
    @strawberry.field
    def song(self, info, id: int) -> Optional[SongType]:
        return Song.objects.get(id=id)

    @strawberry.field
    def songs(self, info) -> List[SongType]:
        return Song.objects.all()

    @strawberry.field
    def user_songs(self, info, osu_user_id: str) -> List[SongType]:
        return Song.objects.filter(osu_user_id=osu_user_id)


@strawberry.input
class SongInput:
    map_url: str
    user_name: str


@strawberry.type
class SongMutation:
    @strawberry.mutation
    def addSong(self, info, input: SongInput) -> Optional[SongType]:
        beatmapset = OsuUtils.get_beatmapset(input.map_url)
        user_id = OsuUtils.get_user_id(input.user_name)

        if not (beatmapset and user_id):
            return None

        try:
            song = Song.objects.get(osu_user_id=user_id, beatmapset=beatmapset)
        except Song.DoesNotExist:
            song = Song(osu_user_id=user_id, beatmapset=beatmapset)
            song.save()

        # I don't know how to do this decently
        song.bookmarks_url = reverse(user_songs, args=[song.osu_user_id])

        return song
