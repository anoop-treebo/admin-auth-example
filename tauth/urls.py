from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tauth import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('sso-users/<str:email>/services/',
        views.AdminServiceList.as_view(),
        name='adminservice-list'),
])
