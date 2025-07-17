from django.shortcuts import render
from .models import Cloth

def home(request):
    clothes = Cloth.objects.filter(size='L')  # for now only size L
    return render(request, 'main/home.html', {'clothes': clothes})
