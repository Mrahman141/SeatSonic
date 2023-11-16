from django.shortcuts import render
from django.http import HttpResponse
#import helpers
import utils

def venues(request):
    if request.session.get('user_id'):
        account = True
    else:
        account = False
    venue = utils.venue.find({})
    return render(request, 'venues.html', {'venues': venue, 'account': account})

