from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home_anpr/home.html')

def residents(request):
    return render(request, 'home_anpr/residents.html')

def activity(request):
    return render(request, 'home_anpr/activity.html')