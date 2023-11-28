from django.urls import path 
from . import views 

urlpatterns = [
    # GET
    path('', views.overview, name="overview"),
    path("vehicles-list/", views.fetchVehicles, name="vehicles-list"),
    path("residents-list/", views.fetchTenant, name="residents-list"),

    # POST
    path("tenant-create/", views.CreateTenant, name="tenant-create"),
    path("vehicle-create/", views.CreateVehicle, name="vehicle-create"),
    path("bulk-register/", views.BulkRegister, name="bulk-register"),
    
    # update
    # path("vehicle-update/", views.UpdateVehicle, name="vehicle-update"),
]