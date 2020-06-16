from django.urls import path, include
from . import views
from .views import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', include('django.contrib.auth.urls')),
]