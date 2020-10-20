from django.shortcuts import render ,redirect
from django.views.generic import ListView ,DetailView,CreateView, UpdateView ,DeleteView
from .models import post
from .forms import postform
# Create your views here.


class All_List(ListView):
    model=post

class detail(DetailView):
    model=post

class NewPost(CreateView):
    model=post
    template_name='blog/new_post.html'
    fields='__all__'
    success_url='/blog/cbv/'

class Edit(UpdateView):
    model=post
    fields='__all__'
    success_url='/blog/cbv/'


class Delete(DeleteView):
    model=post
    success_url='/blog/cbv/'





