import hashlib
import json
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario


# ── Páginas HTML ──
class RegistroView(TemplateView):
    template_name = "login.html"

class LoginView(TemplateView):
    template_name = "logeo.html"


# ── API Login ──
@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(View):
    def post(self, request):
        try:
            print(">>> BODY RAW:", request.body)
            data           = json.loads(request.body)
            nombre_usuario = data.get('nombre_usuario')
            contrasena     = data.get('contrasena')

            contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

            # Buscar solo por nombre_usuario primero
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)

            # Comparar hash manualmente
            if usuario.contrasena != contrasena_hash:
                print(">>> Hash BD:    ", repr(usuario.contrasena))
                print(">>> Hash calc:  ", repr(contrasena_hash))
                return JsonResponse({'ok': False, 'error': 'Credenciales incorrectas'}, status=401)

            request.session['usuario_id']     = usuario.id
            request.session['nombre_usuario'] = usuario.nombre_usuario

            return JsonResponse({'ok': True})

        except Usuario.DoesNotExist:
            return JsonResponse({'ok': False, 'error': 'Usuario no encontrado'}, status=401)
        except Exception as e:
            return JsonResponse({'ok': False, 'error': str(e)}, status=500)

# ── API Registro ──
@method_decorator(csrf_exempt, name='dispatch')
class RegistroAPIView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            nombre_usuario  = data.get('nombre_usuario')
            nombre_completo = data.get('nombre')
            contrasena      = data.get('contrasena')

            if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
                return JsonResponse({'ok': False, 'error': 'El usuario ya existe'}, status=400)

            contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

            Usuario.objects.create(
                nombre_usuario  = nombre_usuario,
                nombre_completo = nombre_completo,
                contrasena      = contrasena_hash,
                activo          = 1,
                rol_id          = 1
            )

            return JsonResponse({'ok': True})

        except Exception as e:
            return JsonResponse({'ok': False, 'error': str(e)}, status=500)