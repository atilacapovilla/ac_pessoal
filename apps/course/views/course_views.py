import sweetify

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from apps.course.models.course import Course
from apps.course.models.course import Subject
from apps.course.forms.course_forms import CourseForm


class CourseList(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/course_list.html'
    paginate_by = 10

    def get_queryset(self):
        courses = Course.objects.filter(user=self.request.user)
        query = self.request.GET.get('search')
        if query:
            courses = courses.filter(title__icontains=query)
        return courses


class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('courses')

    def get_initial(self):
        return {'usuario': self.request.user}

    def form_valid(self, form):
        form.instance.user = self.request.user
        sweetify.success(self.request, 'O Curso foi criado com suceso.')
        return super(CourseCreate, self).form_valid(form)


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'course/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('courses')

    def get_initial(self):
        return {'usuario': self.request.user}

    def form_valid(self, form):
        # messages.success(self.request, 'O Curso foi alterado com sucesso.')
        sweetify.success(self.request, 'O Curso foi alterado com suceso.')
        return super(CourseUpdate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(CourseUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    context_object_name = 'course'
    template_name = 'course/course_confirm_delete.html'
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        # messages.success(self.request, 'O Curso foi excluido com sucesso.')
        sweetify.error(self.request, 'O Curso foi excluido com suceso.')
        return super(CourseDelete, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(CourseDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)
