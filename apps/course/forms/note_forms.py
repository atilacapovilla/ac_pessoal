from django import forms
from django_summernote.widgets import SummernoteWidget

from apps.course.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'active']
        labels = {
            "title": ("Título"),
            "content": ("Conteúdo"),
            "active": ("Anotação Ativa"),
        }
        widgets = {
            'content': SummernoteWidget()
        }
