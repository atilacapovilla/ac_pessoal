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


def get_finance_method(request, month, year):
    transactions = Transaction.objects\
        .filter(user=request.user, transaction_date__year=year, transaction_date__month=month)\

    revenues = transactions\
        .filter(type='C')\
        .exclude(category__group='3')\
        .exclude(category__group='4')\
        .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

    essential_prev = revenues * 50 / 100
    superfluous_prev = revenues * 30 / 100
    investments_prev = revenues * 20 / 100

    essential_real = transactions\
        .filter(type='D', category__method='1')\
        .exclude(category__group='3')\
        .exclude(category__group='4')\
        .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

    superfluous_real = transactions\
        .filter(type='D', category__method='2')\
        .exclude(category__group='3')\
        .exclude(category__group='4')\
        .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

    investiments_real = transactions\
        .filter(type='C', category__method='3')\
        .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

    essential_perc = essential_real / revenues * 100
    superfluous_perc = superfluous_real / revenues * 100
    investiments_perc = investiments_real / revenues * 100

    finance_method = dict(
        revenues=revenues,
        essential_prev=essential_prev,
        superfluous_prev=superfluous_prev,
        investments_prev=investments_prev,
        essential_real=essential_real,
        essential_perc=essential_perc,
        superfluous_real=superfluous_real,
        superfluous_perc=superfluous_perc,
        investiments_real=investiments_real,
        investiments_perc=investiments_perc,
    )

    labels_method = ['Essencial', 'Superfluo', 'Divida/Investimento']
    data_method = []
    data_method.append(int(essential_perc))
    data_method.append(int(superfluous_perc))
    data_method.append(int(investiments_perc))

    return finance_method, labels_method, data_method
