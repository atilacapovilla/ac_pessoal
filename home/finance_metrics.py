from datetime import date
from django.db.models import Q
from django.db.models import Sum

from finance.models import Account, Transaction


def get_finance_balance(request, month, year):

    transactions = Transaction.objects\
        .filter(user=request.user, transaction_date__year=year, transaction_date__month=month)\
        .exclude(category__group='3')\
        .exclude(category__group='4')

    expenses = transactions\
        .filter(type='D')\
        .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

    revenues = transactions\
        .filter(type='C')\
        .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

    balance = revenues - expenses

    return dict(
        expenses=expenses,
        revenues=revenues,
        balance=balance,
    )


def get_finance_accounts_balance(request):
    balance_total = 0

    accounts = Account.objects.filter(
        Q(user=request.user), Q(type='CC') | Q(type='DN'),)

    for account in accounts:
        transactions = Transaction.objects.filter(
            account=account, is_paid=True)
        expenses = transactions.filter(type='D').aggregate(
            Sum('transaction_value'))['transaction_value__sum'] or 0
        revenues = transactions.filter(type='C').aggregate(
            Sum('transaction_value'))['transaction_value__sum'] or 0
        balance = account.opening_balance + revenues - expenses
        account.current_balance = balance
        account.save()
        balance_total += balance

    accounts_other = Account.objects.filter(user=request.user).exclude(
        type='CC').exclude(type='DN').order_by('type', 'name')
    for account in accounts_other:
        transactions = Transaction.objects.filter(account=account)
        expenses = transactions.filter(type='D').aggregate(
            Sum('transaction_value'))['transaction_value__sum'] or 0
        revenues = transactions.filter(type='C').aggregate(
            Sum('transaction_value'))['transaction_value__sum'] or 0
        balance = account.opening_balance + revenues - expenses
        account.current_balance = balance
        account.save()

    finance_accounts_balance = dict(
        accounts=accounts,
        accounts_other=accounts_other,
        balance_total=balance_total,
    )
    return finance_accounts_balance
