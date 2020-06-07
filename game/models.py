from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

# Create your models here.

class Game(models.Model):
	rencontre = models.CharField(max_length=255)
	league = models.ForeignKey('league.League', on_delete=models.CASCADE, related_name='League')
	equipes = models.ManyToManyField('equipe.Equipe')
	stade = models.CharField(max_length=255)
	date_start = models.DateTimeField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Rencontre (VS)'
		verbose_name_plural = 'Rencontres (VS)'

	def __str__(self):
		return str(self.rencontre)