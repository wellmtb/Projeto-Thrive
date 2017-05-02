from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

context = {
'titulo' : '2001 Video - O Cinema está aqui!',
'footer': '© Todos os direitos reservados ',
}


def index(request):
    	return render(request,"index.html",context)

def produtos(request):
    return render(request,"produtos.html",context)

def contatos(request):
    return render( request, "contatos.html", context)