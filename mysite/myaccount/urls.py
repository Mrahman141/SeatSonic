from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('tickets/', views.tickets, name='account'),
    path('account/edit', views.edit_account, name='edit_account'),
    path('account/addconcert', views.add_concert, name='add_concert'),
    path('account/addvenue', views.add_venue, name='add_venue'),
    path('account/listvenue', views.list_venue, name='list_venue'),
    path('account/listconcert', views.list_concert, name='list_concert'),
    path('account/editvenue/<int:ven_id>', views.edit_venue, name='edit_venue'),
    path('account/deletevenue/<int:ven_id>', views.delete_venue, name='delete_venue'),
    path('account/editconcert/<int:con_id>', views.edit_concert, name='edit_concert'),
    path('account/deleteconcert/<int:con_id>', views.delete_concert, name='delete_concert'),
    path('account/delete', views.delete_account, name='delete_account'),
    path('account/signup', views.signup, name='signup'),

]