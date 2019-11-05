
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from .models import *


class TipoAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAtividade
        fields = ('nome', 'codigo', 'descricao')


class AtividadeSerializer(serializers.ModelSerializer):
    tipoAtividade = TipoAtividadeSerializer()
    class Meta:
        model = Atividade
        fields = ('id','nome', 'descricao', 'tipoAtividade', 'data_criacao')



class RealizacaoComAtividadeSerializer(serializers.ModelSerializer):
    atividade = AtividadeSerializer()
    id = serializers.ModelField(model_field=Realizacao()._meta.get_field('id'))
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

class SensacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensacao
        fields = ('id','nome')

class HumorSerializer(serializers.ModelSerializer):
    realizacoes = RealizacaoComAtividadeSerializer(many=True)
    sensacoes = SensacaoSerializer(many=True)

    class Meta:
        model = Humor
        fields = ('id', 'nivel', 'sensacoes', 'realizacoes', 'descricao', 'data_criacao')
    
    def create(self, validated_data):
        sensacoes_data = validated_data.pop('sensacoes')
        realizacoes_data = validated_data.pop('realizacoes')
        realizacoes_list = []
        sensacoes_list = []
        for sensacaoData in sensacoes_data:
            sensacao, created = Sensacao.objects.get_or_create(nome=sensacaoData['nome'])
            print(sensacaoData)
            sensacoes_list.append(sensacao)
        for realizacaoData in realizacoes_data:
            print(realizacaoData)
            realizacao, created = Realizacao.objects.get_or_create(id=realizacaoData['id'])
            print('REALIZACAO CRIADA!')
            realizacoes_list.append(realizacao)
        #validated_data['realizacoes'] = realizacoes_list
        #validated_data['sensacoes'] = sensacoes_list
        humor = Humor.objects.create(**validated_data)
        humor.realizacoes.set(realizacoes_list)
        humor.sensacoes.set(sensacoes_list)
        humor.save()
        return humor

    def update(self, instance, validated_data):
        sensacoes_data = validated_data.pop('sensacoes')
        realizacoes_data = validated_data.pop('realizacoes')
        realizacoes_list = []
        sensacoes_list = []
        for sensacaoData in sensacoes_data:
            sensacao, created = Sensacao.objects.get_or_create(nome=sensacaoData['nome'])
            print(sensacaoData)
            sensacoes_list.append(sensacao)
        for realizacaoData in realizacoes_data:
            print(realizacaoData)
            realizacao, created = Realizacao.objects.get_or_create(id=realizacaoData['id'])
            print('REALIZACAO CRIADA!')
            realizacoes_list.append(realizacao)
        instance.realizacoes.set(realizacoes_list)
        instance.sensacoes.set(sensacoes_list)
        instance.nivel = validated_data['nivel']
        instance.descricao = validated_data['descricao']
        instance.data_realizacao = validated_data['data_criacao']
        instance.save()
        return instance




    


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