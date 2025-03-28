from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Organization, User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_dpo', 'organization')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('organization', 'position', 'is_dpo', 'phone')}),
    )

admin.site.register(Organization)
admin.site.register(User, CustomUserAdmin)