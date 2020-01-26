import strawberry
from typing import Optional


@strawberry.type
class BeatmapSet:
    id: int
    osu_beatmapset_id: str
    artist: str
    title: str
    creator: str


@strawberry.type
class Song:
    id: int
    beatmapset: BeatmapSet
    osu_user_id: str
    bookmarks_url: Optional[str]
