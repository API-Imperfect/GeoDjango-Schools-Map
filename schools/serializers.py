from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import School


class SchoolSerailizer(GeoFeatureModelSerializer):
    class Meta:
        model = School
        geo_field = 'location'
        fields = ['name', 'name', 'province', 'district',    'level',
                  'male', 'female', 'electricity_availability', 'school_code']
        read_only_fields = ['id', 'created_at', 'updated_at']
