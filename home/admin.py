from django.contrib import admin
from home import models
# Register your models here.

class HeaderAdmin(admin.ModelAdmin):
	list_display = (
	'email',
	'telephone',
	'date_add',
	'date_upd',
	)

	list_per_page = 10

	fieldsets = [
		('Information de contact',{
			'fields':[
				'email',
				'telephone',
			]
		}),
	]



class FooterAdmin(admin.ModelAdmin):
	list_display = (
	'geolocation',
	'slmall_presentation',
	'date_add',
	'date_upd',
	)

	list_per_page = 10
	date_hierarchy = 'date_add'

	fieldsets = [
		('Information de Pied de page',{
			'fields':[
				'geolocation',
				'slmall_presentation',
			]
		}),
	]

def _register(model, admin_class):
	admin.site.register(model, admin_class)

_register(models.Header, HeaderAdmin)
_register(models.Footer, FooterAdmin)