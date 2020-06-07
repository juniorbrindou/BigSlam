from django.contrib import admin
from league import models

# Register your models here.

class LeagueAdmin(admin.ModelAdmin):
	list_display = (
	'libelle',
	'pays',
	'date_add',
	'date_upd',
	)

	list_filter = (
	'pays',
	)

	search_fields = (
	'libelle',
	)

	list_per_page = 10
	date_hierarchy = 'date_add'

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'libelle',
				'pays',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.League, LeagueAdmin)