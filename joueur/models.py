from django.db import models

# Create your models here.



class Joueur(models.Model):
	nom = models.CharField(max_length=255)
	nationnalite = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	maillot = models.PositiveIntegerField()

	class Meta:
		verbose_name = 'Joueur'
		verbose_name_plural = 'Joueurs'

	def __str__(self):
		return str(self.nom)