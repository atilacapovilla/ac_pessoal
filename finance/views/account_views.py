import sweetify

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from finance.models import Account
from finance.forms import AccountForm


class AccountList(LoginRequiredMixin, ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'account/account_list.html'
    paginate_by = 10

    def get_queryset(self):
        accounts = Account.objects.filter(user=self.request.user)
        query = self.request.GET.get('search')
        if query:
            accounts = accounts.filter(name__icontains=query)
        return accounts


class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    template_name = 'account/account_form.html'
    form_class = AccountForm
    success_url = reverse_lazy('accounts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        sweetify.success(self.request, 'A Conta foi criada com suceso.')
        return super(AccountCreate, self).form_valid(form)


class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'account/account_form.html'
    form_class = AccountForm
    success_url = reverse_lazy('accounts')

    def form_valid(self, form):
        sweetify.success(self.request, 'A Conta foi alterada com suceso.')
        return super(AccountUpdate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(AccountUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    context_object_name = 'account'
    template_name = 'account/account_confirm_delete.html'
    success_url = reverse_lazy('accounts')

    def form_valid(self, form):
        sweetify.error(self.request, 'A Conta foi excluida com suceso.')
        return super(AccountDelete, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(AccountDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)
