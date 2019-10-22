from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Atividade, Humor, Realizacao
from .forms import AtividadeForm, HumorForm, RealizacaoForm

# Create your views here.
# Views ATIVIDADE
def lista_atividade(request):
    atividades = Atividade.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')
    return render(request, 'atividade/lista_atividade.html', {'atividades': atividades})

def detalhe_atividade(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    return render(request, 'atividade/detalhe_atividade.html', {'atividade': atividade})

def nova_atividade(request):
     if request.method == "POST":
         form = AtividadeForm(request.POST)
         if form.is_valid():
             atividade = form.save(commit=False)
             atividade.autor = request.user
             atividade.data_criacao = timezone.now()
             atividade.save()
             return redirect('detalhe_atividade', pk=atividade.pk)
     else:
         form = AtividadeForm()
     return render(request, 'atividade/edicao_atividade.html', {'form': form})


def edicao_atividade(request, pk):
     atividade = get_object_or_404(Atividade, pk=pk)
     if request.method == "POST":
         form = AtividadeForm(request.POST, instance=atividade)
         if form.is_valid():
             atividade = form.save(commit=False)
             atividade.autor = request.user
             atividade.data_criacao = timezone.now()
             atividade.save()
             return redirect('detalhe_atividade', pk=atividade.pk)
     else:
         form = AtividadeForm(instance=atividade)
     return render(request, 'atividade/edicao_atividade.html', {'form': form})
 
 
# Views HUMOR
def lista_humor(request):
    humores = Humor.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')
    return render(request, 'humor/lista_humor.html', {'humores': humores})

def detalhe_humor(request, pk):
    humor = get_object_or_404(Humor, pk=pk)
    return render(request, 'humor/detalhe_humor.html', {'humor': humor})

def novo_humor(request):
     if request.method == "POST":
         form = HumorForm(request.POST)
         if form.is_valid():
             humor = form.save(commit=False)
             humor.autor = request.user
             humor.data_criacao = timezone.now()
             humor.save()
             return redirect('detalhe_humor', pk=humor.pk)
     else:
         form = HumorForm()
     return render(request, 'humor/edicao_humor.html', {'form': form})


def edicao_humor(request, pk):
     humor = get_object_or_404(Humor, pk=pk)
     if request.method == "POST":
         form = HumorForm(request.POST, instance=humor)
         if form.is_valid():
             humor = form.save(commit=False)
             humor.autor = request.user
             humor.data_criacao = timezone.now()
             humor.save()
             return redirect('detalhe_humor', pk=humor.pk)
     else:
         form = HumorForm(instance=humor)
     return render(request, 'humor/edicao_humor.html', {'form': form})
 
 

# Views REALIZACAO
def lista_realizacao(request):
    realizacoes = Realizacao.objects.filter(data_realizacao__lte=timezone.now()).order_by('data_realizacao')
    return render(request, 'realizacao/lista_realizacao.html', {'realizacoes': realizacoes})

def detalhe_realizacao(request, pk):
    realizacao = get_object_or_404(Realizacao, pk=pk)
    return render(request, 'realizacao/detalhe_realizacao.html', {'realizacao': realizacao})

def nova_realizacao(request):
     if request.method == "POST":
         form = RealizacaoForm(request.POST)
         if form.is_valid():
             realizacao = form.save(commit=False)
             realizacao.autor = request.user
             realizacao.save()
             return redirect('detalhe_realizacao', pk=realizacao.pk)
     else:
         form = RealizacaoForm()
     return render(request, 'realizacao/edicao_realizacao.html', {'form': form})


def edicao_realizacao(request, pk):
     realizacao = get_object_or_404(Realizacao, pk=pk)
     if request.method == "POST":
         form = RealizacaoForm(request.POST, instance=realizacao)
         if form.is_valid():
             realizacao = form.save(commit=False)
             realizacao.autor = request.user
             realizacao.save()
             return redirect('detalhe_realizacao', pk=realizacao.pk)
     else:
         form = RealizacaoForm(instance=realizacao)
     return render(request, 'realizacao/edicao_realizacao.html', {'form': form})
 
 
