from django.shortcuts import render,redirect
from .forms import signupform
from django.contrib.auth import authenticate ,login
from django.urls import reverse
from .models import profile
# Create your views here.


def signup(request):
    if request.method =='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
        
            username = form.cleaned_data['username']     ### update session
            password = form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts/profile')) 
       
        
    else:
        form=signupform()

    return render(request,'registration/signup.html',{'form':form})



def profiles(request):
    profiler= profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profiler':profiler})