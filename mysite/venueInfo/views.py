from django.shortcuts import render, redirect
import utils


def venue_info(request, venue_id):

    venue = utils.venue.find_one({"venue_id": venue_id})
    concerts = utils.concert.find({"venue_id": venue_id})

    if request.session.get('user_id'):
        account = True

    else:
        account = False

    if venue is None:
        return render(request, '404.html', {'account': account}, status=404)
    else:
        return render(request, 'venueInfo.html',
                      {'concerts': concerts, 'account': account, 'venue': venue})
