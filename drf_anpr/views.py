from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from coreapi import Request 
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import VisitationSerializer, VehicleSerializer, TenantSerializer, HouseSerializer, GuestSerializer
from home_anpr.models import Vehicle, Tenant, House
from .utils import InputData



# Create your views here.

''' GET ONE '''
class FetchOneVehicle(RetrieveAPIView):
    serializer_class = VehicleSerializer
    @swagger_auto_schema(tags=['Vehicle Operations'], operation_summary="Retrieve a single vehicle")
    def get(self, request, plate_number):
        vehicles = Vehicle.objects.get(plate_number=plate_number) 
        vehicle_serializer = VehicleSerializer(vehicles)
        return Response(vehicle_serializer.data)
  
    # queryset = Vehicle.objects.all()
    # serializer_class = VehicleSerializer
    # lookup_field = 'plate_number'
    
    # @swagger_auto_schema(tags=['Vehicle Operations'], operation_summary="Retrieve a single vehicle")
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
    
    # def get_object(self):
    #     plate_number = self.kwargs.get(self.lookup_url_kwarg)
    #     # Directly query the database using the plate_number
    #     obj = Vehicle.objects.filter(plate_number=plate_number).first()
    #     if obj is None:
    #         # Customize the response if the object is not found
    #         return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    #     self.check_object_permissions(self.request, obj)
    #     return obj
    
'''GET ALL'''
class FetchVehicles(GenericAPIView):
    serializer_class = VehicleSerializer
    @swagger_auto_schema(tags=['Vehicle Operations'], operation_summary="Retrieve all vehicles")
    def get(self, request):
        vehicles = Vehicle.objects.all() 
        vehicle_serializer = VehicleSerializer(vehicles, many=True)
        return Response(vehicle_serializer.data)

class FetchTenants(GenericAPIView):
    serializer_class = TenantSerializer
    @swagger_auto_schema(tags=['Tenant Operations'], operation_summary="Retrieve a single tenant")
    def get(self, request):
        tenants = Tenant.objects.all() 
        tenants_serializer = TenantSerializer(tenants, many=True)
        return Response(tenants_serializer.data)

# CREATE tenant, vehicle
class CreateTenant(GenericAPIView):
    serializer_class = TenantSerializer 
    @swagger_auto_schema(tags=['Tenant Operations'], operation_summary="Create a single tenant")
    def post(self, request):
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class CreateVehicle(GenericAPIView):
    serializer_class = VehicleSerializer 

    @swagger_auto_schema(tags=['Vehicle Operations'], operation_summary="Create a vehicle")
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) 

class BulkRegister(GenericAPIView):
    serializer_class = VehicleSerializer 
    
    @swagger_auto_schema(tags=['Vehicle Operations'], operation_summary="Create bulk vehicle registrations")
    def post(self, request):
        # list of dicts 
        vehicles_data = InputData().read_csv()
        new_list = []
        for data  in vehicles_data:
            tenant_name = data['tenant_name']
            
            # lookup tenant by name in models
            tenant_table = Tenant.objects.get(name=tenant_name)
            data['tenant'] = tenant_table.id

            # # create serializer instance
            serializer = VehicleSerializer(data=data)

            # Validata and save the data if valid
            if serializer.is_valid():
                serializer.save() 
                new_list.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(new_list, status=status.HTTP_201_CREATED)

''' DELETE '''
# class DeleteVehicle(GenericAPIView):
#     serializer_class = VehicleSerializer 

#     def delete(self, request, pk):
#         vehicle = Vehicle.objects.get(id=pk)
#         print(vehicle)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class DeleteResident(GenericAPIView):
#     serializer_class = TenantSerializer 

#     def delete(self, request, pk):
#         tenant = Tenant.objects.get(id=pk)
#         return Response(status=status.HTTP_204_NO_CONTENT)