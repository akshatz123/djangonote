from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Note, Tag
from .forms import NoteForm, TagForm
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView


def superuser_only(user):
    u = user.is_authenticated
    return u


@user_passes_test(superuser_only, login_url="/")
def index_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    # notes = Note.objects.filter(user=request.user.id)
    tags = Tag.objects.all()
    # user = Note.objects.filter(user=request.user).values()
    context = {
        'notes': notes,
        'tags': tags,
        # 'user': user,
    }
    return render(request, 'notes/index.html', context)


@user_passes_test(superuser_only, login_url="/")
def add_note(request):

    id = request.GET.get('id', None)

    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Note Deleted!')
            return HttpResponseRedirect(reverse('notes.index_view'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            f = form.save()
            f.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes.index_view'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form':form, 'note':note})


@user_passes_test(superuser_only, login_url="/")
def add_tag(request):

    id = request.GET.get('id', None)

    if id is not None:
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag Deleted!')
            return HttpResponseRedirect('notes.index_view')

        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Tag Added!')
            return HttpResponseRedirect('notes.index')
    else:
        form = TagForm(instance=tag)

    return render(request, 'notes/addtag.html', {'form': form, 'tag': tag})


@user_passes_test(superuser_only, login_url="/")
def tag_search(request, **kwargs):
    slug = kwargs['slug']
    tags = get_object_or_404(Tag, slug=slug)
    notes = tags.notes.all()
    context = {
        'notes': notes,
        'tags': tags
    }
    return render(request, 'notes/tagsearch.html', context)

#
# class search_results(ListView):
#     model = Note
#     template_name = 'search.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return Note.objects.filter(body__startswith=query)


@user_passes_test(superuser_only, login_url="/")
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        # print (query)
        submitbutton = request.GET.get('submit', None)
        # print(submitbutton)
        if query is not None:
            lookups = Q(label__icontains=query)
            # print (lookups)
            results = Tag.objects.filter(lookups)
            # print(results)

            return render(request, 'search.html', {'results': results, 'submitbutton': submitbutton})

        else:
            return render(request, 'base.html')

    else:
        return render(request, 'search.html')
# results =Note.objects.all()
# body = results.GET.get('body', None)
# if body:
#     results = results.objects.filter(body__contains=body)