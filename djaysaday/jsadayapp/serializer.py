
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
        model = settings.AUTH_USER_MODEL