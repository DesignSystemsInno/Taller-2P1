from django.db import models
# Create your models here.

class migrantes(models.Model):
    nombre_completo = models.CharField(max_length=30)
    pais_origen = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_migracion = models.DateField()
    documento = models.IntegerField()
    