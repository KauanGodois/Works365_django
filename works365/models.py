from django.db import models

class Professional(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    areas_atuacao = models.TextField()
    senha = models.CharField(max_length=255)  # Use um hash de senha em um cenário real

    def __str__(self):
        return self.nome_completo

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=255)  # Use um hash de senha em um cenário real

    def __str__(self):
        return self.nome_completo
   
    
class ServicoUsuario(models.Model):
    SERVICO_CATEGORIAS = [
        ('1', 'Limpeza'),
        ('2', 'Reparos'),
        ('3', 'Consultoria'),
        ('4', 'Outros'),
    ]

    servico = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    categoria = models.CharField(max_length=1, choices=SERVICO_CATEGORIAS)

    def __str__(self):
        return self.servico