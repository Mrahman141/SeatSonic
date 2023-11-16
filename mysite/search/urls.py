from django.urls import path
from . import views

urlpatterns = [
    # path('concert/<str:query>/', views.search_concert, name='search_concert'),
    # path('venue/<str:query>/', views.search_venue, name='search_venue')

    path('search/', views.search, name='search')
]
