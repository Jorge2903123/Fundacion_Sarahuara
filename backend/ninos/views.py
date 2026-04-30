from rest_framework.generics import ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from .models import Nino
from .serializers import NinoSerializer
from usuarios.views import get_usuario_desde_token

class ListaNinosView(ListAPIView):
    serializer_class = NinoSerializer

    def get_queryset(self):
        usuario, error = get_usuario_desde_token(self.request)
        if error:
            raise AuthenticationFailed('Token inválido o no proporcionado.')
        return Nino.objects.filter(activo=True).select_related('escuela', 'tutor').order_by('nombre')
