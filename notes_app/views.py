from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.

# show all notes
def all_notes(request):
    pass
    # return HttpResponse('<h1> this  section retrive all notes </h1>')
    all_notes = Note.objects.all()
    context={
       'allNotes' : all_notes 
    }
    return render(request, 'all_notes.html', context)
# show note details
def details(request):
    pass