from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Atividade, Humor, Realizacao
from ..forms import AtividadeForm, HumorForm, RealizacaoForm

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
 
 