from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import views, authenticate
from django.views import generic

from .forms import SignUpForm, LoginForm
from ..animes.models import Anime


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "pages/index.html"
    redirect_field_name = ''
    model = Anime

    def get_queryset(self):
        """Return 5 last anime"""
        return Anime.objects.order_by('-released_date')[:5]


def register(req):
    if req.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(req, 'registration/register.html', {
        'form': form
    })


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    class Meta:
        fields = ['username']