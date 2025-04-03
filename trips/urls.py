from django.urls import path
from . import views 

urlpatterns = [
    path('save_trip', views.save_trip, name='save_trip')
]
