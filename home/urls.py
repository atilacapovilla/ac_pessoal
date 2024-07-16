from django.urls import path

from home.views import home, Dashboard


urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', Dashboard.as_view(), name='dashboard')
]
