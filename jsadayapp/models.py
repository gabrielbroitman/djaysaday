from django.db import models
from django.conf import settings
from django.utils import timezone

class TipoAtividade(models.Model):
    nome = models.CharField(max_length=12)
    codigo = models.CharField(max_length=1)
    descricao = models.TextField()
    #data_ultima_utilizacao = models.DateTimeField(blank=True, null=True)
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipoAtividade = models.ForeignKey('TipoAtividade', on_delete=models.CASCADE, default=None)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def cadastrar(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome



class Realizacao(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    atividade = models.ForeignKey('Atividade', on_delete=models.CASCADE, default=None)
    descricao = models.TextField()
    data_realizacao = models.DateTimeField(default=timezone.now)
    # data_ultima_utilizacao = models.DateTimeField(blank=True, null=True) #

    def publish(self):
        self.data_realizacao = timezone.now()
        self.save()

    def __str__(self):
        return self.atividade.nome

class Humor(models.Model):
    nome = models.CharField(max_length=30)
    nivel = models.CharField(max_length=1, default=None) #1 pra pior - 5 pra melhor
    data_criacao = models.DateTimeField(default=timezone.now)
    sensacoes = models.ManyToManyField('Sensacao', default=None)
    realizacoes = models.ManyToManyField('Realizacao', default=None)
    # data_ultima_utilizacao = models.DateTimeField(blank=True, null=True) #

    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome




class Sensacao(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    # data_ultima_utilizacao = models.DateTimeField(blank=True, null=True) #

    def cadastrar(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome


