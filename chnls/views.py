from django.shortcuts import render, redirect, get_object_or_404
from .models import Statictic, DataItem
from faker import Faker

fake = Faker()

def main(request):
    qs = Statictic.objects.all()
    if request.method == 'POST':
        new_stat = request.POST.get('new-statistic')
        obj, _ =Statictic.objects.get_or_create(name=new_stat)
        return redirect('chnls:dashboard', obj.slug)

    return render(request, 'chnls/main.html', {'qs': qs})

def dashboard(request, slug):
    obj = get_object_or_404(Statictic, slug=slug)
    return render(request, 'chnls/dashboard.html', {
            'name': obj.name,
            'slug': obj.slug,
            'data': obj.data,
            'user': request.user.username if request.user.username else fake.name()
            

    })