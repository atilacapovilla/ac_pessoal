import json
from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import course_metrics


def home(request):
    return render(request, 'home/home.html')


@login_required
def principal(request):
    course_balance = course_metrics.get_course_metrics(request)

    context = {
        'course_balance': course_balance,
    }

    return render(request, 'home/principal.html', context)
