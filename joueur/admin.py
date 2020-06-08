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
	'photo',
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
				'taille',
				'photo',
			]
		}),
	]



class PositionAdmin(admin.ModelAdmin):
	list_display = (
	'position',
	'date_add',
	'date_upd',
	)

	list_per_page = 10
	date_hierarchy = 'date_add'

	fieldsets = [
		('Creation de Joueur',{
			'fields':[
				'position',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Joueur, JoueurAdmin)
_register(models.Position, PositionAdmin)