from django.contrib import admin
from django.urls import path
from usuarios.views import LoginView
from ninos.views import ListaNinosView
from asistencia.views import RegistroAsistenciaView
from reportes.views import DashboardMetricsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/ninos/', ListaNinosView.as_view(), name='api-ninos'),
    path('api/asistencia/', RegistroAsistenciaView.as_view(), name='api-asistencia'),
    path('api/reportes/', DashboardMetricsView.as_view(), name='api-reportes'),
]
