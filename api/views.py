from telnetlib import STATUS
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor
from .serializers import SensorSerializers


# function handler for getting data and post data
@api_view(['GET', 'POST'])
def sensorHandler(request):
    qs = Sensor.objects.all()

    if request.method == 'GET':
        serializer = SensorSerializers(qs, many=True)    
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = SensorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
