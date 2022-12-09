from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse([1,2,3,"hey",4])
    d = {
        "name":"Allu",
        "age":"24" ,
    }
    return HttpResponse("<b> hello world</b>")