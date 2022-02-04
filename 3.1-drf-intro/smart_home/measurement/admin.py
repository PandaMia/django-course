from django.contrib import admin
from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created_at']
