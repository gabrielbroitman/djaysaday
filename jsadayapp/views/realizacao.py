from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..forms import RealizacaoComAtividadeForm, RealizacaoSemAtividadeForm, AtividadeForm
from ..models import Atividade, Realizacao

# Views REALIZACAO


def lista_realizacao(request):
    realizacoes = Realizacao.objects.filter(
        data_realizacao__lte=timezone.now()).order_by('data_realizacao')
    return render(request, 'realizacao/lista_realizacao.html', {'realizacoes': realizacoes})


def detalhe_realizacao(request, pk):
    realizacao = get_object_or_404(Realizacao, pk=pk)
    return render(request, 'realizacao/detalhe_realizacao.html', {'realizacao': realizacao})


def nova_realizacao_atividade(request):
    if request.method == "POST":
        form = RealizacaoComAtividadeForm(request.POST)
        if form.is_valid():
            realizacao = form.save(commit=False)
            realizacao.autor = request.user
            realizacao.save()
            return redirect('detalhe_realizacao', pk=realizacao.pk)
    else:
        form = RealizacaoComAtividadeForm()

    return render(request, 'realizacao/edicao_realizacao.html', {'form': form})

def nova_realizacao(request):
    if request.method == "POST":
        form = RealizacaoSemAtividadeForm(request.POST)
        formAtividade = AtividadeForm(request.POST)
        if form.is_valid() & formAtividade.is_valid():
            atividade = formAtividade.save(commit=False)
            realizacao = form.save(commit=False)
            realizacao.autor = request.user
            atividade.autor = request.user
            atividade.save()
            realizacao.atividade = atividade
            realizacao.save()
            return redirect('detalhe_realizacao', pk=realizacao.pk)
    else:
        formAtividade =  AtividadeForm()
        form = RealizacaoSemAtividadeForm()

    return render(request, 'realizacao/edicao_realizacao.html', {'form': form, 'formAtividade': formAtividade})



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
