from django import forms

from finance.models import Category, Account, Transaction


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


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_date', 'due_date', 'is_paid',  'account',
                  'category', 'description', 'transaction_value', 'type']

        labels = {
            "transaction_date": ("Data da Transação"),
            "due_date": ("Data de Vencimento"),
            "is_paid": ("Está pago ?"),
            "account": ("Conta"),
            "category": ("Categoria"),
            "description": ("Descrição"),
            "transaction_value": ("Valor da Transação"),
            "Type": ("Tipo"),
        }
