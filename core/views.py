from django.shortcuts import render

from .models import Produto
# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    
    content = {
    'Conteudo': 'Passando conteudo através da view do Django',
    'produtos': produtos
    }
    
    return render(request, 'index.html', content)

def contato(request):
    return render(request, 'contato.html')