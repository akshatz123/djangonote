from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views
from djangonote.views import *
from notes.views import *
from djangonote import settings
from djangonote.views import home_view
from notes.views import search
from .views import *

urlpatterns = [
    url(r'^$', home_view, name = 'login'),
    path('logout/', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register/', register_view, name='register'),
    # path('notes/', include('notes.urls'), name='notes'),
    path('search/', search, name='search'),
]