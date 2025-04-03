from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from places.models import Place
from restaurants.models import Restaurant
from .models import Trips, TripDetailsPlace, TripDetailsRestraurant
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def save_trip(request):
    if 'customPlaces' in request.session and 'customRestaurants' in request.session:
        customPlaces_ids = request.session.get('customPlaces', [])
        customRestaurants_ids = request.session.get('customRestaurants', [])
        customPlaces = Place.objects.filter(id__in=customPlaces_ids)
        customRestaurants = Restaurant.objects.filter(id__in=customRestaurants_ids)
        
        user = User.objects.get(id=request.user.id)
        newTrip = Trips(startDay=1, userID=user)
        newTrip.save()
        
        counter = 0
        for i in customPlaces:
            place = Place.objects.get(id=i.id)
            newPlace = TripDetailsPlace(day=counter, trip=newTrip, place=place)
            newPlace.save()
            counter = counter + 1
        
        counter = 0
        for i in customRestaurants:
            rest = Restaurant.objects.get(id=i.id)
            newRest = TripDetailsRestraurant(day=counter, trip=newTrip, place=rest)
            newRest.save()
            counter = counter + 1
            
            
        return redirect('home_page')
        
    else:
        return HttpResponseNotFound('not data in the places or restaurant')
    
