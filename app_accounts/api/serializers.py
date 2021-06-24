from rest_framework.serializers import ModelSerializer
from app_accounts.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 2