from django.urls import path 
from . import views 

urlpatterns = [
    # GET
    
    path("vehicle/<str:plate_number>/", views.FetchOneVehicle.as_view(), name="vehicle"),
    path("vehicles-list/", views.FetchVehicles.as_view(), name="vehicles-list"),
    path("residents-list/", views.FetchTenants.as_view(), name="residents-list"),

    # POST
    path("tenant-create/", views.CreateTenant.as_view(), name="tenant-create"),
    path("vehicle-create/", views.CreateVehicle.as_view(), name="vehicle-create"),
    path("bulk-register/", views.BulkRegister.as_view(), name="bulk-register"),
    
    # update
    # path("vehicle-update/", views.UpdateVehicle, name="vehicle-update"),
    
    # # DELETE
    # path("vehicle-delete/<str:pk>/", views.DeleteVehicle.as_view(), name="vehicle-delete"),
    # path("resident-delete/<str:pk>/", views.DeleteResident.as_view(), name="resident-delete"),
]
