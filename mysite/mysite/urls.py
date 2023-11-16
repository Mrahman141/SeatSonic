
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('myaccount.urls')),
    path('', include('allConcerts.urls')),
    path('', include('about.urls')),
    path('', include('venues.urls')),
    path('', include('checkout.urls')),
    path('', include('sign_up_in_out.urls')),
    path('', include('concertInfo.urls')),
    path('', include('search.urls')),
    path('', include('venueInfo.urls')),
]

handler404 = 'home.views.error_404'
