from django import forms

from .models import Atividade
from .models import Realizacao

class AtividadeForm(forms.ModelForm):

    class Meta:
        model = Atividade
        fields = ('nome', 'descricao')
        
