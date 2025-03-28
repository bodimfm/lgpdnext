# ...existing code...
from django.db import models
from core.models import Organization, User

class DashboardSettings(models.Model):
    """Configurações personalizadas para o dashboard"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dashboard_settings')
    show_activities = models.BooleanField(default=True)
    show_risks = models.BooleanField(default=True)
    show_documents = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dashboard Settings for {self.user.username}"