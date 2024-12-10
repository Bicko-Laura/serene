from django.contrib.auth.models import User
from django.db import models

# Create your models here.
SELECT_PACKAGE = [
    ('mombasa','Mombasa Value'),
    ('diani','Diani Classic'),
    ('malindi','Malindi Deluxe'),
    ('bugdets','Bugdets Safari'),
    ('mid-range','Mid-Range Safari'),
    ('luxury','Luxury Safari'),
    ('meru','Meru Value'),
    ('nyeri','Nyeri Comfort'),
    ('nanyuki','Nanyuki Exclusive'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    email = models.EmailField()
    checkin_date = models.CharField(max_length=10)
    checkout_date = models.CharField(max_length=10)
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    select_package = models.CharField(max_length=100, choices=SELECT_PACKAGE, blank=True)
    trip_preferences = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


