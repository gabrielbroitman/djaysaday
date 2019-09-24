from django.shortcuts import render
from django.utils import timezone
from .models import Atividade

# Create your views here.
def lista_atividade(request):
    atividades = Atividade.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')
    return render(request, 'atividade/lista_atividade.html', {'atividades': atividades})
