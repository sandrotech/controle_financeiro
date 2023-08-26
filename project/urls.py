from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from controle_financeiro.views import RegistroViewSet
from controle_visual import views
router = DefaultRouter()
router.register(r'registros', RegistroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('telaInicial/', views.home , name="home"),
]
