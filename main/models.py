from django.db import models

class Write(models.Model):
	text = models.TextField(max_length=1000)
# Create your models here.
