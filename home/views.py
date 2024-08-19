from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.list import ListView

# from course.models.course import Course
from . import metrics_courses
from . import metrics_finances


def home(request):
    return render(request, 'home/home.html')


@login_required
def dashboard(request):
    course_metrics = metrics_courses.get_course_metrics(request)
    finance_metrics = metrics_finances.get_finance_metrics(request)

    context = {
        'course_metrics': course_metrics,
        'finance_metrics': finance_metrics,
    }

    return render(request, 'home/dashboard.html', context)
