from django.shortcuts import render

# Create your views here.
def lista_atividade(request):
    return render(request, 'atividade/lista_atividade.html', {})
