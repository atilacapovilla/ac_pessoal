from django.urls import path

from home.views import home, dashboard


urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard')
]
