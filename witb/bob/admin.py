from bob.models import *
from django.contrib import admin

class FloorAdmin(admin.ModelAdmin):
	readonly_fields = ['date_created', 'date_updated', 'rating']
	fields = ['floor_id', 'description', 'level', 'date_created', 'date_updated', 'rating']

class CommentAdmin(admin.ModelAdmin):
	readonly_fields = ['date_created', 'date_updated']
	fields = ['comment_id' , 'comment' , 'guid' , 'date_created','date_updated']
	
admin.site.register(Floor, FloorAdmin)
admin.site.register( Comment, CommentAdmin)
admin.site.register(Room)
admin.site.register(Room_Name)
admin.site.register(Room_Type)