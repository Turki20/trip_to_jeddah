from django.db import models
from django.contrib.auth.models import User 

from places.models import Place
from restaurants.models import Restaurant
# Create your models here.

class Trips(models.Model):
    startDay = models.IntegerField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.userID)
    
    
class TripDetailsPlace(models.Model):
    day = models.IntegerField()
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.trip)
    
class TripDetailsRestraurant(models.Model):
    day = models.IntegerField()
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    place = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.trip)