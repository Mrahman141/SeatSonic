from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('concert/<int:concert_id>/', views.concert_info, name='concert_info')
]
