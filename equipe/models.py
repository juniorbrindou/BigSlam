from django.db import models

# Create your models here.

class Equipe(models.Model):
	libelle = models.CharField(max_length=255)
	nationnalite = models.CharField(max_length=255)
	stade = models.CharField(max_length=255)
	coach = models.CharField(max_length=255)

	class Meta:
		verbose_name = 'Equipe'
		verbose_name_plural = 'Equipes'
