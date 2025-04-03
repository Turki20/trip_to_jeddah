from django.urls import path

from . import views as user
urlpatterns = [
    path('login/', user.login, name='login'),
    path('register/', user.register, name='register'),
    path('logout/', user.logout_view, name='logout'),
    path('profile/', user.profile_view, name='profile'),
    path('update_profile/', user.profile_update_view, name='update_profile'),
    path('delete_trip/<int:id>/', user.delete_trip, name='delete_trip'),
]
