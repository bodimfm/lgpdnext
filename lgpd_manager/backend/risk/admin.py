from django.contrib import admin
from .models import RiskCategory, Risk, MitigationMeasure

admin.site.register(RiskCategory)
admin.site.register(Risk)
admin.site.register(MitigationMeasure)