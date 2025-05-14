from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,NewRecordForm
from .models import Record
# Create your views here.

def home(request):
    records=Record.objects.all()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Congrats you have been logged in!')
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials, try again!')
            return redirect('home')
    return render(request,'website/home.html',{
        "records" : records
    })

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
            return redirect('home')
        else:
            messages.error(request, 'There were errors in the form. Please fix them and try again.')
    else:
        form=RegistrationForm()
    return render(request,'website/register.html',{
        'form' : form   
         })

@login_required
def add_record(request):
    if request.method == 'POST':
        form=NewRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New record has been added')
            return redirect('home')
        else:
            messages.error(request,'There were errors in the form. Please fix them and try again.')
    else:
        form=NewRecordForm()
    return render(request,'website/add_record.html',{
        "form" : form
    })

@login_required
def customer_record(request,pk):
        customer_record=Record.objects.get(id=pk)
        return render(request,'website/customer_record.html',{
        'customer_record' : customer_record
        })

@login_required
def delete_record(request, pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()  
    messages.success(request, 'Record has been deleted.')
    return redirect('home')


@login_required
def update_record(request,pk):
    current_record=Record.objects.get(id=pk)
    if request.method == 'POST':
        form=NewRecordForm(request.POST or None , instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record has been Updated')
            return redirect('home')
        else:
            messages.error(request,'There were errors in the form. Please fix them and try again.')
    else:
        form=NewRecordForm(instance=current_record)
    return render(request,'website/update_record.html',{
        "form" : form
    })
