from django.urls import path
from . import views

urlpatterns = [
    path('allConcerts/', views.allConcerts, name='allConcerts'),

]