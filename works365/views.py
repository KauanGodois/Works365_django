from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Professional, Usuario, ServicoUsuario

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
            senha=senha  
        )
        professional.save()
        return redirect('home')  
    return render(request, 'pages/profissional.html')

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
            return JsonResponse({'success': False, 'errors': 'Senhas não coincidem!'})

        # Verificar se o email já está registrado
        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'errors': 'Email já está registrado!'})

        # Criação do novo usuário
        usuario = Usuario(
            nome_completo=nome_completo,
            cpf=cpf,
            telefone=telefone,
            email=email,
            senha=senha  # Certifique-se de criptografar a senha em um caso real
        )
        usuario.save()
        return JsonResponse({'success': True})
        
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

