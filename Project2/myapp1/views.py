from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.


def home(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'index.html', {'data': chais})