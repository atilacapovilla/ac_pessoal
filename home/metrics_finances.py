from datetime import date
from django.db.models import Sum

from finance.models import Transaction


def get_finance_metrics(request):
    today = date.today()

    transactions = Transaction.objects\
        .filter(user=request.user, transaction_date__year=today.year, transaction_date__month=today.month)\
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
