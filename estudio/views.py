from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class Index(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'estudio/index.html')

    def post(self, request, *args, **kwargs):
        
        texto = request.POST["text"]
        palabras = len(texto.split())
        context = {
            'palabras':palabras,
            'texto': texto
        }
        return render(request, 'estudio/index.html', context)