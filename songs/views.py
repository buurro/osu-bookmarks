from .models import Song
from django.http import HttpResponse


def user_songs(request, osu_user_id):
    songs = Song.objects.filter(osu_user_id=osu_user_id)
    a_hrefs = []
    for s in songs:
        b = s.beatmapset
        a_hrefs.append('<a href="{}">{} - {}</a>'.format(
            b.url,
            b.artist,
            b.title
        ))
    out = '<br>'.join(a_hrefs)
    return HttpResponse(out)
