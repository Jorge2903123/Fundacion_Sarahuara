from django.db import models
from ninos.models import Nino
from usuarios.models import Usuario

class Asistencia(models.Model):
    nino = models.ForeignKey(Nino, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha = models.DateField()
    asistio = models.BooleanField(default=True)
    recibio_comida = models.BooleanField(default=False)
    sincronizado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nino.nombre} - {self.fecha}"
