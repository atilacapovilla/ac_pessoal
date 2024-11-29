import json
from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.finance.utils import finance_metrics
from apps.finance.utils import finance_grafics


@login_required
def dashboard(request):
    today = date.today()

    labels_fix, data_fix, labels_var, data_var = finance_grafics.get_finance_expense_month(
        request, today.month, today.year)

    labels_year, data_expenses_year, data_incomes_year = finance_grafics.get_finance_incomes_expense_year(
        request, today.year)

    finance_balance = finance_metrics.get_finance_balance(
        request, today.month, today.year)

    finance_accounts_balance = finance_metrics.get_finance_accounts_balance(
        request)

    total_balance = finance_accounts_balance['balance_total']

    finance_pendents = finance_metrics.get_finance_pendents(
        total_balance, request)

    finance_method = finance_metrics.get_finance_method(request)

    context = {
        'finance_balance': finance_balance,
        'labels_fix': json.dumps(labels_fix),
        'data_fix': json.dumps(data_fix),
        'labels_var': json.dumps(labels_var),
        'data_var': json.dumps(data_var),
        'labels_year': json.dumps(labels_year),
        'data_expenses_year': json.dumps(data_expenses_year),
        'data_incomes_year': json.dumps(data_incomes_year),
        'finance_accounts_balance': finance_accounts_balance,
        'finance_pendents': finance_pendents,
        'finance_method': finance_method,
    }

    return render(request, 'dashboard/dashboard.html', context)
