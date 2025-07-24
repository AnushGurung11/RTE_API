from rest_framework import serializers
from .models import Room,Seat

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        field = ['id','']
        
         