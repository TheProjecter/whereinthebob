from django.db import models

class Floor(models.Model):
	floor_id = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=200)
	date_created = models.DateTimeField(editable=False)
	date_updated = models.DateTimeField(null=True)
	level = models.IntegerField()
	rating = models.IntegerField(default=0, null=True)

	def __unicode__(self):
		return "ID#" + str(self.floor_id)+ ", date_created=" + str(self.date_created) + ", level=" + str(self.level) + ", rating=" + str(self.rating)