from django.db import models


class DateTimeModel(models.Model):
    time_start = models.DateTimeField(db_index=True)
    time_end = models.DateTimeField(db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.pk)


class Sleep(DateTimeModel):

    class Meta:
        verbose_name_plural = 'Sleep'


class Steps(DateTimeModel):
    value = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Steps'


class Geo(DateTimeModel):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name_plural = 'Geo coordinates'
