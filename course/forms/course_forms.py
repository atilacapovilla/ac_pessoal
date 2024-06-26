from django import forms
from course.models import Course
from course.models import Subject


class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        usuario = kwargs['initial']['usuario']
        self.fields['subject'].queryset = Subject.objects.filter(user=usuario)

    class Meta:
        model = Course
        fields = ['title', 'description', 'subject']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 8}),
        }
        labels = {
            "title": ("Título"),
            "description": ("Descrição"),
            "subject": ("Assunto"),
        }
