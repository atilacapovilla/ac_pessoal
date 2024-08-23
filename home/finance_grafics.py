from django.db.models import Sum

from finance.models import Transaction


def get_finance_expense_month(request, month, year):
    labels = []
    data = []

    queryset = Transaction.objects\
        .values('category__name')\
        .annotate(total_expenses=Sum('transaction_value'))\
        .filter(user=request.user, type='D', transaction_date__year=year, transaction_date__month=month)\
        .exclude(category__group='3')\
        .exclude(category__group='4')\
        .order_by('-total_expenses')

    for entry in queryset:
        labels.append(entry['category__name'])
        data.append(int(entry['total_expenses']))

    return labels, data


def get_finance_revenues_expense_year(request, year):
    labels_year = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai',
                   'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez',]
    data_expenses_year = []
    data_revenues_year = []
    dates = [i for i in range(1, 13, 1)]

    transactions = Transaction.objects\
        .filter(user=request.user, transaction_date__year=year)\
        .exclude(category__group='3')\
        .exclude(category__group='4')

    for date in dates:
        expense = transactions\
            .filter(transaction_date__month=date, type='D')\
            .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

        data_expenses_year.append(int(expense))

        revenue = transactions\
            .filter(transaction_date__month=date, type='C')\
            .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

        data_revenues_year.append(int(revenue))

    return labels_year, data_expenses_year, data_revenues_year
