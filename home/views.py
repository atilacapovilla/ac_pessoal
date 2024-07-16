from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from course.models.course import Course


def home(request):
    return render(request, 'home/home.html')


class Dashboard(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'home/dashboard.html'
    paginate_by = 3

    def get_queryset(self):
        courses = Course.objects.filter(
            user=self.request.user).order_by('title')
        # query = self.request.GET.get('search')
        # if query:
        #     courses = courses.filter(title__icontains=query)
        return courses
