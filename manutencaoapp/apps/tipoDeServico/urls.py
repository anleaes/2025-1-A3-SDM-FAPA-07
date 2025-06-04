from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tipoDeServico'

router = routers.DefaultRouter()
router.register('', views.TipoDeServicoViewSet, basename='tipoDeServico')

urlpatterns = [
    path('', include(router.urls)),
]