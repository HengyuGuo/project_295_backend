from rest_framework import serializers
from backend.models import Sensors, Clusters, LANGUAGE_CHOICES, STYLE_CHOICES


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ('id', 'cluster_id', 'latitude', 'longitude', 'sensor_type', 'manufacture', 'operation', 'health', 'message')


class ClustersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clusters
        fields = ('id', 'operation', 'health', 'message')
