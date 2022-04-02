from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.submit_city_view, name="submit_city"),
    path('todays_weather/<city>/', views.show_weather_view, name="todays_weather"),

]
