# ...existing code...
from django.db import models
from core.models import Organization, User
from mapping.models import ProcessingActivity


class RiskCategory(models.Model):
    """Categorias de riscos"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='risk_categories')
    
    def __str__(self):
        return self.name


class Risk(models.Model):
    """Riscos identificados"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE, related_name='risks')
    processing_activity = models.ForeignKey(ProcessingActivity, on_delete=models.CASCADE, related_name='risks')
    
    PROBABILITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]
    
    IMPACT_CHOICES = [
        ('low', 'Baixo'),
        ('medium', 'Médio'),
        ('high', 'Alto'),
    ]
    
    probability = models.CharField(max_length=10, choices=PROBABILITY_CHOICES)
    impact = models.CharField(max_length=10, choices=IMPACT_CHOICES)
    
    @property
    def risk_level(self):
        """Calcula o nível de risco baseado na probabilidade e impacto"""
        probability_map = {'low': 1, 'medium': 2, 'high': 3}
        impact_map = {'low': 1, 'medium': 2, 'high': 3}
        
        risk_value = probability_map[self.probability] * impact_map[self.impact]
        
        if risk_value <= 2:
            return 'low'
        elif risk_value <= 6:
            return 'medium'
        else:
            return 'high'
    
    is_mitigated = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_risks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='risks')
    
    def __str__(self):
        return self.name


class MitigationMeasure(models.Model):
    """Medidas de mitigação para riscos"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='mitigation_measures')
    is_implemented = models.BooleanField(default=False)
    implementation_date = models.DateField(blank=True, null=True)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='responsible_measures')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_measures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='mitigation_measures')
    
    def __str__(self):
        return self.name