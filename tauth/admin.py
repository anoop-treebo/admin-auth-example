from django.contrib import admin
from django.contrib.auth.models import User
from tauth.models import AdminService, SSOUser


admin.site.register(AdminService)
admin.site.register(SSOUser)
admin.site.unregister(User)
