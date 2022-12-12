from django.shortcuts import get_object_or_404, render

from .models import Produto


# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    
    content = {
    'Conteudo': 'Passando conteudo através da view do Django',
    'produtos': produtos,
    }
    
    return render(request, 'index.html', content)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id = pk)
    context = {
        'produto':prod
    }
    return render(request, 'produto.html',context)