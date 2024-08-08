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

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        user = kwargs['initial']['user']
        self.fields['account'].queryset = Account.objects.filter(user=user)
        self.fields['category'].queryset = Category.objects.filter(user=user)

    transaction_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}), label='Data da Transação')
    due_date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}), label='Data de Vencimento')

    class Meta:
        model = Transaction
        fields = ['transaction_date', 'due_date', 'is_paid',  'account',
                  'category', 'description', 'transaction_value', 'type']
