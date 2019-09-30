from django.conf.urls import include, url
from .views import index_view, add_note, add_tag, tag_search

urlpatterns = [
	url(r'^$', index_view, name='notes.index_view'),
	url(r'^addnote/', add_note, name='notes.addnote'),
	url(r'^addtag/', add_tag, name='notes.addtag'),
	url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='notes.tagsearch'),
]