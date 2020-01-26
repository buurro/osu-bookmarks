from django.urls import path
from .views import user_songs


urlpatterns = [
    path("user/<int:osu_user_id>/songs", user_songs)
]
