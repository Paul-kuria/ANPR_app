from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.response import Response

from home_anpr.models import *

from .serializers import *
from .utils import InputData

# Create your views here.

""" [GET] REQUESTS """


class FetchOneVehicle(RetrieveAPIView):
    serializer_class = VehicleSerializer

    @swagger_auto_schema(
        tags=["Vehicle Operations"], operation_summary="Retrieve a single vehicle"
    )
    def get(self, request, plate_number):
        vehicles = Vehicle.objects.get(plate_number=plate_number)
        vehicle_serializer = VehicleSerializer(vehicles)
        return Response(vehicle_serializer.data)


"""GET ALL"""


class FetchVehicles(GenericAPIView):
    serializer_class = VehicleSerializer

    @swagger_auto_schema(
        tags=["Vehicle Operations"], operation_summary="Retrieve all vehicles"
    )
    def get(self, request):
        vehicles = Vehicle.objects.all()
        vehicle_serializer = VehicleSerializer(vehicles, many=True)
        return Response(vehicle_serializer.data)


class FetchTenants(GenericAPIView):
    serializer_class = TenantSerializer

    @swagger_auto_schema(
        tags=["Tenant Operations"], operation_summary="Retrieve a single tenant"
    )
    def get(self, request):
        tenants = Tenant.objects.all()
        tenants_serializer = TenantSerializer(tenants, many=True)
        return Response(tenants_serializer.data)


""" [CREATE] REQUESTS """


class CreateTenant(GenericAPIView):
    serializer_class = TenantSerializer

    @swagger_auto_schema(
        tags=["Tenant Operations"], operation_summary="Create a single tenant"
    )
    def post(self, request):
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CreateVehicle(GenericAPIView):
    serializer_class = VehicleSerializer

    @swagger_auto_schema(
        tags=["Vehicle Operations"], operation_summary="Create a vehicle"
    )
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BulkRegister(GenericAPIView):
    serializer_class = VehicleSerializer

    @swagger_auto_schema(
        tags=["Vehicle Operations"],
        operation_summary="Create bulk vehicle registrations",
    )
    def post(self, request):
        # list of dicts
        vehicles_data = InputData().read_csv()
        new_list = []
        for data in vehicles_data:
            tenant_name = data["tenant_name"]

            # lookup tenant by name in models
            tenant_table = Tenant.objects.get(name=tenant_name)
            data["tenant"] = tenant_table.id

            # # create serializer instance
            serializer = VehicleSerializer(data=data)

            # Validata and save the data if valid
            if serializer.is_valid():
                serializer.save()
                new_list.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(new_list, status=status.HTTP_201_CREATED)


""" [UPDATE REQUESTS] """
# TODO: Fix implementation here


class UpdateVehicle(GenericAPIView):
    serializer_class = VehicleSerializer

    @swagger_auto_schema(
        tags=["Vehicle Operations"], operation_summary="Update vehicle data based on id"
    )
    def put(self, request, pk):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(instance=vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


""" [DELETE REQUESTS] """


class DeleteVehicle(DestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    @swagger_auto_schema(operation_summary="Delete vehicle based on id")
    def delete(self, request, pk):
        return super().delete(request, pk)


class DeleteResident(DestroyAPIView):
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()

    @swagger_auto_schema(operation_summary="Delete resident based on id")
    def delete(self, request, pk):
        return super().delete(request, pk)
