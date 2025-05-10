from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request,'website/home.html')

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Congrats you have been logged in!')
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials, try again!')
            return redirect('home')
    return render(request,'website/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You have logged out!!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have been registered now can log in')
            return redirect('login')
        else:
            messages.error(request, 'There were errors in the form. Please fix them and try again.')
    else:
        form=RegistrationForm()
    return render(request,'website/register.html',{
        'form' : form   
         })
