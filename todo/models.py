from django.db import models

#Class represents each todo item in our SQLite3 database
class TodoItem(models.Model):
	content = models.TextField()

