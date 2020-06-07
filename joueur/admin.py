from django.contrib import admin
from joueur import models
# Register your models here.

class JoueurAdmin(admin.ModelAdmin):
	list_display = (
	'nom',
	'maillot',
	'equipe',
	'nationnalite',
	'position',
	'masse',
	'taille',
	'date_add',
	'date_upd',
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
	date_hierarchy = 'date_add'

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'nom',
				'nationnalite',
				'position',
				'maillot',
				'masse',
				'equipe'
				'taille',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Joueur, JoueurAdmin)