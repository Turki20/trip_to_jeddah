from django.shortcuts import render, redirect

from django.contrib.auth import login as login_auth, authenticate, logout
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required

from trips.models import Trips, TripDetailsRestraurant, TripDetailsPlace
from django.contrib.auth.models import User
# Create your views here.


@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_auth(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_auth(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home') # اذا سوى تسجيل خروج يحذف session المخزنه

@login_required
def profile_view(request):
    getTrips = Trips.objects.filter(userID=request.user)
    dict_trips = []
    for i in getTrips:
        singleTrip = {
            'trip': i,
            'places': [],
            'restuarants': [],
        }
        getPlaceDetails = TripDetailsPlace.objects.filter(trip=i)
        for place in getPlaceDetails:
            singleTrip['places'].append(place.place)
            
        getRestDetails = TripDetailsRestraurant.objects.filter(trip=i)
        for place in getRestDetails:
            singleTrip['restuarants'].append(place.place)
            
        dict_trips.append(singleTrip)
        
    context = {
        'user': request.user,
        'trips': dict_trips,
    }
    return render(request, 'profile.html', context)

@csrf_exempt
@login_required
def profile_update_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})

@login_required
def delete_trip(request, id):
    delTrip = Trips.objects.get(id=id)
    delTrip.delete()
    return redirect('profile')