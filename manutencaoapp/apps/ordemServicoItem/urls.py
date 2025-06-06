from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ordem_servico_item'

router = routers.DefaultRouter()
router.register('', views.OrdemServicoItemViewSet, basename='ordemservicoitem')

urlpatterns = [
    path('', include(router.urls)),
]