from django.shortcuts import render
from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
 
# Create your views here.


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'is_student')
        extra_kwargs = {'password': {
            'write_oly': True, 'min_length': 8
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializers_class = UserSerializer
