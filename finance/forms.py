from django import forms

from finance.models import Category, Account


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


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'type', 'opening_balance',  'logo']

        labels = {
            "name": ("Nome"),
            "type": ("Tipo de Conta"),
            "opening_balance": ("Saldo Inicial"),
            "logo": ("Logotipo"),
        }
