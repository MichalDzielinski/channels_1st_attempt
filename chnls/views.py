from django.shortcuts import render
from .models import Statictic, DataItem

def main(request):
    qs = Statictic.objects.all()
    return render(request, 'chnls/main.html', {'qs': qs})

def dashboard(request, slug):
    return render(request, 'chnls/dashboard.html', {})