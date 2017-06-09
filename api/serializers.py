from rest_framework import serializers
from welltory import models


class SleepSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sleep
        fields = ('id', 'time_start', 'time_end')


class StepsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Steps
        fields = ('id', 'time_start', 'time_end', 'value')


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Geo
        fields = ('id', 'time_start', 'time_end', 'latitude', 'longtitude')
