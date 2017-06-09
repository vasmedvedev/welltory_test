from rest_framework import viewsets
from api import serializers
from welltory import models


class SleepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sleep.objects.all()
    serializer_class = serializers.SleepSerializer

    def get_queryset(self):
        time_start = self.request.query_params.get('time_start')
        time_end = self.request.query_params.get('time_end')

        kwargs = {}
        if time_start is not None and time_end is not None:
            kwargs['time_start__gte'] = time_start
            kwargs['time_start__lte'] = time_end

        return self.queryset.filter(**kwargs)


class StepsViewSet(SleepViewSet):
    queryset = models.Steps.objects.all()
    serializer_class = serializers.StepsSerializer


class GeoViewSet(SleepViewSet):
    queryset = models.Geo.objects.all()
    serializer_class = serializers.GeoSerializer
