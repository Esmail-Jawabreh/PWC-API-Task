from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields = ('event', 'airport_code', 'flight_number', 'departure_time', 'arrival_time', 'created_at')