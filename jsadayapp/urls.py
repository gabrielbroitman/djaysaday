from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_atividade, name='lista_atividade'),
]