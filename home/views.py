from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from course.models.course import Course
from . import metrics


def home(request):
    return render(request, 'home/home.html')


def dashboard(request):
    course_metrics = metrics.get_course_metrics(request)

    context = {
        'course_metrics': course_metrics,
    }

    return render(request, 'home/dashboard.html', context)
