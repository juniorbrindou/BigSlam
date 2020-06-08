from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Equipe(models.Model):
	libelle = models.CharField(max_length=255)
	nationnalite = models.CharField(max_length=255)
	logo = models.ImageField(upload_to = 'static/images/logos/',null=True, blank=True)
	stade = models.CharField(max_length=255)
	coach = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Equipe'
		verbose_name_plural = 'Equipe'

	def __str__(self):
		return str(self.libelle)