from django.db import models

# Create your models here.

class Floor(models.Model):
	floor_id int
	description str
	date_created date
	date_updated date
	level int
	rating int
	guid int

class Room(models.Model):
	room_id int
	floor_id int
	room_name str
	type int
	description str
	rating int
	guid int

class Room_Type(models.Model):
	type_id int
	type str

class Room_Name(models.Model):
	room_id int
	name str

class Comment(models.Model):
	guid int
	comment str
	date date