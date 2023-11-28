from django.shortcuts import render
from .models import * 

# Create your views here.
def home(request):
    vehicles_data = Vehicle.objects.all()
    # model_fields = Vehicle._meta.fields
    # vehicle_field_names = [field.name for field in model_fields]
    vehicle_field_names = ['no', 'vehicle_name','plate_number', 'tenant', 'vehicle_color', 'date_created']
    context = {
        'vehicles_data':vehicles_data,
        'vehicle_field_names': vehicle_field_names,
    }

    return render(request, 'home_anpr/home.html', context)

def residents(request):
    resident_data = Tenant.objects.all()
    resident_field_names = ['no', 'name', 'telephone']
    context = {
        'resident_data':resident_data,
        'resident_field_names': resident_field_names,
    }

    return render(request, 'home_anpr/residents.html', context)

def activity(request):
    return render(request, 'home_anpr/activity.html')