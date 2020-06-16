from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AllView.as_view(), name="allanime"),
    path('<slug:slug>/', views.anime_detail, name="anime-detail"),
    path('<slug:slug>/<int:id>', views.season_detail, name="season_detail")
]