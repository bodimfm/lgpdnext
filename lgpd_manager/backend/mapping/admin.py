from django.contrib import admin
from .models import DataCategory, DataElement, Department, ProcessingActivity

admin.site.register(DataCategory)
admin.site.register(DataElement)
admin.site.register(Department)
admin.site.register(ProcessingActivity)