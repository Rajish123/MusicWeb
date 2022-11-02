from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('artist/',views.artist, name = 'artist'),
    path('album/',views.album, name = 'album'),
    # get album of artist
    path('<int:id>/<slug:slug>/', views.ArtistAlbums, name = 'artist_album'),
    # get all songs of selected album, requires album_id and album slug
    path('albumsong/<int:album_id>/<slug:slug>/', views.AlbumSongs, name = 'album_song'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

