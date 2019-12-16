from rest_framework import serializers
from .models import Downtime

class DowntimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downtime
        fields = ('id', 'machine', 'employee', 'stoppage', 'date', 'startTime', 'endTime', 'stoppageHours')