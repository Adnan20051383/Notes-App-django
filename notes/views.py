from datetime import timezone, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from notes.models import Note


def show_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {"notes": notes})


def show_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'note-detail.html', {"note": note})


def make_note(request):
    note = Note(title=request.POST['title'], content=request.POST['content'], datetime=datetime.now())
    note.save()
    return redirect('notes')


