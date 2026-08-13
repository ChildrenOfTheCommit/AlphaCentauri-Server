from django.db import models


class Account(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	codename = models.CharField(max_length=100, unique=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)