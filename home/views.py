from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/home.html')


@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')
