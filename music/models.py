from enum import unique
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Artist(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = "artist_picture")
    name = models.CharField(max_length=25, verbose_name = "Artists or Band name")
    slug = models.SlugField(max_length = 200, null = False)
    
    class Meta:
        ordering = ('name',)
        # creates an index for the name field, will be useful for lookups based on name
        indexes = [
            models.Index(fields = ['name',]),
            models.Index(fields = ['slug',]),
            
        ]
        verbose_name = 'Artist'
        verbose_name_plural = "Artists"
        
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("artist_album", kwargs={"id":self.id, "slug": self.slug})
        
    @staticmethod
    def get_all_artists():
        return Artist.objects.all()

    def __str__(self):
        return self.name
    

class Album(models.Model):
    album_id = models.AutoField(primary_key=True,verbose_name = "id")
    # related_name attribute specifies the name of the reverse relation
    # eg:Aritst_instance.albums.all()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name = 'albums',verbose_name = "band")
    album_name = models.CharField(max_length=100,verbose_name = "name")
    album_logo = models.ImageField(default = 'album_logo.jpg', upload_to = "album_logo_picture",verbose_name = "image")
    release_date = models.DateTimeField(default=timezone.now,verbose_name = "released_date")
    genre = models.CharField(max_length=50,verbose_name = "genre")
    producer = models.CharField(max_length=100,verbose_name = "producer")
    description = models.TextField(max_length = 250,null=True, blank=True,verbose_name = "description")
    date_posted = models.DateTimeField(default=timezone.now,verbose_name = "posted_date")
    votes = models.IntegerField(default = 0,verbose_name = "votes")
    slug = models.SlugField(max_length = 200, null = False)
    
    
    class Meta:
        ordering = ('-album_id',)
        # creates an index for the name field, will be useful for lookups based on name as well as slug
        indexes = [
            models.Index(fields = ['album_id',]),
            models.Index(fields = ['slug',]),
            
        ]
        verbose_name = 'Album'
        verbose_name_plural = "Albums"
        
    def save(self,*args,**kwargs):
        self.slug = slugify(self.album_name)
        super(Album, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.album_name
    
    def get_absolute_url(self):
        return reverse("album_song", kwargs={"album_id":self.album_id, "slug": self.slug})
    
    @staticmethod
    def get_all_album():
        return Album.objects.all()

    

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name = "songs", verbose_name = 'related_album')
    title = models.CharField(max_length=100, verbose_name = 'title')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name = 'date')
    audio = models.FileField(upload_to = "mp3", verbose_name = 'song')
    votes = models.IntegerField(default = 0,verbose_name = "votes")
    

    class Meta:
        ordering = ('-id',)
        # creates an index for the name field, will be useful for lookups based on name
        indexes = [
            models.Index(fields = ['id',]),
        ]
        verbose_name = 'Song'
        verbose_name_plural = "Songs"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("songs", kwargs={"id":self.id, })
 
    @staticmethod
    def get_all_songs():
        return Song.objects.all()


class MyPlaylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.CharField(max_length=100000,default="")

    def __str__(self):
        return f"{self.user.profile}-->playlist"







