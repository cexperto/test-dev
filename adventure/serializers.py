from rest_framework import serializers


class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()

class JourneyStopSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    end = serializers.DateField()