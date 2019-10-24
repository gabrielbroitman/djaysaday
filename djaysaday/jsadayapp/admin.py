from django.contrib import admin
from .models import Atividade
from .models import Realizacao
from .models import Humor
from .models import TipoAtividade
from .models import Sensacao


# Register your models here.
admin.site.register(TipoAtividade)
admin.site.register(Sensacao)
admin.site.register(Humor)
admin.site.register(Atividade)
admin.site.register(Realizacao)