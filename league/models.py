from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class League(models.Model):
	libelle = models.CharField(max_length=255)
	pays = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'League'
		verbose_name_plural = 'Leagues'

	def __str__(self):
		return str(self.libelle)
