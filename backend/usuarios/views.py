import hashlib
import secrets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario

_tokens = {}

def _hash_password(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()

def get_usuario_desde_token(request):
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Token '):
        return None, Response({'error': 'Token no proporcionado.'}, status=status.HTTP_401_UNAUTHORIZED)
    token = auth_header.split(' ', 1)[1].strip()
    usuario_id = _tokens.get(token)
    if usuario_id is None:
        return None, Response({'error': 'Token inválido o sesión expirada.'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        usuario = Usuario.objects.select_related('rol').get(id=usuario_id, activo=True)
    except Usuario.DoesNotExist:
        return None, Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_401_UNAUTHORIZED)
    return usuario, None

class LoginView(APIView):
    def post(self, request):
        nombre_usuario = request.data.get('nombre_usuario', '').strip()
        contrasena = request.data.get('contrasena', '')
        if not nombre_usuario or not contrasena:
            return Response({'error': 'nombre_usuario y contrasena son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = Usuario.objects.select_related('rol').get(nombre_usuario=nombre_usuario, activo=True)
        except Usuario.DoesNotExist:
            return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        if usuario.contrasena != _hash_password(contrasena):
            return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        token = secrets.token_hex(32)
        _tokens[token] = usuario.id
        return Response({
            'token': token,
            'nombre_completo': usuario.nombre_completo,
            'rol': usuario.rol.nombre,
            'puede_editar': usuario.rol.puede_editar,
            'puede_eliminar': usuario.rol.puede_eliminar,
            'puede_exportar': usuario.rol.puede_exportar,
        }, status=status.HTTP_200_OK)
