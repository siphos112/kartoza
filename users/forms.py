from enum import unique
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from phonenumber_field.modelfields import PhoneNumberField


class UserForm(UserCreationForm):
	'''
	Form that uses built-in UserCreationForm to handle user creation
	'''
	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	#reCAPTCHA token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )



class AuthForm(AuthenticationForm):
	'''
	Form that uses built-in AuthenticationForm to handel user auth
	'''
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )




class UserProfileForm(forms.ModelForm):
	'''
	Basic model-form for our user profile that extends Django user model.
	
	'''
	telephone_number = PhoneNumberField(unique=True, null=False, blank=True, widget = forms.TextInput)
	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	complex_building = forms.CharField(max_length=100, required=False, widget = forms.HiddenInput())
	suburb = forms.CharField(max_length=100, required=False, widget = forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	province = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('telephone_number', 'address', 'complex_building', 'suburb', 
		'town', 'province', 'post_code', 'country', 'longitude', 'latitude')
