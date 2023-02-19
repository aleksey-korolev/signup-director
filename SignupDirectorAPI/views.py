from django.shortcuts import render

# Create your views here.

from .models import Participants
from .serializers import ParticipantsSerializer
from rest_framework import generics

class ParticipantsView(generics.ListCreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer

class SingleParticipantView(generics.RetrieveUpdateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer