from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. It's polls index.")

# Create your views here.
