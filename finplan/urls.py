
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from financas.api import viewsets as financas_viewsets

route = routers.DefaultRouter()
route.register(r'categorias', financas_viewsets.CategoriaViewSet, basename='Categoria')
route.register(r'transacoes', financas_viewsets.TransacaoViewSet, basename='Transacao')
route.register(r'relatorios', financas_viewsets.RelatorioMensalViewSet, basename='RelatorioMensal')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls))
]
