from django.urls import path, include
from rest_frameworks import routers
from . import views

app_name = 'endereco'

router = routers.DefaultRouter()
router.register('', views.EnderecoViewSet, basename='endereco')

urlpatterns = [
    path('', include(router.urls)),
]