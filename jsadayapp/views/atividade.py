from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Atividade
from ..forms import AtividadeForm

# Views ATIVIDADE


def lista_atividade(request):
    atividades = Atividade.objects.filter(
        data_criacao__lte=timezone.now()).order_by('data_criacao')
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
