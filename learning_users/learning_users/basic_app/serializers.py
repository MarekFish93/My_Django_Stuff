from rest_framework import serializers
from .models import UserProfileInfo

class UserProfileInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = "__all__"
