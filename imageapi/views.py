from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.utils import json

from .serializers import *
from .models import *


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

