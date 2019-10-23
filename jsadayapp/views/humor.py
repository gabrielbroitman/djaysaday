from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Humor
from ..forms import HumorForm

# Views HUMOR


def lista_humor(request):
    humores = Humor.objects.filter(
        data_criacao__lte=timezone.now()).order_by('data_criacao')
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
