from django.contrib import admin
from joueur import models
# Register your models here.

class JoueurAdmin(admin.ModelAdmin):
	list_display = (
	'nom',
	'maillot',
	'nationnalite',
	'position',
	'masse',
	'taille',
	)

	list_filter = (
	'position',
	'nationnalite',
	'masse',
	'taille',
	)

	search_fields = (
	'nom',
	)

	list_per_page = 10

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'nom',
				'nationnalite',
				'position',
				'maillot',
				'masse',
				'taille',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Joueur, JoueurAdmin)