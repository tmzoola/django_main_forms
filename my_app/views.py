from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Car
from .forms import Review



def rental_review(request):
    if request.method == 'POST':
        form = Review(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_app:thank_you'))
    else:
        form = Review()
    return render(request, 'my_app/rental_review.html',context={'form':form})



def thank_you(request):
    return render(request, 'my_app/thank_you.html')





def index(request):
    objects = Car.objects.all()
 

    return render(request, 'my_app/index.html',context={'objects':objects})

def add(request):
    if request.POST:
        brand = request.POST['name']
        year = request.POST['year']
        Car.objects.create(name=brand, year = year)
        return redirect(reverse('my_app:index'))
        
 
    return render(request, 'my_app/add.html')