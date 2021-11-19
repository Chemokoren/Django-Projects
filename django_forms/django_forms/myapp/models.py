from django.db import models


class Snippet(models.Model):
	name = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return self.name

# demonstrating formsets
class FormsetExample(models.Model):
	name = models.CharField(max_length=20)
	location = models.CharField(max_length=20)

