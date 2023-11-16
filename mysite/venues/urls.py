from django.urls import path
from . import views

urlpatterns = [
    path('venues/', views.venues, name='venues'),

]