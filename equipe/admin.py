from django.contrib import admin
from equipe import models 

# Register your models here.

class EquipeAdmin(admin.ModelAdmin):
	list_display = (
	'libelle',
	'nationnalite',
	'stade',
	'coach',
	'date_add',
	'date_upd',
	)

	list_filter = (
	'nationnalite',
	)

	search_fields = (
	'nationnalite',
	)

	list_per_page = 10
	date_hierarchy = 'date_add'


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