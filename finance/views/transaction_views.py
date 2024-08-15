import sweetify
from datetime import date
from calendar import monthrange

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from finance.models import Transaction, Account
from finance.forms import TransactionForm, TransferForm


class TransactionList(LoginRequiredMixin, ListView):
    model = TransactionForm
    context_object_name = 'transactions'
    template_name = 'transaction/transaction_list.html'
    paginate_by = 10

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        account = self.request.GET.get('account')

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

        return transactions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Account.objects.filter(user=self.request.user)
        return context


class TransactionCreate(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = 'transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transactions')

    def get_initial(self):
        return {'user': self.request.user}

    def form_valid(self, form):
        form.instance.user = self.request.user
        sweetify.success(self.request, 'A Transaçãofoi criada com suceso.')
        return super(TransactionCreate, self).form_valid(form)


class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaction
    template_name = 'transaction/transaction_form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transactions')

    def get_initial(self):
        return {'user': self.request.user}

    def form_valid(self, form):
        sweetify.success(self.request, 'A Transação foi alterada com suceso.')
        return super(TransactionUpdate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TransactionUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'transaction/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions')

    def form_valid(self, form):
        sweetify.error(self.request, 'A Transação foi excluida com suceso.')
        return super(TransactionDelete, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TransactionDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)


@login_required
def Transfer(request):
    template_name = 'transaction/transfer_form.html'
    form = TransferForm(request.user, request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            transaction_date = request.POST.get('transaction_date')
            account_origin = request.POST.get('account_origin')
            account_destination = request.POST.get('account_destination')
            category = request.POST.get('category')
            transaction_value = request.POST.get('transaction_value')
            description = request.POST.get('description')

            transction = Transaction(
                due_date=transaction_date,
                transaction_date=transaction_date,
                account_id=account_origin,
                category_id=category,
                transaction_value=transaction_value,
                description=description,
                type='D',
                is_paid=True,
                user=request.user,
            )
            transction.save()

            transction = Transaction(
                due_date=transaction_date,
                transaction_date=transaction_date,
                account_id=account_destination,
                category_id=category,
                transaction_value=transaction_value,
                description=description,
                type='C',
                is_paid=True,
                user=request.user,
            )
            transction.save()

            return redirect('transactions')

    context = {'form': form}
    return render(request, template_name, context)
