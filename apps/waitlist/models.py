from django.db import models
from apps.utils.models import Timestamps


class Waitlist(Timestamps, models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=200,
        verbose_name='email address',
        unique=True,
    )
    level = models.IntegerField(verbose_name='Class Level', default=1)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'waitlist entiries'

    def full_name(self):
        return f'{self.firstname} {self.last_name}'
