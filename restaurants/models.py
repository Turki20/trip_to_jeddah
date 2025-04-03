from django.db import models

# Create your models here.
class RestCategoriy(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    googlMapLink = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='imagesR/', blank=True, null=True)
    desc = models.TextField()
    category = models.ForeignKey(RestCategoriy, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name