from django.db import models


class TimestampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class AdminService(models.Model):
    name = models.CharField(max_length=32)
    login_url = models.URLField()
    redirect_url = models.URLField()

    def __str__(self):
        return self.name


class SSOUser(TimestampMixin, models.Model):
    email = models.EmailField(primary_key=True)
    is_active = models.BooleanField(default=True)
    allowed_services = models.ManyToManyField(AdminService, related_name='user')

    def __str__(self):
        return self.email
