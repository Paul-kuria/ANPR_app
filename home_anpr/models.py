from django.db import models


# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = ['week', 'description', 'year']

    def __str__(self) -> str:
        return self.name


class House(models.Model):
    house_number = models.CharField(max_length=100)
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"House {self.house_number}"


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True, null=False)
    vehicle_name = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=100)

    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.plate_number}"


class Visitations(models.Model):
    plate_number = models.CharField(max_length=20, null=True, blank=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    entry_exit = models.DateTimeField(null=True, blank=True)

    tenant_name = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    house_name = models.ForeignKey(
        House, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.plate_number} - {self.tenant_name}"


class Guest(models.Model):
    guest_name = models.CharField(max_length=100)
    visiting_user = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.guest_name} visiting {self.visiting_user.name}"
