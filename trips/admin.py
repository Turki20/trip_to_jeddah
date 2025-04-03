from django.contrib import admin
from .models import Trips, TripDetailsPlace, TripDetailsRestraurant

# Register your models here.
admin.site.register(Trips)
admin.site.register(TripDetailsRestraurant)
admin.site.register(TripDetailsPlace)