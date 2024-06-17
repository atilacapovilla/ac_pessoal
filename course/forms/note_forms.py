from django import forms
from django_summernote.widgets import SummernoteWidget
from course.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        labels = {
            "title": ("Título"),
            "content": ("Conteúdo"),
        }
        widgets = {
            'content': SummernoteWidget()
        }
