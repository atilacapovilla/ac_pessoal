from django import forms
from course.models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['title',]
        labels = {
            "title": ("Título"),
        }
