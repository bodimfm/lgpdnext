from django.db import models
from core.models import Organization, User


class DataCategory(models.Model):
    """Categorias de dados pessoais"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_sensitive = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='data_categories')
    
    def __str__(self):
        return self.name


class DataElement(models.Model):
    """Elementos de dados específicos"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(DataCategory, on_delete=models.CASCADE, related_name='elements')
    retention_period = models.CharField(max_length=100, blank=True, null=True)
    is_collected_from_data_subject = models.BooleanField(default=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='data_elements')
    
    def __str__(self):
        return self.name


class Department(models.Model):
    """Departamentos da organização"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='departments')
    
    def __str__(self):
        return self.name


class ProcessingActivity(models.Model):
    """Atividades de tratamento de dados"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    departments = models.ManyToManyField(Department, related_name='processing_activities')
    data_elements = models.ManyToManyField(DataElement, related_name='processing_activities')
    purposes = models.TextField()
    
    LEGAL_BASIS_CHOICES = [
        ('consent', 'Consentimento'),
        ('legal_obligation', 'Obrigação Legal'),
        ('contract', 'Execução de Contrato'),
        ('legitimate_interest', 'Interesse Legítimo'),
        ('public_interest', 'Interesse Público'),
        ('vital_interest', 'Proteção da Vida'),
        ('research', 'Pesquisa'),
        ('credit_protection', 'Proteção ao Crédito'),
    ]
    
    legal_basis = models.CharField(max_length=50, choices=LEGAL_BASIS_CHOICES)
    legal_basis_details = models.TextField(blank=True, null=True)
    sharing_entities = models.TextField(blank=True, null=True)
    security_measures = models.TextField(blank=True, null=True)
    international_transfer = models.BooleanField(default=False)
    international_transfer_details = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_activities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='processing_activities')
    
    def __str__(self):
        return self.name