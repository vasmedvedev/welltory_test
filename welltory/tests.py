from rest_framework.test import APIClient
from django.test import TestCase
from welltory import models
from decimal import Decimal


class ObjectsListTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.time_start1 = '2017-01-01T12:00:00Z'
        self.time_end1 = '2017-01-01T12:30:00Z'
        
        self.time_start2 = '2017-02-01T00:15:00Z'
        self.time_end2 = '2017-02-01T01:45:00Z'

        self.time_start3 = '2017-03-01T14:30:00Z'
        self.time_end3 = '2017-03-01T14:55:00Z'

        self.sleep1 = models.Sleep.objects.create(time_start=self.time_start1, time_end=self.time_end1)
        self.sleep2 = models.Sleep.objects.create(time_start=self.time_start2, time_end=self.time_end2)
        self.sleep3 = models.Sleep.objects.create(time_start=self.time_start3, time_end=self.time_end3)

        self.steps1 = models.Steps.objects.create(time_start=self.time_start1, time_end=self.time_end1, value=100)
        self.steps2 = models.Steps.objects.create(time_start=self.time_start2, time_end=self.time_end2, value=200)
        self.steps3 = models.Steps.objects.create(time_start=self.time_start3, time_end=self.time_end3, value=300)

        self.geo1 = models.Geo.objects.create(
            time_start=self.time_start1,
            time_end=self.time_end1,
            latitude=Decimal('55.555555'),
            longtitude=Decimal('65.555555')
        )
        self.geo2 = models.Geo.objects.create(
            time_start=self.time_start2,
            time_end=self.time_end2,
            latitude=Decimal('56.666666'),
            longtitude=Decimal('70.666666')
        )
        self.geo3 = models.Geo.objects.create(
            time_start=self.time_start3,
            time_end=self.time_end3,
            latitude=Decimal('66.888888'),
            longtitude=Decimal('60.888888')
        )

    def test_get_sleep_list(self):
        response = self.client.get('/api/sleep/', {
            'time_start': '2017-01-01T13:00:00+0100',
            'time_end': '2017-01-01T13:00:01+0100'
        })

        self.assertListEqual(
            response.data,
            [{'id': self.sleep1.pk, 'time_start': self.time_start1, 'time_end': self.time_end1}]
        )

    def test_get_steps_list(self):
        response = self.client.get('/api/steps/', {
            'time_start': '2017-02-01T00:00:00Z',
            'time_end': '2017-04-01T00:00:00Z'
        })

        self.assertItemsEqual(
            response.data,
            [
                {'id': self.steps2.pk, 'time_start': self.time_start2, 'time_end': self.time_end2, 'value': 200},
                {'id': self.steps3.pk, 'time_start': self.time_start3, 'time_end': self.time_end3, 'value': 300},
            ]
        )

    def test_get_geo_list(self):
        response = self.client.get('/api/geo/', {
            'time_start': '2017-02-01T04:00:00+0300', 'time_end': '2017-03-01T18:00:00+0300'
        })

        self.assertItemsEqual(
            response.data,
            [
                {
                    'id': self.geo3.pk,
                    'time_start': self.time_start3,
                    'time_end': self.time_end3,
                    'latitude': '66.888888',
                    'longtitude': '60.888888'
                }
            ]
        )
