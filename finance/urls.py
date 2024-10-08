from django.urls import path

from finance.views.category_views import (
    CategoryList,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
)
from finance.views.account_views import (
    AccountList,
    AccountCreate,
    AccountUpdate,
    AccountDelete,
)
from finance.views.transaction_views import (
    TransactionList,
    TransactionCreate,
    TransactionUpdate,
    TransactionDelete,
)
from finance.views.transfer_views import Transfer
from finance.views.card_views import CardList

urlpatterns = [
    # Category
    path('categories/', CategoryList.as_view(), name='categories'),
    path('category/create/', CategoryCreate.as_view(), name='category-create'),
    path('category/update/<int:pk>/',
         CategoryUpdate.as_view(), name='category-update'),
    path('category/delete/<int:pk>/',
         CategoryDelete.as_view(), name='category-delete'),
    # Accounts
    path('accounts/', AccountList.as_view(), name='accounts'),
    path('account/create/', AccountCreate.as_view(), name='account-create'),
    path('account/update/<int:pk>/',
         AccountUpdate.as_view(), name='account-update'),
    path('account/delete/<int:pk>/',
         AccountDelete.as_view(), name='account-delete'),
    # Transactions
    path('transactions/', TransactionList.as_view(), name='transactions'),
    path('transaction/create/', TransactionCreate.as_view(),
         name='transaction-create'),
    path('transaction/update/<int:pk>/',
         TransactionUpdate.as_view(), name='transaction-update'),
    path('transaction/delete/<int:pk>/',
         TransactionDelete.as_view(), name='transaction-delete'),
    # Tranfer
    path('transfer/', Transfer, name='transfer'),
    # Cards
    path('cards/', CardList, name='cards'),
]
