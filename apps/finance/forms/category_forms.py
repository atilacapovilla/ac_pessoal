from django import forms

from apps.finance.models.category import Category


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Category.objects.filter(
            parent__isnull=True)

    class Meta:
        model = Category
        fields = ['name', 'parent', 'order', 'category_type',
                  'category_nature', 'category_priority', 'active']
