from django import forms
from finance.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'group', 'type', 'method']

        labels = {
            "name": ("Nome"),
            "group": ("Grupo"),
            "type": ("Fixa ou Variável"),
            "method": ("Método 50-30-20"),
        }
