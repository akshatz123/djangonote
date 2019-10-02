from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views
from djangonote.views import home_view
from .views import *
from djangonote import settings

urlpatterns = [
    url(r'^$', home_view, name = 'login'),
    path('logout/', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register/', register_view, name='register'),
    path('notes/', include('notes.urls'), name='notes'),
]