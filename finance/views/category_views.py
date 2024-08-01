import sweetify

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from finance.models import Category
from finance.forms import CategoryForm


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category/category_list.html'
    paginate_by = 10

    def get_queryset(self):
        categories = Category.objects.filter(user=self.request.user)
        query = self.request.GET.get('search')
        if query:
            categories = categories.filter(name__icontains=query)
        return categories


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        form.instance.user = self.request.user
        sweetify.success(self.request, 'A Categoria foi criada com suceso.')
        return super(CategoryCreate, self).form_valid(form)


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'category/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        sweetify.success(self.request, 'A Categoria foi alterada com suceso.')
        return super(CategoryUpdate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(CategoryUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        sweetify.error(self.request, 'A Categoria foi excluida com suceso.')
        return super(CategoryDelete, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(CategoryDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)
