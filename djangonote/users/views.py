from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages

from notes.models import *

from notes.views import *
from .forms import UserRegisterForm


def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Your account is created ! You are now able to login'
            messages.success(request, msg)
            return redirect("/")
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


# @user_passes_test(superuser_only, login_url="/")
# def search(request):
#     if request.method == 'GET':
#         query = request.GET.get('q')
#         submitbutton= request.GET.get('submit', None)
#         if query:
#             lookups= Q(body__contains=query)
#             results= Note.objects.filter(lookups).distinct()
#
#             return render(request, 'search.html',context={'results': results, 'submitbutton': submitbutton})
#
#         else:
#             return render(request, 'search.html')
#
#     else:
#         return render(request, 'search.html')
