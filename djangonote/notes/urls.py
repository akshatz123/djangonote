from django.conf.urls import include, url
from django.contrib import admin
from notes.views import index, addnote, addtag, tagsearch

urlpatterns = [
	url(r'^$', index, name='notes.index'),
	url(r'^addnote/', addnote, name='notes.addnote'),
	url(r'^addtag/', addtag, name='notes.addtag'),
	url(r'^tags/(?P<slug>[-\w]+)/$', tagsearch, name='notes.tagsearch'),
]