from rest_framework.serializers import ModelSerializer
from app_school.models import School, SchoolAdmin

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class SchoolAdminSerializer(ModelSerializer):
    class Meta:
        model = SchoolAdmin
        fields = "__all__"

        depth = 2