from django.db import models
# Create your models here.


class Header(models.Model):
	email = models.CharField(max_length=255)
	telephone = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'En-Tête-Information'
		verbose_name_plural = 'En-Tête-Informations'

	def __str__(self):
		return str(self.email)




class Footer(models.Model):
	geolocation = models.CharField(max_length=255)
	slmall_presentation = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Pied-De-Page'
		verbose_name_plural = 'Pied-De-Pages'

	def __str__(self):
		return str(self.geolocation)