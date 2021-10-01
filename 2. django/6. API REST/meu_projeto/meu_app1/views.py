from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    frutas = ["maçã", "banana", "morango", "abacaxi", "kiwi"]
    flag = False

    dicionario = {"frutas": frutas, "flag": flag}

    return render(request, 'index.html', dicionario)

def segunda(request):
    return render(request, 'page2.html')