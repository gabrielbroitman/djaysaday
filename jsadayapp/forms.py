from django import forms

from .models import Atividade
from .models import Humor
from .models import Realizacao

class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Atividade
        fields = ('nome', 'descricao', 'tipoAtividade')
        
class RealizacaoForm(forms.ModelForm):

    class Meta:
        model = Realizacao
        fields = ('atividade', 'descricao', 'data_realizacao')
                
        
class HumorForm(forms.ModelForm):

    class Meta:
        model = Humor
        fields = ('nome', 'nivel', 'sensacoes', 'realizacoes')
        
