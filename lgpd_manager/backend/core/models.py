# ...existing code...
from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    """Organização/empresa usando o sistema"""
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True, 
                           choices=[
                               ('micro', 'Microempresa'),
                               ('small', 'Empresa de Pequeno Porte'),
                               ('medium', 'Empresa de Médio Porte'),
                               ('large', 'Empresa de Grande Porte'),
                           ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    """Usuário do sistema com campos adicionais"""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name='users')
    position = models.CharField(max_length=100, blank=True, null=True)
    is_dpo = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username