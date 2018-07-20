from django.db import models

# Create your models here.
class iotdevices(models.Model):
	device_id=models.CharField(max_length=50)
	time=models.CharField(max_length=50)
	value=models.CharField(max_length=50)

	def __str__(self):
		return self.device_id