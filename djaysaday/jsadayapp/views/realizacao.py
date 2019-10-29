from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializer import *
from django.utils import timezone

from ..forms import RealizacaoComAtividadeForm, RealizacaoSemAtividadeForm, AtividadeForm
from ..models import Atividade, Realizacao

# Views REALIZACAO


@api_view(['GET', 'POST'])
def lista_realizacao(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        realizacoes = Realizacao.objects.filter(data_realizacao__lte=timezone.now()).order_by('data_realizacao')
        serializer = RealizacaoComAtividadeSerializer(realizacoes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RealizacaoComAtividadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_realizacao(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        realizacao = Realizacao.objects.get(pk=pk)
    except Realizacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RealizacaoComAtividadeSerializer(realizacao)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RealizacaoComAtividadeSerializer(realizacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        realizacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
