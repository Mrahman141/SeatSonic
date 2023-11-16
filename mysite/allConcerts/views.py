from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
import utils


def allConcerts(request):
    if request.session.get('user_id'):
        account = True
    else:
        account = False
    concerts = utils.concert.find({})
    sorted_documents = sorted(concerts, key=lambda x: datetime.strptime(x['date_time'], '%A, %B %d, %Y at %I:%M %p'))

    return render(request, 'concerts.html', {'concerts': sorted_documents,'account': account})


