from django.shortcuts import render
from django.utils import timezone
from ..models import Atividade, Realizacao, Humor

#View HOME
def home(request):
    atividades = Atividade.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')
    realizacoes = Realizacao.objects.filter(data_realizacao__lte=timezone.now()).order_by('data_realizacao')
    humores = Humor.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')
    return render(request, 'base/home.html', {'atividades': atividades, 'realizacoes': realizacoes, 'humores': humores})
