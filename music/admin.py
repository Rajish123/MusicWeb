from django.contrib import admin
from .models import *

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name','image','slug',]
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_id','artist','album_name','album_logo','genre','release_date','slug',]
    prepopulated_fields = {"slug": ("album_name",)}
    
    
    
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['album','title','date_posted','audio',]