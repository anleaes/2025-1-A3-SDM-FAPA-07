"""
URL configuration for manutencaoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tipoDeServico/', include('tipoDeServico.urls', namespace='tipoDeServico')),
    path('servicos/', include('servicos.urls', namespace='servicos')),
    path('tecnico/', include('tecnico.urls', namespace='tecnico')),
    path('cliente/', include('cliente.urls', namespace='cliente')),
    path('endereco/', include('endereco.urls', namespace='endereco')),
    path('ordemServico/', include('ordemServico.urls', namespace='ordemServico')),
    path('ordemServicoItem/', include('ordemServicoItem.urls', namespace='ordemServicoItem')),
    path('equipamento/', include('equipamento.urls', namespace='equipamento')),
    path('token-autenticacao/', obtain_auth_token)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
