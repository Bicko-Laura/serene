from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    checkin_date = models.CharField(max_length=10)
    checkout_date = models.CharField(max_length=10)
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    trip_preferences = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


