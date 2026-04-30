from django.db import models

class Usuario(models.Model):
    nombre_usuario  = models.CharField(max_length=100, unique=True)
    nombre_completo = models.CharField(max_length=200, blank=True, null=True)
    contrasena      = models.CharField(max_length=64)
    activo          = models.IntegerField(default=1)
    fecha_registro  = models.DateTimeField(auto_now_add=True)
    rol_id          = models.IntegerField(default=1)

    class Meta:
        db_table = 'usuarios_usuario'  # apunta a la tabla que ya existe            # Django NO toca esta tabla

    def __str__(self):
        return self.nombre_usuario