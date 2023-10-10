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

def update_mission_completion(mission):
    if mission.is_completed_within_21_days():
        mission.isCompleted = True
    mission.save()