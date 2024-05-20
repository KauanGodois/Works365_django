from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Professional, Usuario

def home(request):
    return render(request, 'pages/home.html')

def register_professional(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('username')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        areas_atuacao = request.POST.get('categorias')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validações básicas
        if senha != confirmar_senha:
            return HttpResponse("Senhas não coincidem!")

        # Criação do novo profissional
        professional = Professional(
            nome_completo=nome_completo,
            cpf=cpf,
            telefone=telefone,
            email=email,
            areas_atuacao=areas_atuacao,
            senha=senha  # Lembre-se de usar um hash de senha em um cenário real
        )
        professional.save()
        return redirect('success_page')  # Certifique-se de definir essa URL no seu urls.py
    return render(request, 'profissional.html')

def register_usuario(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('username')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validações básicas
        if senha != confirmar_senha:
            return HttpResponse("Senhas não coincidem!")

        # Criação do novo usuário
        usuario = Usuario(
            nome_completo=nome_completo,
            cpf=cpf,
            telefone=telefone,
            email=email,
            senha=senha  # Lembre-se de usar um hash de senha em um cenário real
        )
        usuario.save()
        return redirect('success_page')  # Certifique-se de definir essa URL no seu urls.py
    return render(request, 'usuario.html')

def success_page(request):
    return HttpResponse("Cadastro realizado com sucesso!")
