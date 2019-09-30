from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

