from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

# Create your models here.

class Game(models.Model):
	rencontre = models.CharField(max_length=255)
	league = models.ForeignKey('league.League', on_delete=models.CASCADE, related_name='League')
	adversaire = models.ForeignKey('Adversaire', on_delete=models.CASCADE, related_name='Adversaire')
	stade = models.CharField(max_length=255)
	date_start = models.DateTimeField()
	has_played= models.BooleanField(default=False)
	our_score = models.PositiveIntegerField()
	them_score = models.PositiveIntegerField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Match'
		verbose_name_plural = 'Matchs'

	def __str__(self):
		return str(self.adversaire)

class Adversaire(models.Model):
	equipe = models.CharField(max_length=255)
	logo = models.ImageField(upload_to = 'static/images/aversaires-logo/',null=True, blank=True)
	nationnalite = models.CharField(max_length=255)
	stade = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Adversaire'
		verbose_name_plural = 'Adversaires'

	def __str__(self):
		return str(self.equipe)