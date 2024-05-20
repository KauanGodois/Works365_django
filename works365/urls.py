from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register_professional/', views.register_professional, name='register_professional'),
    path('register_usuario/', views.register_usuario, name='register_usuario'),
    path('success/', views.success_page, name='success_page'),
]