from rest_framework import serializers


class DatesForCalendarSerializer(serializers.Serializer):
    date = serializers.DateField()
    day = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()
