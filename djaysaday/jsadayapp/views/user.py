from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from ..serializer import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "PUT", "DELETE"])
def detalhe_user(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = settings.AUTH_USER_MODEL
    except settings.AUTH_USER_MODEL.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(user)

    # elif request.method == "PUT":
    #     serializer = AtividadeSerializer(atividade, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == "DELETE":
    #     atividade.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
