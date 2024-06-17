import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from course.models.course import Course
from course.models.note import Note
from course.forms.note_forms import NoteForm


@login_required
def notes(request, id=id):
    course = get_object_or_404(Course, id=id, user=request.user)
    notes = Note.objects.filter(user=request.user, course=course)
    context = {
        'course': course,
        'notes': notes
    }
    return render(request, 'note/note.html', context)


@login_required
def note_list(request, id=id):
    course = get_object_or_404(Course, id=id, user=request.user)
    notes = Note.objects.filter(user=request.user, course=course)
    return render(request, 'note/note_list.html', {'notes': notes})


@login_required
def add_note(request, id=id):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            course = get_object_or_404(Course, id=id, user=request.user)
            note = Note.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                course=course,
                user=request.user
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "noteListChanged": None,
                        "showMessage": f"{note.title} salvo."
                    })
                })
        else:
            return render(request, 'note/note_form.html', {'form': form, })
    else:
        form = NoteForm()
        return render(request, 'note/note_form.html', {'form': form, })


@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, initial={
            'title': note.title,
            'content': note.content,
        })
        if form.is_valid():
            note.title = form.cleaned_data.get('title')
            note.content = form.cleaned_data.get('content')
            note.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "noteListChanged": None,
                        "showMessage": f"{note.title} alterado."
                    })
                }
            )
        else:
            return render(request, 'note/note_form.html', {
                'form': form,
                'note': note,
            })
    else:
        form = NoteForm(initial={
            'title': note.title,
            'content': note.content,
        })
        return render(request, 'note/note_form.html', {'form': form, 'note': note, })


@login_required
def remove_note_confirmation(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'note/note_confirm_delete.html', {'note': note, })


@ require_POST
def remove_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "noteListChanged": None,
                "showMessage": f"{note.title} excluido."
            })
        })


@login_required
def detail_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'note/note_detail.html', {'note': note, })
