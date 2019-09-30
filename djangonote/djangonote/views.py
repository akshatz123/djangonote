from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


def home_view(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		auth = authenticate(username=username, password=password)
		if auth is not None:
			login(request, auth)
			return HttpResponseRedirect('notes/')
		else:
			messages.add_message(request, messages.INFO, "Authentication Failed!")
			return HttpResponseRedirect('home')

	return render(request, 'home.html')


def logout_view(request):
	return render(request, 'home.html')


def register(request):
	return  render(request, 'users/templates/register')
