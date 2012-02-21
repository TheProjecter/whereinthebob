from bob.models import *
from django.contrib import admin

class FloorAdmin(admin.ModelAdmin):
	readonly_fields = ['date_created', 'date_updated', 'rating']
	fields =  ['description', 'level', 'date_created', 'date_updated', 'rating']
	list_display = ( 'description', 'level', 'date_created', 'date_updated', 'rating')
	list_filter = ['date_created']

class CommentAdmin(admin.ModelAdmin):
	readonly_fields = ['date_created', 'date_updated']
	fields = [ 'comment' , 'date_created','date_updated']
	list_display = ('comment_id' , 'comment' , 'guid' , 'date_created','date_updated')

class RoomAdmin(admin.ModelAdmin):
	readonly_fields = ['rating']
	fields = [ 'floor_id','type_id', 'description','rating']
	list_display = ('room_id','floor_id','type_id','description','rating')
	list_filter = ['floor_id']

class RoomNameAdmin(admin.ModelAdmin):
	fields = ['room_id', 'name']
	list_display = ('room_id','name')
	list_filter = ['room_id']
	
class RoomTypeAdmin(admin.ModelAdmin):
	fields = ['type_id', 'type_name']
	list_display = ('type_id', 'type_name') 	
	
	
admin.site.register(Floor, FloorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Room_Name, RoomNameAdmin)
admin.site.register(Room_Type, RoomTypeAdmin)
