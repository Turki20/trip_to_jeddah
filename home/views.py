from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from places.models import Place, PlaceCategoriy
from restaurants.models import Restaurant, RestCategoriy

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from trips.models import Trips, TripDetailsRestraurant, TripDetailsPlace

# This function renders the main index page
def index(request):
    return render(request, 'index.html')


# This function handles the home page, processes user input, and recommends places/restaurants
@csrf_exempt
def home(request):
    categories = PlaceCategoriy.objects.all()
    allPlaces = Place.objects.all()
    if request.method == 'POST':
        if not request.POST.getlist('places'):
            return redirect('/') # Redirects to the index page if no places are selected
         # Retrieve user-selected values from the form
        places = request.POST.getlist('places')
        restaurants = request.POST.getlist('restaurants')
        kids = request.POST.get('kids')
        interests = request.POST.getlist('interests')
        duration = request.POST.get('duration')

        # Call functions to analyze user preferences and suggest places and restaurants
        customPlaces = analysis(places, kids, interests, duration)
        customRestaurants = analysisRestaurants(restaurants, duration)

        context = {
            'places': allPlaces,
            'categories': categories,
            'customPlaces': customPlaces,
            'customRestaurants': customRestaurants,
        }
        
        # Store results in session for later retrieval
        request.session['customPlaces'] = [places.id for places in customPlaces]
        request.session['customRestaurants'] = [restaurants.id for restaurants in customRestaurants]
    
    else: # if method == 'GET'
        # Retrieve stored preferences if available
        if 'customPlaces' in request.session:
            customPlaces_ids = request.session.get('customPlaces', [])
            customRestaurants_ids = request.session.get('customRestaurants', [])
            customPlaces = Place.objects.filter(id__in=customPlaces_ids)
            customRestaurants = Restaurant.objects.filter(id__in=customRestaurants_ids)
            context = {
                'places': allPlaces,
                'categories': categories,
                'customPlaces': customPlaces,
                'customRestaurants': customRestaurants,
            }
        else:
            return redirect('/')  # Redirect if no data is found in session
        
    return render(request, 'home.html', context)


@csrf_exempt
@login_required  # Ensures that only authenticated users can access this page
def home_page(request):
    allPlaces = ''
    if request.method == 'POST': # from the search form
         # Search for places based on user input and category selection
        if not request.POST.get('search').strip() == '' and int(request.POST.get('category')) == -1:
            allPlaces = Place.objects.filter(name__icontains=request.POST.get('search').strip())
            print(request.POST.get('search'))
            print(request.POST.get('category'))
            
        elif request.POST.get('search').strip() == '' and not int(request.POST.get('category')) == -1:
            allPlaces = Place.objects.select_related('category').filter(category=request.POST.get('category'))
            
        elif not request.POST.get('search').strip() == '' and not int(request.POST.get('category')) == -1:
            allPlaces = Place.objects.select_related('category').filter(category=request.POST.get('category'), name__icontains=request.POST.get('search').strip())
        else:
            allPlaces = Place.objects.all()
    else:
        allPlaces = Place.objects.all()
 
    categories = PlaceCategoriy.objects.all()
    lastTrip = Trips.objects.filter(userID=request.user) 
    
    if len(lastTrip) <= 0:
        return redirect('/')
    lastTrip = lastTrip[len(lastTrip)-1] # Get the most recent trip
    
        # Retrieve places and restaurants for the last trip
    idPlaces = TripDetailsPlace.objects.filter(trip=lastTrip)
    customPlaces = []
    for i in idPlaces:
        customPlaces.append(Place.objects.get(id=i.place.id))
    
    idRest = TripDetailsRestraurant.objects.filter(trip=lastTrip)
    customRestaurants = []
    for i in idRest:
        customRestaurants.append(Restaurant.objects.get(id=i.place.id))
    context = {
        'places': allPlaces,
        'categories': categories,
        'customPlaces': customPlaces,
        'customRestaurants': customRestaurants,
    }
            
    return render(request, 'home_page.html', context)

# This function removes a selected place or restaurant from session data
def delete_place(request, id, type):
    if type == 'place':
        request.session['customPlaces'] = [pid for pid in request.session.get('customPlaces', []) if pid != id]
    elif type == 'rest':
        request.session['customRestaurants'] = [rid for rid in request.session.get('customRestaurants', []) if rid != id]
        
    return redirect('home')
 
 # This function filters restaurants based on user preferences   
def analysisRestaurants(restaurants, duration):
    UserRestID = []
    for i in restaurants:
        if i == 'fastfood':
            UserRestID.append(2)
            UserRestID.append(7)
        # if i == 'international':
        if i == 'specialty':
            UserRestID.append(4)
            UserRestID.append(6)
            UserRestID.append(8)
        if i == 'seafood':
            UserRestID.append(1)
        if i == 'local':
            UserRestID.append(3)
        if i == 'cafe':
            UserRestID.append(5)
            UserRestID.append(9)
            UserRestID.append(10)
    
    restCategories = Restaurant.objects.select_related('category').filter(id__in=UserRestID)

    countOfRests = int(duration) * 2
    finallRest = [] # Return a limited number of restaurants based on countOfRests
    for i in range(countOfRests):
        if len(restCategories) > i:
            finallRest.append(restCategories[i]) 

    return finallRest

def analysis(places, kids, interests, duration):
    # تسجيل جميع الفئات حسب ادخال رغبات المستخدم في مصفوفه
    UserPlacesID = []
    for i in places:
        if i == 'historical':
            UserPlacesID.append(15)
            UserPlacesID.append(16)
            UserPlacesID.append(18)
        if i == 'beaches':
            UserPlacesID.append(23)
            UserPlacesID.append(24)
        if i == 'malls':
            UserPlacesID.append(21)
            UserPlacesID.append(22)
        if i == 'markets':
            UserPlacesID.append(20)
        if i == 'themeparks':
            UserPlacesID.append(25)
        if i == 'museums':
            UserPlacesID.append(17)
            UserPlacesID.append(19)
        #if i == 'parks':
    
    # البحث عن جميع الفئات من المصفوفه اللي حددنا فيها رغبات المستخدم 
    placesCategories = Place.objects.select_related('category').filter(category__in=UserPlacesID)
    
    # احتساب النقاط لكل مكان
    placesWithPoints = []
    for i in placesCategories:
        points = 0
        
        if kids == 'yes':
            points += int(i.kids)
        
        if i.photography and 'photography' in interests:
            points += 5
            
        if i.art and 'art' in interests:
            points += 5
            
        if i.sports and 'sports' in interests:
            points += 5
            
        if i.events and 'events' in interests:
            points += 5
            
        if i.quiet and 'quiet' in interests:
            points += 5
            
        if i.crowded and 'crowded' in interests:
            points += 5
            
        dict_p = {
            'place': i,
            'points': points
        }
        placesWithPoints.append(dict_p)
          
    # ترتيب الاماكن حسب الاعلى نقاطا الى الاقل
    sorted_places = sorted(placesWithPoints, key=lambda x: x['points'], reverse=True)
    
    # ناخذ بعدها عدد الايام ونضيف مكانين لكل يوم
    countOfPlaces = int(duration) * 2

    finallPlaces = []
    for i in range(countOfPlaces):
        if len(sorted_places) > i:
            finallPlaces.append(sorted_places[i]['place']) # المصفوفه النهائية بدون نقاط فقط كائن المكان

    return finallPlaces