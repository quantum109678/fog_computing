from django.shortcuts import render
from rest_framework import viewsets
from .models import iotdevices
from .serializers import LanguageSerializer
# Create your views here.
class LanguageView(viewsets.ModelViewSet):
	queryset=iotdevices.objects.all()
	serializer_class=LanguageSerializer
