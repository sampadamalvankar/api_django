from rest_framework import serializers
from API.models import User,Client,Project

class UserSerializer(serializers.Modelserializer):
    class Meta:
        model=User
        fields=('UserId','UserName','created_at','created_by')


class ClientSerializer(serializers.Modelserializer):
    class Meta:
        model=Client
        fields=('ClientId', 'ClientName', 'created_at', 'created_by')


class ProjectSerializer(serializers.Modelserializer):
    class Meta:
        model=Project
        fields=('ProjectName')
