from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atividade/listar/', views.lista_atividade, name='lista_atividade'),
    path('atividade/<int:pk>/', views.detalhe_atividade, name='detalhe_atividade'),
    path('atividade/nova/', views.nova_atividade, name='nova_atividade'),
    path('atividade/<int:pk>/edit/', views.edicao_atividade, name='edicao_atividade'),
    path('humor/<int:pk>/', views.detalhe_humor, name='detalhe_humor'),
    path('humor/listar', views.lista_humor, name='lista_humor'),
    path('humor/novo/', views.novo_humor, name='novo_humor'),
    path('humor/<int:pk>/edit/', views.edicao_humor, name='edicao_humor'),
    path('realizacao/listar', views.lista_realizacao, name='lista_realizacao'),
    path('realizacao/<int:pk>/', views.detalhe_realizacao, name='detalhe_realizacao'),
    path('realizacao/novo/', views.nova_realizacao, name='nova_realizacao'),
    path('realizacao/<int:pk>/edit/', views.edicao_realizacao, name='edicao_realizacao'),
]