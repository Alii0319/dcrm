from django.shortcuts import render

# Create your views here.
def home(request,name):
    return render(request,'website/index.html',{
        "name"  : name.capitalize()
    })