from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from course.models.course import Course
from course.models.note import Note
from course.forms.note_forms import NoteForm


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/note_list.html'
    paginate_by = 10

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        notes = Note.objects.filter(
            user=self.request.user, course_id=course_id)
        query = self.request.GET.get('search')
        if query:
            notes = notes.filter(title__icontains=query)
        return notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['course_id']
        context["course"] = Course.objects.get(id=id)
        return context


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note/note_form.html'
    form_class = NoteForm
    paginate_by = 10

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.course_id = self.kwargs['course_id']
        messages.success(self.request, 'A Anotação foi criada com sucesso.')
        return super(NoteCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note-list', kwargs={'course_id': self.kwargs['course_id']})


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'note/note_form.html'
    form_class = NoteForm

    def form_valid(self, form):
        messages.success(self.request, 'A Anotação foi alterada com sucesso.')
        return super(NoteUpdate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(NoteUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('note-list', kwargs={'course_id': self.kwargs['course_id']})


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    template_name = 'note/note_confirm_delete.html'

    def form_valid(self, form):
        messages.success(self.request, 'A Anotação foi excluida com sucesso.')
        return super(NoteDelete, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(NoteDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('note-list', kwargs={'course_id': self.kwargs['course_id']})
