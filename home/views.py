import json
from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import course_metrics
from . import finance_metrics
from . import finance_grafics


def home(request):
    return render(request, 'home/home.html')


@login_required
def dashboard(request):
    today = date.today()

    course_balance = course_metrics.get_course_metrics(request)

    labels, data = finance_grafics.get_finance_expense_month(
        request, today.month, today.year)

    labels_year, data_expenses_year, data_revenues_year = finance_grafics.get_finance_revenues_expense_year(
        request, today.year)

    finance_balance = finance_metrics.get_finance_balance(
        request, today.month, today.year)

    finance_accounts_balance = finance_metrics.get_finance_accounts_balance(
        request)

    context = {
        'course_balance': course_balance,
        'finance_balance': finance_balance,
        'labels_month': json.dumps(labels),
        'data_month': json.dumps(data),
        'labels_year': json.dumps(labels_year),
        'data_expenses_year': json.dumps(data_expenses_year),
        'data_revenues_year': json.dumps(data_revenues_year),
        'finance_accounts_balance': finance_accounts_balance,
    }

    return render(request, 'home/dashboard.html', context)
