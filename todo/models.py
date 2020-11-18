
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	title = models.CharField(max_length=100)
	desc = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	date_due = models.DateTimeField(default=timezone.now)


class Goals(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goallist", null=True)
	goal = models.CharField(max_length=100)
