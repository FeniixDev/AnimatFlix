from django.db import models


# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    voteAverage = models.FloatField(default=0)
    poster = models.ImageField(upload_to='animes')
    slug = models.SlugField()
    released_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    name = models.CharField(max_length=64)
    released_date = models.DateTimeField(auto_now_add=True)
    animeID = models.ForeignKey(Anime, on_delete=models.CASCADE)
    thumb = models.ImageField(upload_to='seasons')

    def __str__(self):
        return self.name


class Episode(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    timeDuration = models.TimeField()
    seasonID = models.ForeignKey(Season, on_delete=models.CASCADE)
    episodeID = models.IntegerField()
    local_path = models.TextField()
    thumb = models.ImageField(upload_to='episodes')
    released_date = models.DateTimeField(auto_now_add=True)

    def anime_name(self):
        return self.seasonID.animeID.title + ' (' + self.seasonID.name + ')'
