from django.urls import path
from .views import sensorHandler

urlpatterns = [
    path('api/', sensorHandler, name='sensor')
]