from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Your account is created ! You are now able to login'
            messages.success(request, msg)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html')
