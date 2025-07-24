from django.shortcuts import render
from rest_framework import viewsets
from .models import Room, Seat
from .serializers import RoomSerializer, SeatSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

