# ...existing code...
from django.db import models
from core.models import Organization, User
from mapping.models import ProcessingActivity


class DocumentTemplate(models.Model):
    """Templates para documentos"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    
    DOCUMENT_TYPE_CHOICES = [
        ('privacy_notice', 'Aviso de Privacidade'),
        ('dpia', 'Relatório de Impacto'),
        ('consent_form', 'Formulário de Consentimento'),
        ('other', 'Outro'),
    ]
    
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_templates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='document_templates')
    
    def __str__(self):
        return self.name


class Document(models.Model):
    """Documentos gerados"""
    name = models.CharField(max_length=200)
    template = models.ForeignKey(DocumentTemplate, on_delete=models.SET_NULL, null=True, related_name='documents')
    content = models.TextField()
    related_activities = models.ManyToManyField(ProcessingActivity, related_name='documents')
    version = models.CharField(max_length=20)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='documents')
    
    def __str__(self):
        return self.name