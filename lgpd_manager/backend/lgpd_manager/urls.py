"""
Configurações de URL para o projeto LGPD Manager.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Endpoints de autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Incluir URLs dos apps
    # path('api/core/', include('core.urls')),
    # path('api/mapping/', include('mapping.urls')),
    # path('api/risk/', include('risk.urls')),
    # path('api/document/', include('document.urls')),
    # path('api/dashboard/', include('dashboard.urls')),
]

# Adiciona URLs para arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)