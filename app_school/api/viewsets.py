from rest_framework.viewsets import ModelViewSet
from .serializers import SchoolSerializer
from app_school.models import School

class SchoolViewSet(ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()