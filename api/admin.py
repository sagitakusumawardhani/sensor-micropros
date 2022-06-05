from django.contrib import admin
from .models import Sensor

class sensorAdmin(admin.ModelAdmin):
    list_display = ['ph', 'tds', 'createdAt', 'updatedAt']

admin.site.register(Sensor, sensorAdmin)
