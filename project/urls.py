from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from controle_financeiro.views import RegistroViewSet

router = DefaultRouter()
router.register(r'registros', RegistroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('gerenciamento/', include(controle_visual.urls)),
]
