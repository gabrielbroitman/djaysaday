
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from .models import *


class AtividadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atividade
        fields = ('nome', 'descricao', 'tipoAtividade', 'data_criacao')



class RealizacaoComAtividadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Realizacao
        fields = ('atividade', 'descricao', 'data_realizacao')


class HumorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humor
        fields = ('nome', 'nivel', 'sensacoes', 'realizacoes', 'descricao', 'data_criacao')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = ('username', 'password', 'email')
        exclude = ['username', 'password', 'email']
        read_only_fields = ('username', 'password', 'email')


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        exclude = ['username', 'password', 'email']
        read_only_fields = ('username', 'password', 'email')