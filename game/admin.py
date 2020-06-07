from django.contrib import admin
from game import models

# Register your models here.


class GameAdmin(admin.ModelAdmin):
	list_display = (
	'rencontre',
	'league',
	# 'equipe1',
	# 'equipe2',
	'stade',
	'date_start',
	'date_add',
	'date_upd',
	)

	list_filter = (
	'league',
	'date_start',
	)

	search_fields = (
	# 'equipe1',
	# 'equipe2',
	)

	list_per_page = 10
	date_hierarchy = 'date_add'

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'rencontre',
				'league',
				# 'equipe1',
				# 'equipe2',
				'stade',
				'date_start',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Game, GameAdmin)