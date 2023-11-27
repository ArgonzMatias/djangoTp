from django.db import models


# Create your models here.
class Comunidad(models.Model):
    class Meta:
        db_table = "comunidad"
    nombre = models.CharField(max_length=200)
class Miembro(models.Model):
    class Meta:
        db_table = "miembro"
    comunidad_id = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
class Incidente(models.Model):
    class Meta:
        db_table = "incidente"

    detalle = models.CharField(max_length=200)
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    miembro_id = models.ForeignKey(Miembro, on_delete=models.CASCADE)

