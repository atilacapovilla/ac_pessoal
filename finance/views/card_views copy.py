from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect
from django.shortcuts import render

from finance.models import Account, Category, Transaction
from finance.utils.utils import cards_payment


@login_required
def CardList(request):
    template_name = 'cards/card_list.html'
    cards = []
    total_card = 0

    accounts = Account.objects.filter(
        user=request.user, type='CT').order_by('name')
    accounts_debit = Account.objects.filter(
        user=request.user, type='CC').order_by('name')
    categories = Category.objects.filter(user=request.user, group='4')

    due_date = request.GET.get('due_date')
    account_id = request.GET.get('account')

    if due_date and account_id:
        cards = Transaction.objects.filter(
            user=request.user, account__id=account_id, due_date=due_date, type='D')
        total_card = cards.filter(is_paid=False).aggregate(
            Sum('transaction_value'))['transaction_value__sum'] or 0

    if request.method == 'POST':
        account_debit = request.POST.get('account_debit')
        category = request.POST.get('category')

        if account_debit and category:
            cards_payment(
                cards,
                total_card,
            )

    context = {
        'accounts': accounts,
        'cards': cards,
        'total_card': total_card,
        'accounts_debit': accounts_debit,
        'categories': categories,
    }
    return render(request, template_name, context)

#     cards = Transaction.objects.filter(
#         user=request.user, accounts__id=account_id, due_date=due_date, type='D')
#     total_cards= cards.filter(is_paid=False).aggregate(
#         Sum('value_card'))['value_card__sum']
#     if not total_cards:
#         total_cards = 0

#     context = {
#         'accounts': accounts,
#         'cards': cards,
#         'total_cartao': total_cartao,
#         'contas_debito': contas_debito,
#         'categorias': categorias,
#         'pessoas': pessoas,
#     }

#     return render(request, template_name, context)
