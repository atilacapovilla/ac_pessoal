from django.urls import path

from finance.views.category_views import (
    CategoryList,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
)

urlpatterns = [
    # Category
    path('categories/', CategoryList.as_view(), name='categories'),
    path('category/create/', CategoryCreate.as_view(), name='category-create'),
    path('category/update/<int:pk>/',
         CategoryUpdate.as_view(), name='category-update'),
    path('category/delete/<int:pk>/',
         CategoryDelete.as_view(), name='category-delete'),
]
