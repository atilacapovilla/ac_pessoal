from django import forms
from course.models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'description', 'subject']
        labels = {
            "title": ("Título"),
            "description": ("Descrição"),
            "subject": ("Assunto"),
        }
