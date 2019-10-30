from django.db import models
from django.conf import settings
from django.utils import timezone

NIVEL = [
    ('-2', 'Muito negativo'),
    ('-1', 'Negativo'),
    ('0', 'Neutro'),
    ('1', 'Positivo'),
    ('2', 'Muito positivo'),
]

TIPO_ATIVIDADE = [
    ('F', 'Física'),
    ('S', 'Substância'),
    ('A', 'Alimentação'),
    ('O', 'Outro'),
]


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
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    tipoAtividade = models.ForeignKey(
        'TipoAtividade', on_delete=models.CASCADE, default=None)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome


class Realizacao(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    atividade = models.ForeignKey(
        'Atividade', on_delete=models.CASCADE, default=None, related_name='realizacao_atividade')
    descricao = models.TextField()
    data_realizacao = models.DateTimeField(default=timezone.now)
    # data_ultima_utilizacao = models.DateTimeField(blank=True, null=True) #

    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.descricao


class Humor(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    # -2 pra pior +2 pra melhor
    nivel = models.CharField(max_length=1, choices=NIVEL, default=0,)
    data_criacao = models.DateTimeField(default=timezone.now)
    sensacoes = models.ManyToManyField(
        'Sensacao', related_name='humores')
    
    realizacoes = models.ManyToManyField('Realizacao', default=None)
    descricao = models.TextField(blank=True, default='')
    # data_ultima_utilizacao = models.DateTimeField(blank=True, null=True) #

    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome


class Sensacao(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    # -2 pra pior +2 pra melhor
    nivel = models.CharField(max_length=1, choices=NIVEL, default=0,)
    descricao = models.TextField(null=True, default='')
    data_criacao = models.DateTimeField(default=timezone.now)
    # data_ultima_utilizacao = models.DateTimeField(blank=True, null=True) #

    def cadastrar(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
