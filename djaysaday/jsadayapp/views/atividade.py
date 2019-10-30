from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Count
from django.db import models
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Atividade
from ..forms import AtividadeForm
from ..serializer import *

# Views ATIVIDADE



@api_view(['GET', 'POST'])
def lista_atividade(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        atividades = Atividade.objects.filter(autor=request.user)
        serializer = AtividadeSerializer(atividades, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AtividadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def lista_atividade_rank(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        atividades = Atividade.objects.annotate(realizacao_count=Count('realizacao_atividade')).filter(realizacao_count__gt = 0 and autor==request.user).order_by('-realizacao_count')
        serializer = AtividadeSerializer(atividades, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_atividade(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        atividade = Atividade.objects.get(pk=pk)
    except Atividade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AtividadeSerializer(atividade)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AtividadeSerializer(atividade, data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        atividade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

