from rest_framework import viewsets

from .models import School
from .serializers import SchoolSerailizer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerailizer
