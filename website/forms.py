from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

# create forms here

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=100,label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    username = forms.CharField(
        max_length=150,label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class NewRecordForm(forms.ModelForm):
    first_name=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First name'
    }))
    last_name=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last name'
    }))
    email=forms.CharField(max_length=50,label='',widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email'
    }))
    phone=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Phone'
    }))
    address=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Address'
    }))
    city=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'City'
    }))
    state=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'State'
    }))
    zipcode=forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Zipcode'
    }))
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','state','zipcode']