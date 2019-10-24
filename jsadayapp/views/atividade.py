from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
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
        atividades = Atividade.objects.all()
        serializer = AtividadeSerializer(atividades, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AtividadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        atividade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

