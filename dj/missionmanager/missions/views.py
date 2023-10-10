from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Mission
from .serializers import MissionSerializer

class MissionListCreateView(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
