from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import ServicoUsuario, Usuario, Profissional
from django.contrib import auth

def home(request):
    return render(request, 'pages/home.html')

def register_profissional(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('username')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        areas_atuacao = request.POST.get('categorias')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validações básicas
        if senha != confirmar_senha:
            return messages.success("Senhas não coincidem!")

        # Criação do novo profissional
        profissional = Profissional(
            nome_completo=nome_completo,
            telefone=telefone,
            email=email,
            areas_atuacao=areas_atuacao,
            senha=senha  
        )
        profissional.save()
        return redirect('home')  
    
    return render(request, 'pages/profissional.html')

def register_usuario(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('username')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Criação do novo usuário
        usuario = Usuario(
            nome_completo=nome_completo,
            telefone=telefone,
            email=email,
            senha=senha  # Certifique-se de criptografar a senha em um caso real
        )
        usuario.save()
        return redirect('login')
        
    return render(request, 'pages/usuario.html')

def register_servico(request):
    if request.method == 'POST':
        servico = request.POST.get('servico')
        local = request.POST.get('local')
        categoria = request.POST.get('categoria')

        # Criação do novo serviço
        servico_usuario = ServicoUsuario(
            servico=servico,
            local=local,
            categoria=categoria
        )
        servico_usuario.save()
        return redirect('success_servico_page')  
    return render(request, 'pages/servico_usuario.html')


def visualizar_servico(request):
    return render(request, 'pages/servicos_cadastrados.html')


def login(request):
    return render(request, 'pages/login.html')

def quem_somos(request):
    return render(request, 'pages/quem_somos.html')

def login(request):

    if request.method == "POST":
        usuario = request.POST['username']
        senha = request.POST['senha']

        verificarUsuario = auth.authenticate(request, username=usuario, senha=senha)

        if verificarUsuario != None:
            auth.login(request, verificarUsuario)
            return redirect('servico_cadastrado')
        else:
            return redirect('login')
        
    else:
        return render(request, 'pages/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')
