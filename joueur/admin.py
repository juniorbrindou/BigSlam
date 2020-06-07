from django.contrib import admin
from joueur import models
# Register your models here.

class JoueurAdmin(admin.ModelAdmin):
	list_display = (
	'nom',
	'nationnalite',
	'position',
	)

	list_filter = (
	'position',
	'nationnalite',
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
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Joueur, JoueurAdmin)