from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('venue/<int:venue_id>/', views.venue_info, name='venue_info')
]