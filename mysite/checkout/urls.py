from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('delete/', views.delete, name='delete'),
    path('deleteTicket/<int:ticket>', views.deleteTicket, name='deleteTicket'),
    path('clear/', views.clear, name='clear'),
]