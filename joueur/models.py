from django.db import models
import datetime
from django.utils import timezone
# Create your models here.



class Joueur(models.Model):
	nom = models.CharField(max_length=255)
	nationnalite = models.CharField(max_length=255)
	position = models.ForeignKey('position', on_delete=models.CASCADE, related_name='Position_du_Joueur')
	photo = models.ImageField(upload_to = 'joueur/photos/',null=True, blank=True)
	maillot = models.PositiveIntegerField()
	masse = models.PositiveIntegerField()
	taille = models.PositiveIntegerField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Joueur'
		verbose_name_plural = 'Joueurs'

	def __str__(self):
		return str(self.nom)




class Position(models.Model):
	position = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Position Joeurs'
		verbose_name_plural = 'Positions Joueurs'

	def __str__(self):
		return str(self.position)