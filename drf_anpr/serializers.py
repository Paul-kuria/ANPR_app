from rest_framework import serializers

from home_anpr.models import Guest, House, Tenant, Vehicle, Visitations


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
        lookup_field = "plate_number"  # Specify the lookup field


class VisitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitations
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"
