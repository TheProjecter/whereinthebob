from django.db import models
import uuid
class Floor(models.Model):
	floor_id = models.AutoField(primary_key=True)
	description = models.CharField(max_length=200)
	date_created = models.DateTimeField(editable=False, auto_now_add=True)
	date_updated = models.DateTimeField(null=True, editable=False, auto_now=True)
	level = models.IntegerField()
	rating = models.IntegerField(default=0, null=True)
	guid = models.CharField(max_length=36)

	def __unicode__(self):
		return "ID#" + str(self.floor_id)+ ", date_created=" + str(self.date_created) + ", level=" + str(self.level) + ", rating=" + str(self.rating)

	def save(self):
		if not self.guid:
			self.guid=uuid.uuid4()
			super(Floor, self).save()

class Comment(models.Model):
	comment_id = models.AutoField(primary_key=True)
	guid = models.CharField(max_length=36)
	comment = models.CharField(max_length=1024)
	date_created = models.DateTimeField(editable=False,auto_now_add=True)
	date_updated = models.DateTimeField(null=True,editable=False, auto_now=True)
	
	def __unicode__(self):
		return "ID#" + str(self.comment_id) + ", date_created=" + str(self.date_created) + ", guid=" +str(self.guid)
					
	def getByGuid(self,gid):
		result =  Comment.objects.filter(guid=gid)
		return result


	      
class Room(models.Model):
	room_id = models.AutoField(primary_key=True)
    	floor_id = models.ForeignKey('Floor');
    	type_id = models.ForeignKey('Room_Type')
    	description = models.CharField(max_length=200)
    	rating = models.IntegerField(default=0, null=True)
	guid = models.CharField(max_length=36)
	def save(self):
		if not self.guid:
			self.guid=uuid.uuid4()
			super(Room, self).save()

    	def __unicode__(self):
        	return str(self.room_id)

    
class Room_Type(models.Model):
    	type_id = models.IntegerField(primary_key=True)
    	type_name = models.CharField(max_length=100) 

	def __unicode__(self):
		return str(self.type_id)

class Room_Name(models.Model):
    	room_id = models.ForeignKey('Room')
    	name = models.CharField(max_length=50);
    	
	def __unicode__(self):
		return "room_id=" + str(self.room_id) + ", name=" + str(self.name)
			
