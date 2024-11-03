from django.shortcuts import render
from .models import Song,Singer
from .serializers import songSerializer,SingerSerializer
from rest_framework import viewsets

# Create your views here.
class singerviewset(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
class Songviewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=songSerializer    