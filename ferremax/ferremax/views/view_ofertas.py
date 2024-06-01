from django.shortcuts import render

def ofertas(request):
    return render(request, 'ofertas.html',{})