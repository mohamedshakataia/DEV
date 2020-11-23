from django.urls import path
from .views import signup,profiles

app_name='accounts'


urlpatterns = [
    path('signup/',signup,name='signup'),
    path('profile/',profiles,name='profile'),
]