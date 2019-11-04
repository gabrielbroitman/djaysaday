from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializer import *
from django.utils import timezone
from ..models import Humor, Sensacao
from ..forms import HumorForm

# Views HUMOR

@api_view(['GET'])
def lista_sensacoes(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sensacoes = Sensacao.objects.all()
        serializer = SensacaoSerializer(sensacoes, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def lista_humor(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        humores = Humor.objects.filter(autor=request.user).order_by('data_criacao')
        serializer = HumorSerializer(humores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HumorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_humor(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        humor = Humor.objects.get(pk=pk)
    except Humor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HumorSerializer(humor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HumorSerializer(humor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        humor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)