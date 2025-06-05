from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'ordemServico'

router = routers.DefaultRouter()
router.register('', views.OrdemServicoViewSet, basename='ordemServico')

urlpatterns = [
    path('', include(router.urls)),
]