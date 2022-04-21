from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings

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
    

class Sortie(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE)
    
    date = models.DateField()
    duree = models.TimeField()
    nombrePersonnes = models.IntegerField("Nombre de personnes")
    
    DEBUTANTS = 'DEB'
    EXPERIMENTES = 'EXP'
    MIXTES = 'MIX'
    
    EXP_CHOICES = [
        (DEBUTANTS, 'Debutants'),
        (EXPERIMENTES, 'Experimentes'),
        (MIXTES, 'Mixtes'),
    ]
    
    experience = models.CharField(max_length=30, choices=EXP_CHOICES)
    
    BONNE = 'BON'
    MOYENNE = 'MOY'
    MAUVAISE = 'MAL'
    
    METEO_CHOICES = [
        (BONNE, 'Bonne'),
        (MOYENNE, 'Moyenne'),
        (MAUVAISE, 'Mauvaise'),
    ]    
    
    meteo = models.CharField(max_length=20, choices=METEO_CHOICES)
    
    difficulte = models.IntegerField(validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=5)])
    
