import sweetify

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from apps.finance.forms.transfer_forms import TransferForm
from apps.finance.models.transaction import Transaction


@login_required
def Transfer(request):
    template_name = 'transfer/transfer_form.html'
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
            sweetify.toast(request, 'Tranferancia concluida com sucesso',
                           icon="success", button='OK', timer=2000)

            return redirect('transactions')

    context = {'form': form}
    return render(request, template_name, context)
