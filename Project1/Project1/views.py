from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, world. You're at the home page.")


def about(request):
    return HttpResponse("This is the about page.")


def contact(request):
    return HttpResponse("This is the contact page.")


# Render the HTML template for the home page
def Webpage(request):
    return render(request, "index.html")

def Webpage2(request):
    return render(request, "webpages/web2.html")

def Webpage3(request):
    return render(request, "webpages/web3.html")