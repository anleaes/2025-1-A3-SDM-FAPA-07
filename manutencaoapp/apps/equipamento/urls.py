from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'equipamento'

router = routers.DefaultRouter()
router.register('', views.EquipamentoViewSet, basename='equipamento')

urlpatterns = [
    path('', include(router.urls)),
]