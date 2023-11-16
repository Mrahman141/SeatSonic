from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('logout/', views.logout, name='logout'),
    path('language/<str:language_code>/', views.set_language, name='language_code'),

]