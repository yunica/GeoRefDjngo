from django.shortcuts import render


# Create your views here.

def mainn(request):
    return render(request, 'mapa1/pag1.html', {})
