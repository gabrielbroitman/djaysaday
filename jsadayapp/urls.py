from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_atividade, name='lista_atividade'),
    path('atividade/<int:pk>/', views.detalhe_atividade, name='detalhe_atividade'),
    path('atividade/nova/', views.nova_atividade, name='nova_atividade'),
    path('atividade/<int:pk>/edit/', views.edicao_atividade, name='edicao_atividade'),
]