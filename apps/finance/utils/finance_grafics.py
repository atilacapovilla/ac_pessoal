from django.db.models import Sum

from apps.finance.models.transaction import Transaction


def get_finance_expense_month(request, month, year):
    labels_fix = []
    data_fix = []
    labels_var = []
    data_var = []

    queryset = Transaction.objects\
        .values('category__name')\
        .annotate(total_expenses=Sum('transaction_value'))\
        .filter(user=request.user, type='D', transaction_date__year=year, transaction_date__month=month)\
        .exclude(category__category_type='investimento')\
        .exclude(category__category_type='transferencia')\
        .order_by('-total_expenses')

    expenses_fix = queryset.filter(category__category_nature='fixa')\

    for entry in expenses_fix:
        labels_fix.append(entry['category__name'])
        data_fix.append(int(entry['total_expenses']))

    expenses_var = queryset.filter(category__category_nature='variavel')\

    for entry in expenses_var:
        labels_var.append(entry['category__name'])
        data_var.append(int(entry['total_expenses']))

    return labels_fix, data_fix, labels_var, data_var


def get_finance_incomes_expense_year(request, year):
    labels_year = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai',
                   'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez',]
    data_expenses_year = []
    data_incomes_year = []
    dates = [i for i in range(1, 13, 1)]

    transactions = Transaction.objects\
        .filter(user=request.user, transaction_date__year=year)\
        .exclude(category__category_type='investimento')\
        .exclude(category__category_type='transferencia')

    for date in dates:
        expense = transactions\
            .filter(transaction_date__month=date, type='D')\
            .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

        data_expenses_year.append(int(expense))

        income = transactions\
            .filter(transaction_date__month=date, type='C')\
            .aggregate(Sum('transaction_value'))['transaction_value__sum'] or 0

        data_incomes_year.append(int(income))

    return labels_year, data_expenses_year, data_incomes_year
