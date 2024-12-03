from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control', 'data-toggle':'password', 'id':'password'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form-control', 'data-toggle':'password', 'id':'password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Enter Old Password', 'class':'form-control', 'data-toggle':'password', 'id':'password'}))
    new_password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Enter New Password', 'class':'form-control', 'data-toggle':'password', 'id':'new_password'}))
    new_password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm New Password', 'class':'form-control', 'data-toggle':'password', 'id':'confirm_new_password'}))


    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')


