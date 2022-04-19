from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Itineraire(models.Model):
    titre = models.CharField(max_length=200)
    pointDepart = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    altitudeDepart = models.FloatField('Altitude de depart (m)')
    altitudeMin = models.FloatField('Altitude minimale (m)')
    altitudeMax = models.FloatField('Altitude maximale (m)')
    denivPosCum = models.FloatField('Dénivelé Positif Cumulé (m)')
    denivNegCum = models.FloatField('Dénivelé Negatif Cumulé (m)')
    duree = models.TimeField()
    difficulte = models.IntegerField(validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=5)])