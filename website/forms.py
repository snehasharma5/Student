from django import forms
from django.contrib.auth.models import User
from .models import RegisterModel
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(forms.ModelForm):
    enrollment_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'Enter '
                                                                                                     'Enrollment '
                                                                                                     'Number'}),
                                        required=True)
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Enter Name'}),
                           required=True)
    profile_pic = forms.ImageField(required=True)
    branch = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Enter Branch'}),
                             required=True)

    class Meta:
        model = RegisterModel
        fields = ['enrollment_number', 'name', 'profile_pic', 'branch']


class UpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Enter Name'}),
                           required=True)
    profile_pic = forms.ImageField(required=True)
    branch = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Enter Branch'}),
                             required=True)

    class Meta:
        model = RegisterModel
        fields = ['name', 'profile_pic', 'branch']
