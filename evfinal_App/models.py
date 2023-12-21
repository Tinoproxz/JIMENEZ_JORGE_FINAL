from django.db import models
from django.core import validators

# Create your models here.
class Instituciones(models.Model):
    id_insti = models.IntegerField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre Institucion",max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    direccion = models.CharField(max_length=50)

class Inscritos(models.Model):
    ESTADOS=[('RESERVADO', 'Reservado'),('COMPLETADA', 'Completada'),('ANULADA','Anulada'),('NO ASISTEN','No Asisten')]
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre Inscrito",max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    telefono = models.CharField(max_length=12,validators=[validators.MaxLengthValidator(12), validators.MinLengthValidator(9)])
    fecha_inscri = models.DateField(verbose_name="Fecha Inscripcion", auto_now_add=True)
    id_institucion = models.ForeignKey(Instituciones, on_delete=models.PROTECT, null=True)
    hora_inscri = models.TimeField(verbose_name="Hora Inscripcion", auto_now_add=True) 
    estado = models.CharField(max_length=15,choices=ESTADOS)
    observacion = models.CharField(max_length=250)
    