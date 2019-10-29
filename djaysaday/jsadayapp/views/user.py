from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from ..serializer import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


@api_view(["GET", "PUT", "DELETE"])
def detalhe_user(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        if user is not None:

            auth.login(request, user)
            return Response('Logado com sucesso!')
        else:
            return Response('Credenciais inválidas', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def isauthenticated_user(request):

    if serializer.is_valid():
        if user.is_authenticated:

            return Response(True)
        else:
            return Response(False)


@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response('Deslogado com sucesso!', status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
@permission_classes((AllowAny,))
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == "PUT":
    #     serializer = AtividadeSerializer(atividade, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == "DELETE":
    #     atividade.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)