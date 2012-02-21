from bob.models import Floor
from django.contrib import admin

class FloorAdmin(admin.ModelAdmin):
	readonly_fields = ['date_created', 'date_updated', 'rating']
	fields = ['floor_id', 'description', 'level', 'date_created', 'date_updated', 'rating']

admin.site.register(Floor, FloorAdmin)