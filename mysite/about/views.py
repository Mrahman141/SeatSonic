# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    if request.session.get('user_id'):
        account = True
    else:
        account = False
    return render(request, 'about.html', {'account': account})


