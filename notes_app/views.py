from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
# to import module of user 
from django.contrib.auth.models import User

# Create your views here.

# show all notes
def all_notes(request):
    pass
    # return HttpResponse('<h1> this  section retrive all notes </h1>')
    all_notes = Note.objects.all()
    context={
        # allNotes return to used in form(ui)
       'allNotes' : all_notes 
    }
    return render(request, 'notes.html', context)

# show note details
def details(request, _slug):
    note=Note.objects.get(slug=_slug)
    context={
        'note':note
    }
    return render(request, 'one_note.html', context)

def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm()

    context={
        'form' : form,
    }
    return render(request, 'create.html', context)

def edit(request, slug):
    note = get_object_or_404(Note, slug=slug)
    # print(note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm(instance=note)

    context={
        'form' : form,
    }
    return render(request, 'update.html', context)
