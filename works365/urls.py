from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register_servico/', views.register_servico, name='register_servico'),
    path('servico_cadastrado/', views.visualizar_servico, name='servico_cadastrado'),
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register_usuario/', views.register_usuario, name='register_usuario'),
    path('register_profissional/', views.register_profissional, name='register_profissional'),
]