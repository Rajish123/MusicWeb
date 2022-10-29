from django.shortcuts import render
from .models import *


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
