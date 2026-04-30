from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from ninos.models import Nino
from asistencia.models import Asistencia
from usuarios.views import get_usuario_desde_token

class DashboardMetricsView(APIView):
    def get(self, request):
        usuario, error = get_usuario_desde_token(request)
        if error:
            return error
        hoy = timezone.localdate()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        total_activos = Nino.objects.filter(activo=True).count()
        asistencias_hoy = Asistencia.objects.filter(fecha=hoy, asistio=True).count()
        comidas_hoy = Asistencia.objects.filter(fecha=hoy, asistio=True, recibio_comida=True).count()
        inasistencias_semana = Asistencia.objects.filter(fecha__range=[inicio_semana, hoy], asistio=False).count()
        historico = []
        for i in range(5, -1, -1):
            dia = hoy - timedelta(days=i)
            conteo = Asistencia.objects.filter(fecha=dia, asistio=True).count()
            historico.append({'fecha': dia.isoformat(), 'asistencias': conteo})
        return Response({'total_ninos_activos': total_activos, 'asistencia_hoy': asistencias_hoy, 'comidas_hoy': comidas_hoy, 'inasistencias_semana': inasistencias_semana, 'grafica_asistencia': historico}, status=status.HTTP_200_OK)
