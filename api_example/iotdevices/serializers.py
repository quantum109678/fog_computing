from rest_framework import serializers
from .models import iotdevices

class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = iotdevices
		fields=('id','device_id','time','value')