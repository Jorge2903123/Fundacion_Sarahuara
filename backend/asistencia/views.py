from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Asistencia
from ninos.models import Nino
from usuarios.views import get_usuario_desde_token

class RegistroAsistenciaView(APIView):
    def post(self, request):
        usuario, error = get_usuario_desde_token(request)
        if error:
            return error
        nino_id = request.data.get('id_nino')
        comida = request.data.get('recibio_comida', False)
        if nino_id is None:
            return Response({'error': 'El campo id_nino es requerido.'}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(comida, bool):
            return Response({'error': 'recibio_comida debe ser true o false.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            nino = Nino.objects.get(id=nino_id, activo=True)
        except Nino.DoesNotExist:
            return Response({'error': 'Niño no encontrado o inactivo.'}, status=status.HTTP_404_NOT_FOUND)
        hoy = timezone.localdate()
        asistencia, creado = Asistencia.objects.update_or_create(
            nino=nino, fecha=hoy,
            defaults={'usuario': usuario, 'asistio': True, 'recibio_comida': comida, 'sincronizado': False}
        )
        mensaje = 'Asistencia registrada correctamente.' if creado else 'Asistencia actualizada correctamente.'
        return Response({'mensaje': mensaje, 'asistencia': {'id': asistencia.id, 'nino': nino.nombre, 'fecha': asistencia.fecha.isoformat(), 'asistio': asistencia.asistio, 'recibio_comida': asistencia.recibio_comida}}, status=status.HTTP_200_OK)
