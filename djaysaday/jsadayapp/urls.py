from django.urls import path, include
from django.contrib.auth.urls import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    path(r'^', include('django.contrib.auth.urls')),
    

    # Atividades
    #path('user/getuserlogado/<int:pk>', views.detalhe_user, name='detalhe_user'),
    #path('user/login/', views.login_user, name='login_user'),
    #path('user/logout/', views.logout_user, name='logout_user'),

    # Atividades
    path('atividade/listar/', views.lista_atividade, name='lista_atividade'),
    path('atividade/listar/rank', views.lista_atividade_rank, name='lista_atividade_rank'),
    path('atividade/<int:pk>/', views.detalhe_atividade, name='detalhe_atividade'),
    path('atividade/nova/', views.lista_atividade, name='nova_atividade'),
    path('atividade/<int:pk>/edit/',
         views.detalhe_atividade, name='edicao_atividade'),

    # Definições de Humor
    path('humor/<int:pk>/', views.detalhe_humor, name='detalhe_humor'),
    path('humor/listar', views.lista_humor, name='lista_humor'),
    path('humor/novo/', views.lista_humor, name='novo_humor'),
    path('humor/<int:pk>/edit/', views.detalhe_humor, name='edicao_humor'),
     path('sensacoes/listar', views.lista_sensacoes, name='lista_sensacoes'),

    # Realizações
    path('realizacao/listar', views.lista_realizacao, name='lista_realizacao'),
    path('realizacao/<int:pk>/', views.detalhe_realizacao,
         name='detalhe_realizacao'),
    path('realizacao/nova/', views.lista_realizacao, name='nova_realizacao'),
    path('realizacao/<int:pk>/edit/',
         views.detalhe_realizacao, name='edicao_realizacao'),

    # Add Django site authentication urls (for login, logout, password management)


]
