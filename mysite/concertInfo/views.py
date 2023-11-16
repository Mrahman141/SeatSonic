from django.shortcuts import render, redirect
import utils


def concert_info(request, concert_id):
    s_max = 6
    global concert
    concert = utils.concert.find_one({"concert_id": concert_id})

    if request.session.get('user_id'):
        account = True
        id = request.session.get('user_id')
        user = utils.user.find_one({"user_id": id})
        if user['account_type'] == 'commercial':
            s_max = 30
    else:
        account = False

    if concert is None:
        return render(request, '404.html', {'account': account}, status=404)
    else:
        venue = utils.venue.find_one({"venue_id": concert['venue_id']})
        return render(request, 'concertInfo.html',
                      {'concert': concert, 'account': account, 'venue': venue, 'max_s': s_max})


def checkout(request):
    if request.session.get('user_id'):

        return redirect('/checkout')
    else:
        return redirect('/signup')
