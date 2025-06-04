from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'servicos'

router = routers.DefaultRouter()
router.register('', views.ServicoViewSet, basename='servico')

urlpatterns = [
    path('', include(router.urls) )
]