from rest_framework import serializers

from tauth.models import AdminService


class AdminServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminService
        fields = ('name',)
