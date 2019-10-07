from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
	path('', index_view, name='notes.index_view'),
	path('addnote/', add_note, name='notes.addnote'),
	path('addtag/', add_tag, name='notes.addtag'),
	url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='notes.tagsearch'),
	path('search/', search, name='notes.search_results'),
]