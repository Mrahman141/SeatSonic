from django.shortcuts import render
import utils


def search(request):
    if request.session.get('user_id'):
        account = True
    else:
        account = False

    if request.method == "POST":
        searched = request.POST['searched']
        search_type = request.POST['search_type']

        if search_type == 'venue':
            results = utils.venue.find({'name': {'$regex': searched, '$options': 'i'}})
        else:
            results = utils.concert.find({'artist_name': {'$regex': searched, '$options': 'i'}})

        return render(request, 'search.html',
                      {'searched': searched, 'search_type': search_type, 'records': results, 'account': account})

    else:
        return render(request, 'search.html',
                      {'account': account})
