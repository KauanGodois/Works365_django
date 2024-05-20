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