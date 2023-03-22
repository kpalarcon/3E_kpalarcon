from django.db import models
from django.db.models import ForeignKey
from autenticacion.models import Usuario

########################################################################################################################

class Equipo(models.Model):
    nombreequipo = models.CharField(max_length=255)
    estado = models.IntegerField(default=1)

    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_creacion")
    usuario_modificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_modificacion")

    class Meta:
        db_table = "equipo"
        verbose_name = "equipo"
        verbose_name_plural = "equipos"
        ordering = ['fecha_creacion', 'nombreequipo']

    def __str__(self):
        return '{}'.format(self.nombreequipo)

########################################################################################################################

class Trofeo(models.Model):
    nombretrofeo = models.CharField(max_length=255)
    estado = models.IntegerField(default=1)
    tipo = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    usuario_creacion = models.CharField(max_length=15, default="sistemas")
    usuario_modificacion = models.CharField(max_length=15, default="sistemas")

    class Meta:
        db_table = "trofeo"
        verbose_name = "trofeo"
        verbose_name_plural = "trofeos"
        ordering = ['fecha_creacion', 'nombretrofeo']

    def __str__(self):
        return '{}'.format(self.nombretrofeo)

########################################################################################################################

class Torneo(models.Model):
    nombretorneo = models.CharField(max_length=255)
    equipo = ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
    trofeo = ForeignKey(Trofeo, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.IntegerField(default=1)

    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    usuario_creacion = models.CharField(max_length=15, default="sistemas")
    usuario_modificacion = models.CharField(max_length=15, default="sistemas")

    class Meta:
        db_table = "torneo"
        verbose_name = "torneo"
        verbose_name_plural = "torneos"
        ordering = ['fecha_creacion', 'nombretorneo']

    def __str__(self):
        return '{}'.format(self.nombretorneo)
######################