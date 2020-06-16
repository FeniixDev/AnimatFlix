from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Anime
from .models import Season
from PIL import Image
from .models import Episode


# Create your views here.

class AllView(generic.ListView):
    template_name = "anime/all.html"
    model = Anime

    # paginate_by = 3

    def get_queryset(self):
        return Anime.objects.order_by('-released_date')


def anime_detail(req, slug):
    anime = get_object_or_404(Anime, slug=slug)
    seasons = anime.season_set.all()
    return render(req, 'anime/anime.html', {
        'anime': anime,
        'seasons': seasons,
    })


def season_detail(req, slug, id):
    try:
        anime = Anime.objects.get(slug=slug)
    except Anime.DoesNotExist:
        return redirect('allanime')
    else:
        season = get_object_or_404(Season, pk=id)
        episodes = season.episode_set.all()
        return render(req, 'anime/season.html', {
            'season': season,
            'episodes': episodes
        })
