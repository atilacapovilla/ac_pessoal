from django.contrib import admin
from finance.models import Category, Account, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('group', 'name', 'type', 'method', 'planned_value')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'opening_balance', 'current_balance')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_date', 'due_date', 'account',
                    'description', 'transaction_value', 'is_paid', 'type')
