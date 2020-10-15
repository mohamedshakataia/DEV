from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import post
from .forms import postform
# Create your views here.


class All_List(ListView):
    model=post

class detail(DetailView):
    model=post