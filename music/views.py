from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib import messages
from django.db.models import Case,When


def home(request):
    context = {}
    albums = Album.get_all_album().order_by("-votes")[:4]
    songs = Song.get_all_songs().order_by("-votes")[:4]
    context = {'albums':albums, 'songs':songs}
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

def addsong(request,user,songid):
    my_playlist = MyPlaylist(user=user,song_id=songid)
    my_playlist.save()
    messages.success(request,"Successfully added to playlist")
    

def AddToPlaylist(request):
    if request.method == "POST":
        songid = request.POST['song_id']
        user = request.user
        print(songid)
        my_playlist = MyPlaylist.objects.filter(user = request.user)
        print(my_playlist.exists())
        if my_playlist.exists():
            for i in my_playlist:
                if songid == i.song_id:
                    messages.info(request,"This song is already in your playlist")
                    break
                else:
                    addsong(request,user,songid)
        else:
            addsong(request,user,songid)
        return redirect('myplaylist')
    
def my_playlist(request):
    my_playlist = MyPlaylist.objects.filter(user = request.user)   
    print(my_playlist)     
    ids = []
    for i in my_playlist:
        ids.append(i.song_id)
    # display ablum according to the time when added
    preserved = Case(*[When(pk = pk, then = pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(id__in = ids).order_by(preserved)
    print(f"songs:{song}")
    return render(request, 'music/myplaylist.html',{'playlist':my_playlist,'songs':song})