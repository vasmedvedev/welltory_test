from django.contrib import admin
from welltory import models


class SleepAdmin(admin.ModelAdmin):
    pass


class StepsAdmin(admin.ModelAdmin):
    pass


class GeoAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Sleep, SleepAdmin)
admin.site.register(models.Steps, StepsAdmin)
admin.site.register(models.Geo, GeoAdmin)
