from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import utils
from django.utils.translation import activate

from django.conf import settings


def set_language(request, language_code):
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if language_code:
        activate(language_code)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
    return response


def homepage(request):
    if request.session.get('user_id'):
        account = True
    else:
        account = False
    concert = list(utils.concert.find({}))
    venue = list(utils.venue.find({}))
    template = loader.get_template('homepage.html')
    context = {
        'venue': venue,
        'concert': concert,
        'account': account,
    }
    return HttpResponse(template.render(context, request))


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('/')


def error_404(request, exception):
    if request.session.get('user_id'):
        account = True
    else:
        account = False
    return render(request, '404.html', {'account': account}, status=404)
