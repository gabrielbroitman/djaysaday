
from rest_framework import serializers
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
