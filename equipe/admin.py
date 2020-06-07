from django.contrib import admin
from equipe import models 

# Register your models here.

class EquipeAdmin(admin.ModelAdmin):
	list_display = (
	'libelle',
	'nationnalite',
	'stade',
	'coach',
	)

	list_filter = (
	'nationnalite',
	)

	search_fields = (
	'nationnalite',
	)

	list_per_page = 10

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'libelle',
				'nationnalite',
				'stade',
				'coach',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Equipe, EquipeAdmin)