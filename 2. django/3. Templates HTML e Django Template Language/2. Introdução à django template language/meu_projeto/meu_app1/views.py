from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def segunda(request):
    return render(request, 'page2.html')