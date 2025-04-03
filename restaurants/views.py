from django.shortcuts import render

# Create your views here.
from .models import Restaurant
# Create your views here.

def rest_details(request, id):
    place = Restaurant.objects.get(id=id)
    context = {
        'place': place,
    }
    
    return render(request, 'rest_details.html', context)