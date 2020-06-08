from django.contrib import admin
from game import models

# Register your models here.


class GameAdmin(admin.ModelAdmin):
	list_display = (
	'rencontre',
	'league',
	'adversaire',
	'stade',
	'date_start',
	'has_played',
	'our_score',
	'them_score',
	'date_add',
	'date_upd',
	)

	list_filter = (
	'league',
	'date_start',
	'has_played',
	)

	search_fields = (
	'equipe1',
	)

	list_per_page = 10
	date_hierarchy = 'date_add'

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'rencontre',
				'league',
				'adversaire',
				'stade',
				'has_played',
				'our_score',
				'them_score',
				'date_start',
			]
		}),
	]



class AdversaireAdmin(admin.ModelAdmin):
	list_display = (
	'equipe',
	'nationnalite',
	'stade',
	'logo',
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
				'equipe',
				'nationnalite',
				'stade',
				'logo',
			]
		}),
	]



def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Game, GameAdmin)
_register(models.Adversaire, AdversaireAdmin)