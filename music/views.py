from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def home(request):
    context = {}
    albums = Album.get_all_album().order_by("-votes")[:4]
    context = {'albums':albums}
    return render(request,'music/home.html',context)

def artist(request):
    context = {}
    artists = Artist.get_all_artists()
    context = {'artists':artists}
    return render(request,'music/artist.html',context)

def album(request):
    context = {}
    albums= Album.get_all_album()
    context = {'albums':albums}
    return render(request, 'music/album.html',context)

# get all albums of the selected artist
def ArtistAlbums(request,id,slug):
    context = {}
    artists = get_object_or_404(
        Artist,
        id = id,
        slug = slug
    )
    album = artists.albums.all().order_by('-votes')
    context = {'artists':artists, 'albums':album}
    return render(request,'music/artist_albums.html',context)

# get all songs of album
def AlbumSongs(request,album_id,slug):
    context = {}
    albums = get_object_or_404(
        Album,
        album_id = album_id,
        slug = slug
    )
    songs = albums.songs.all().order_by('-date_posted')
    print(albums)
    context = {'albums':albums, 'songs':songs}
    return render(request,'music/album_songs.html',context)
    
def Songs(request,id):
    context = {}
    song = get_object_or_404(Song,id=id)
    context = {'song':song}
    return render(request,'music/songs.html',context)
    
def AllSongs(request):
    context = {}
    songs = Song.objects.all()
    context = {'songs':songs}
    return render(request,'music/songs_list.html',context)