import sweetify
from datetime import date
from calendar import monthrange

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from finance.models import Transaction, Account
from finance.forms import TransactionForm


class TransactionList(LoginRequiredMixin, ListView):
    model = TransactionForm
    context_object_name = 'transactions'
    template_name = 'transaction/transaction_list.html'
    paginate_by = 10

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        account = self.request.GET.get('account')

        print(account)

        if not start_date or not end_date:
            today = date.today()
            start_date = date(today.year, today.month, 1)
            end_date = start_date.replace(day=monthrange(
                start_date.year, start_date.month)[1])

        transactions = Transaction.objects\
            .filter(user=self.request.user, transaction_date__range=[start_date, end_date])\
            .order_by('-transaction_date', '-due_date')

        if account:
            transactions = transactions.filter(account__id=account)

        print(transactions)

        return transactions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Account.objects.filter(user=self.request.user)
        return context

# class AccountCreate(LoginRequiredMixin, CreateView):
#     model = Account
#     template_name = 'account/account_form.html'
#     form_class = AccountForm
#     success_url = reverse_lazy('accounts')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         sweetify.success(self.request, 'A Conta foi criada com suceso.')
#         return super(AccountCreate, self).form_valid(form)


# class AccountUpdate(LoginRequiredMixin, UpdateView):
#     model = Account
#     template_name = 'account/account_form.html'
#     form_class = AccountForm
#     success_url = reverse_lazy('accounts')

#     def form_valid(self, form):
#         sweetify.success(self.request, 'A Conta foi alterada com suceso.')
#         return super(AccountUpdate, self).form_valid(form)

#     def get_queryset(self):
#         base_qs = super(AccountUpdate, self).get_queryset()
#         return base_qs.filter(user=self.request.user)


# class AccountDelete(LoginRequiredMixin, DeleteView):
#     model = Account
#     context_object_name = 'account'
#     template_name = 'account/account_confirm_delete.html'
#     success_url = reverse_lazy('accounts')

#     def form_valid(self, form):
#         sweetify.error(self.request, 'A Conta foi excluida com suceso.')
#         return super(AccountDelete, self).form_valid(form)

#     def get_queryset(self):
#         base_qs = super(AccountDelete, self).get_queryset()
#         return base_qs.filter(user=self.request.user)
