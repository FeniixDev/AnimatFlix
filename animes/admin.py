from django.contrib import admin

# Register your models here.
from .models import Anime, Season, Episode

admin.site.site_header = 'AnimatFlix Admin'

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'slug', 'description', 'voteAverage', 'poster']})]
    list_display = ('id', 'title', 'slug', 'updated_date', 'released_date')
    search_fields = ['title']


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'animeID', 'thumb']})]
    list_display = ('id', 'name', 'released_date', 'animeID')
    search_fields = ['name']


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['episodeID', 'title', 'description', 'seasonID', 'timeDuration',
                                    'local_path', 'thumb']})]
    list_display = ('id', 'title', 'released_date', 'anime_name')
    search_fields = ['title']
