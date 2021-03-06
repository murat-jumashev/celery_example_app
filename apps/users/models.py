from django.db import models
from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return '<{}>'.format(self.email)
