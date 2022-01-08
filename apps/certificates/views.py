from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Certifacate


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certifacate
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certifacate.objects.all()
    serializer_class = CertificateSerializer
