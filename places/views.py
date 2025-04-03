from django.shortcuts import render

from .models import Place
# Create your views here.

# بدورها تعرض مكان واحد حسب ادخال المستخدم
def place_details(request, id):
    place = Place.objects.get(id=id)
    context = {
        'place': place,
    }
    
    return render(request, 'place_details.html', context)
