from django.contrib import admin

from .models import Guest, House, Tenant, Vehicle, Visitations

# Register your models here.
admin.site.register(Tenant)
admin.site.register(House)
admin.site.register(Vehicle)
admin.site.register(Visitations)
admin.site.register(Guest)
