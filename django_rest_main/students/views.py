from django.shortcuts import render
from django.http import HttpResponse



# Web Aplication ENdpoint
def students(request):
    data = {
        "id": 1,
        "fname": "Dibyendu",
        "lname": "Biswas"
    }
    return HttpResponse(f"<h2> Hello Wrold </h2><p> {data} </p>")


