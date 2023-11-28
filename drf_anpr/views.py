from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from coreapi import Request 

from .serializers import VisitationSerializer, VehicleSerializer, TenantSerializer, HouseSerializer, GuestSerializer
from home_anpr.models import Vehicle, Tenant, House
from .utils import InputData

# Create your views here.
@api_view(['GET'])
def overview(request):
    api_urls = {
        'vehicle':'vehicles-list',
        'residents':'residents-list',
    }

    return Response(api_urls)

@api_view(['GET'])
def fetchVehicles(request):
    vehicle = Vehicle.objects.all()
    vehicle_serializer = VehicleSerializer(vehicle, many=True)
    return Response(vehicle_serializer.data)

@api_view(['GET'])
def fetchTenant(request):
    tenant = Tenant.objects.all()
    tenant_serializer = TenantSerializer(tenant, many=True)
    return Response(tenant_serializer.data)

# CREATE tenant, vehicle
@api_view(['POST'])
def CreateTenant(request):
    if request.content_type == 'application/x-www-form-urlencoded':
        # If the request is a form submission, use request.POST
        serializer = TenantSerializer(data=request.POST)
    else:
        # If the request is JSON, use request.data
        serializer = TenantSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def CreateVehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# BULK CREATE production
@api_view(['POST'])
def BulkRegister(request):
    # list of dicts 
    vehicles_data = InputData().read_csv()

    # # create serializer instance
    # serializer = ProductionSerializer(data=variety_data, many=True)

    # # Validata and save the data if valid
    # if serializer.is_valid():
    #     serializer.save() 
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
