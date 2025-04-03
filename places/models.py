from django.db import models

# Create your models here.
class PlaceCategoriy(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    googlMapLink = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='imagesP/', blank=True, null=True)
    long_desc = models.TextField()
    category = models.ForeignKey(PlaceCategoriy, on_delete=models.CASCADE)
    kids = models.IntegerField(null=True)
    photography = models.BooleanField(null=True)
    art = models.BooleanField(null=True)
    sports = models.BooleanField(null=True)
    events = models.BooleanField(null=True)
    quiet = models.BooleanField(null=True)
    crowded = models.BooleanField(null=True)
    
    def __str__(self):
        return self.name