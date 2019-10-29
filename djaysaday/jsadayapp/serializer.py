
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from .models import *


class TipoAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAtividade
        fields = ('nome', 'codigo', 'descricao')


class AtividadeSerializer(serializers.ModelSerializer):
    tipoAtividade = TipoAtividadeSerializer(read_only=True)
    class Meta:
        model = Atividade
        fields = ('id','nome', 'descricao', 'tipoAtividade', 'data_criacao')



class RealizacaoComAtividadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Realizacao
        fields = ('id', 'atividade', 'descricao', 'data_realizacao')


class HumorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humor
        fields = ('id', 'nome', 'nivel', 'sensacoes', 'realizacoes', 'descricao', 'data_criacao')


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