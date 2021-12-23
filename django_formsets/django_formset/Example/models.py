from django.db import models

from django.db import models

class Example(models.Model):
	name = models.CharField(max_length=20)
	location = models.CharField(max_length=20)
