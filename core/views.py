from django.shortcuts import render


# Create your views here.
def index(request):
    content = {
    'Conteudo': 'Passando conteudo através da view do Django'}
    return render(request, 'index.html', content)

def contato(request):
    return render(request, 'contato.html')