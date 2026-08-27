from django.db import models


class Planets(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, unique=True)
	galaxy = models.CharField(max_length=200, null=True, blank=True)
	star_system = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	discover_date = models.CharField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)