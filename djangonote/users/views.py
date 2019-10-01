from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import user_passes_test
from django import forms

def register_view(request):
    context={}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Your account is created ! You are now able to login'
            messages.success(request, msg)
            return redirect(request, 'login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context)