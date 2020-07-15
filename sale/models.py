from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import make_aware

from car_sale import settings


def default_end_time():
    end_time = datetime.now()
    end_time += timedelta(days=7)

    return make_aware(end_time)


class Advertisement(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, related_name='ads', null=True)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    car_name = models.CharField(max_length=64, null=False, blank=False)
    car_model = models.CharField(max_length=64, null=False, blank=False)
    min_price = models.PositiveIntegerField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False, default=default_end_time)

    def __str__(self):
        return self.title


class Offer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    advertisement = models.ForeignKey(to=Advertisement, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=False, blank=False)
    creation_date = models.DateTimeField(auto_now=True, editable=False)
