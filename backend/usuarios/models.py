from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    puede_editar = models.BooleanField(default=False)
    puede_eliminar = models.BooleanField(default=False)
    puede_exportar = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    nombre_usuario = models.CharField(max_length=100, unique=True)
    nombre_completo = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=256)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_usuario
