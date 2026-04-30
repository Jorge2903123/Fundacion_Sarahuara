from django.db import models

class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    turno = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Tutor(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Nino(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.PROTECT)
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=50, unique=True)
    codigo_qr = models.CharField(max_length=200, blank=True)
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
