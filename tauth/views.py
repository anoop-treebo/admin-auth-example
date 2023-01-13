from rest_framework import generics
from rest_framework.permissions import AllowAny

from tauth.models import AdminService
from tauth.serializers import AdminServiceSerializer

class AdminServiceList(generics.ListAPIView):
    queryset = AdminService.objects.all()
    serializer_class = AdminServiceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super(AdminServiceList, self).get_queryset()
        queryset = queryset.filter(user__email=self.kwargs['email'])
        return queryset
