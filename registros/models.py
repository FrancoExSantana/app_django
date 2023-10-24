from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class inscripciones(models.Model):
    ANALISTA_PRIMERO = 'Primero de Analista De Sistemas'
    ANALISTA_SEGUNDO = 'Segundo de Analista De Sistemas'
    ANALISTA_TERCERO = 'Tercero de Analista De Sistemas'
    INFRAESTRUCTURA_PRIMERO = 'Primero de Infraestructura y Redes'
    INFRAESTRUCTURA_SEGUNDO = 'Segundo de Infraestructura y Redes'
    INFRAESTRUCTURA_TERCERO = 'Tercero de Infraestructura y Redes'
    COMERCIALIZACION_PRIMERO = 'Primero de Comercializacion'
    COMERCIALIZACION_SEGUNDO = 'Segundo de Comercializacion'
    COMERCIALIZACION_TERCERO = 'Tercero de Comercializacion'
    DISEÑO_PRIMERO = 'Primero de Diseño Grafico'
    DISEÑO_SEGUNDO = 'Segundo de Diseño Grafico'
    DISEÑO_TERCERO = 'Tercero de Diseño Grafico'
    CAREER_CHOICES = [
        (ANALISTA_PRIMERO, 'Primero de Analista De Sistemas'),
        (ANALISTA_SEGUNDO, 'Segundo de Analista De Sistemas'),
        (ANALISTA_TERCERO, 'Tercero de Analista De Sistemas'),
        (INFRAESTRUCTURA_PRIMERO, 'Primero de Infraestructura y Redes'),
        (INFRAESTRUCTURA_SEGUNDO, 'Segundo de Infraestructura y Redes'),
        (INFRAESTRUCTURA_TERCERO, 'Tercero de Infraestructura y Redes'),
        (COMERCIALIZACION_PRIMERO, 'Primero de Comercializacion'),
        (COMERCIALIZACION_SEGUNDO, 'Segundo de Comercializacion'),
        (COMERCIALIZACION_TERCERO, 'Tercero de Comercializacion'),
        (DISEÑO_PRIMERO, 'Primero de Diseño Grafico'),
        (DISEÑO_SEGUNDO, 'Segundo de Diseño Grafico'),
        (DISEÑO_TERCERO, 'Tercero de Diseño Grafico'),
    ]
    carrera = models.CharField(max_length=50, choices=CAREER_CHOICES)
    subject1_primero_analista = models.BooleanField(default=False)
    subject2_primero_analista = models.BooleanField(default=False)
    subject3_primero_analista = models.BooleanField(default=False)
    subject1_segundo_analista = models.BooleanField(default=False)
    subject2_segundo_analista = models.BooleanField(default=False)
    subject3_segundo_analista = models.BooleanField(default=False)
    subject1_tercero_analista = models.BooleanField(default=False)
    subject2_tercero_analista = models.BooleanField(default=False)
    subject3_tercero_analista = models.BooleanField(default=False)
    subject1_primero_infraestructura = models.BooleanField(default=False)
    subject2_primero_infraestructura = models.BooleanField(default=False)
    subject3_primero_infraestructura = models.BooleanField(default=False)
    subject1_segundo_infraestructura = models.BooleanField(default=False)
    subject2_segundo_infraestructura = models.BooleanField(default=False)
    subject3_segundo_infraestructura = models.BooleanField(default=False)
    subject1_tercero_infraestructura = models.BooleanField(default=False)
    subject2_tercero_infraestructura = models.BooleanField(default=False)
    subject3_tercero_infraestructura = models.BooleanField(default=False)
    subject1_primero_comercializacion = models.BooleanField(default=False)
    subject2_primero_comercializacion = models.BooleanField(default=False)
    subject3_primero_comercializacion = models.BooleanField(default=False)
    subject1_segundo_comercializacion = models.BooleanField(default=False)
    subject3_segundo_comercializacion = models.BooleanField(default=False)
    subject1_tercero_comercializacion = models.BooleanField(default=False)
    subject2_tercero_comercializacion = models.BooleanField(default=False)
    subject3_tercero_comercializacion = models.BooleanField(default=False)
    subject1_primero_diseno = models.BooleanField(default=False)
    subject2_primero_diseno = models.BooleanField(default=False)
    subject3_primero_diseno = models.BooleanField(default=False)
    subject1_segundo_diseno = models.BooleanField(default=False)
    subject2_segundo_diseno = models.BooleanField(default=False)
    subject3_segundo_diseno = models.BooleanField(default=False)
    subject1_tercero_diseno = models.BooleanField(default=False)
    subject2_tercero_diseno = models.BooleanField(default=False)
    subject3_tercero_diseno = models.BooleanField(default=False)
