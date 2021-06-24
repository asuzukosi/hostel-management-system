from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

from .serializers import SchoolAdminSerializer, SchoolSerializer
from app_school.models import SchoolAdmin, School

class SchoolViewSet(ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    @action(url_name="school specific admins", detail=True)
    def admins(self, request, pk=None):
        school = School.objects.get(pk=pk)
        school_admins = SchoolAdmin.objects.filter(school=school)

        serializer = SchoolAdminSerializer(school_admins, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class SchoolAdminViewset(ModelViewSet):
    serializer_class = SchoolAdminSerializer
    queryset = SchoolAdmin.objects.all()