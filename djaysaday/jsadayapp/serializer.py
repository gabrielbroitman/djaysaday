
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from .models import *


class TipoAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAtividade
        fields = ('nome', 'codigo', 'descricao')


class AtividadeSerializer(serializers.ModelSerializer):
    tipoAtividade = TipoAtividadeSerializer
    class Meta:
        model = Atividade
        fields = ('id','nome', 'descricao', 'tipoAtividade', 'data_criacao')



class RealizacaoComAtividadeSerializer(serializers.ModelSerializer):
    atividade = AtividadeSerializer()
    class Meta:
        model = Realizacao
        fields = ('id', 'atividade', 'descricao', 'data_realizacao')
    
    def create(self, validated_data):
        atividade_data = validated_data.pop('atividade', None)
        atividade = Atividade.objects.get_or_create(**atividade_data)[0]
        validated_data['atividade'] = atividade
        realizacao = Realizacao.objects.create(**validated_data)
        return realizacao

    def update(self, instance, validated_data):
        atividade_data = validated_data.pop('atividade', None)
        atividade = Atividade.objects.get_or_create(**atividade_data)[0]
        validated_data['atividade'] = atividade
        instance.atividade = validated_data['atividade']
        instance.descricao = validated_data['descricao']
        instance.data_realizacao = validated_data['data_realizacao']
        instance.save()
        return instance


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