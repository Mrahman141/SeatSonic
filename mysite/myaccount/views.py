from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from datetime import datetime
import utils


def account(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        name = user['username']
        account_a = True
    else:
        return redirect('/signin/')
    glow = True
    return render(request, 'account.html',
                  {'glow_p': glow, 'account': account_a, 'admin': admin, 'name': name, 'user': user})


def tickets(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        name = user['username']
        account_a = True
    else:
        return redirect('/signin/')
    glow = True
    return render(request, 'tickets.html',
                  {'glow_p': glow, 'account': account_a, 'admin': admin, 'name': name, 'user': user})


def edit_account(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        name = user['username']
        account_a = True
    else:
        return redirect('/signin/')
    glow = True
    id = request.session.get('user_id')
    user = utils.user.find_one({"user_id": id})
    if request.method == "POST":
        print(request.POST['first_name'])
        utils.user.update_one({'user_id': request.session.get('user_id')},
                              {'$set': {'fname': request.POST['first_name'],
                                        'lname': request.POST['last_name'],
                                        'email': request.POST['user_email'],
                                        'phone': request.POST['phoneNumber'],
                                        'province': request.POST['province'],
                                        'street_address': request.POST['street_address'],
                                        'country': request.POST['country']
                                        }})
        return redirect('/account/')

    return render(request, 'edit_account.html', {'glow_e': glow, 'user': user, 'admin': admin, 'account': account_a})


def add_venue(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    if request.method == 'POST':
        venue_count = utils.venue.count_documents({});
        venue_count = venue_count + 1;
        while (utils.venue.find_one({'venue_id': venue_count}) is not None):
            venue_count = venue_count + 1;

        if utils.venue.find_one({'name': request.POST['venue_name']}) is not None:
            errors = True;
            error = "The Venue with this name is already been added."
            template = loader.get_template('add_venue.html')
            context = {
                'er': errors,
                'err_msg': error,
                'admin': admin,
                'account': account_a
            }
            return HttpResponse(template.render(context, request))

        if utils.venue.find_one({'email': request.POST['venue_email']}) is not None:
            errors = True;
            error = "The Venue with this email is already been added."
            template = loader.get_template('add_venue.html')
            context = {
                'er': errors,
                'err_msg': error,
                'admin': admin,
                'account': account_a
            }
            return HttpResponse(template.render(context, request))

        lines = request.POST['venue_seat_types'].splitlines()
        seats = []
        total_seats = 0;
        for line in lines:
            parts = line.split("-")
            sea = {"type": parts[0].strip(), "seats": int(parts[1].strip())}
            seats.append(sea)
            total_seats += sea['seats']

        if not (total_seats == int(request.POST['venue_totseats'])):
            errors = True;
            error = "The total number of seats for the venue does not match the sum of seats for all the seat types."
            template = loader.get_template('add_venue.html')
            context = {
                'er': errors,
                'err_msg': error,
                'admin': admin,
                'account': account_a
            }
            return HttpResponse(template.render(context, request))

        newVenue = {
            "venue_id": venue_count,
            "name": request.POST['venue_name'],
            "email": request.POST['venue_email'],
            "phone_number": request.POST['venue_phone'],
            "image": request.POST['venue_image'],
            "country": request.POST['venue_country'],
            "province": request.POST['venue_province'],
            "street_address": request.POST['venue_streetaddress'],
            "city": request.POST['venue_city'],
            "postal_code": request.POST['venue_postalcode'],
            "total_seats": int(request.POST['venue_totseats']),
            "seat_types": seats
        }
        print(newVenue)
        utils.venue.insert_many([newVenue])
        return render(request, 'added_venue.html',
                      {'venue': newVenue, 'account': account_a, 'admin': admin, 'message': "Added"})
    glow = True;
    return render(request, 'add_venue.html', {'glow_av': glow, 'account': account_a, 'admin': admin})


def add_concert(request):
    error = ''
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    if request.method == 'POST':
        concert_count = utils.concert.count_documents({});
        concert_count = concert_count + 1;
        while utils.concert.find_one({'concert_id': concert_count}) is not None:
            concert_count = concert_count + 1;
        lines = request.POST['venue_seat_price'].splitlines()
        prices = []
        total_seats = 0
        for line in lines:

            parts = line.split("-")
            if len(parts) == 3:
                pri = {"type": parts[0].strip(), "price": float(parts[1].strip()), 'total': int(parts[2].strip()),
                       'booked': 0}

                prices.append(pri)
                total_seats += int(parts[2].strip())
            else:
                error = "Provide all 3 arguments in Seat Price field"
                venue = utils.venue.find({})

                template = loader.get_template('add_concert.html')

                glow = True;
                context = {
                    'venue': venue,
                    'glow_ac': glow,
                    'account': account_a,
                    'admin': admin,
                    'err': error,

                }
                return HttpResponse(template.render(context, request))

        venue = utils.venue.find_one({'venue_id': int(request.POST['venueID'])})
        concerts = utils.concert.find({})
        for concert in concerts:
            if request.POST['concert_name'] == concert['concert_name'] and request.POST['concert_date_time'] == concert[
                'date_time']:
                return render(request, 'added_concert.html',
                              {'concert': concert, 'account': account_a, 'admin': admin, 'message': "Added"})

        concert_seat_types = {seat["type"]: seat for seat in prices}
        venue_seat_types = {seat["type"]: seat for seat in venue["seat_types"]}
        if not all(seat_type in venue_seat_types for seat_type in concert_seat_types) \
                or not all(seat_type in concert_seat_types for seat_type in venue_seat_types):
            error = "Concert seats do not match venue seats"
            venue = utils.venue.find({})
            template = loader.get_template('add_concert.html')
            glow = True;
            context = {
                'venue': venue,
                'glow_ac': glow,
                'account': account_a,
                'admin': admin,
                'err': error,

            }
            return HttpResponse(template.render(context, request))

        for seat_type in concert_seat_types:
            concert_seats = next(seat for seat in prices if seat["type"] == seat_type)["total"]
            venue_seats = next(seat for seat in venue["seat_types"] if seat["type"] == seat_type)["seats"]
            if concert_seats > venue_seats:
                error = f"Concert has more {seat_type} row seats than venue"
                venue = utils.venue.find({})
                template = loader.get_template('add_concert.html')
                glow = True;
                context = {
                    'venue': venue,
                    'glow_ac': glow,
                    'account': account_a,
                    'admin': admin,
                    'err': error,

                }
                return HttpResponse(template.render(context, request))

        if total_seats > venue['total_seats']:
            error = "Total seats have to be less or equal to " + str(venue['total_seats'])
            venue = utils.venue.find({})
            template = loader.get_template('edit_concert.html')
            glow = True;
            context = {
                'venue': venue,
                'glow_ac': glow,
                'account': account_a,
                'admin': admin,
                'err': error,

            }
            return HttpResponse(template.render(context, request))
        else:
            newConcert = {
                "venue_id": int(request.POST['venueID']),
                "concert_id": concert_count,
                "concert_name": request.POST['concert_name'],
                "artist_name": request.POST['artist_name'].split(","),
                "genre": request.POST['artist_genre'].split(","),
                "image": request.POST['artist_image'],
                "date_time": (datetime.strptime(request.POST['concert_date_time'], '%Y-%m-%dT%H:%M')).strftime("%A, %B %d, %Y at %I:%M %p"),
                "doors_open": request.POST['concert_door_open'],
                "seats": prices
            }
            utils.concert.insert_many([newConcert])
            return render(request, 'added_concert.html',
                          {'concert': newConcert, 'account': account_a, 'admin': admin, 'message': "Added"})

    venue = utils.venue.find({})
    template = loader.get_template('add_concert.html')
    glow = True;
    context = {
        'venue': venue,
        'glow_ac': glow,
        'account': account_a,
        'admin': admin,
        'err': error,

    }
    return HttpResponse(template.render(context, request))


def list_venue(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    venue = utils.venue.find({})
    template = loader.get_template('list_venue.html')
    glow = True;
    context = {
        'venue': venue,
        'glow_uv': glow,
        'account': account_a,
        'admin': admin
    }
    return HttpResponse(template.render(context, request))


def list_concert(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    concert = list(utils.concert.find({}))
    venue = list(utils.venue.find({}))
    template = loader.get_template('list_concert.html')
    glow = True;
    context = {
        'concert': concert,
        'glow_uc': glow,
        'venue': venue,
        'account': account_a,
        'admin': admin
    }
    return HttpResponse(template.render(context, request))


def edit_venue(request, ven_id):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')

    if request.method == 'POST':
        lines = request.POST['venue_seat_types'].splitlines()
        seats = []
        total_seats = 0;
        for line in lines:
            parts = line.split("-")
            sea = {"type": parts[0].strip(), "seats": int(parts[1].strip())}
            seats.append(sea)
            total_seats += sea['seats']

        if not (total_seats == int(request.POST['venue_totseats'])):
            errors = True;
            error = "The total number of seats for the venue does not match the sum of seats for all the seat types."
            template = loader.get_template('add_venue.html')
            context = {
                'er': errors,
                'err_msg': error,
                'admin': admin,
                'account': account_a
            }
            return HttpResponse(template.render(context, request))
        updatedvenue = {
            "venue_id": int(request.POST['venueID']),
            "name": request.POST['venue_name'],
            "email": request.POST['venue_email'],
            "phone_number": request.POST['venue_phone'],
            "image": request.POST['venue_image'],
            "country": request.POST['venue_country'],
            "province": request.POST['venue_province'],
            "street_address": request.POST['venue_streetaddress'],
            "city": request.POST['venue_city'],
            "postal_code": request.POST['venue_postalcode'],
            "total_seats": int(request.POST['venue_totseats']),
            "seat_types": seats
        }
        utils.venue.replace_one({'venue_id': ven_id}, updatedvenue)
        return render(request, 'added_venue.html',
                      {'venue': updatedvenue, 'account': account_a, 'admin': admin, 'message': "Edited"})

    e_venue = utils.venue.find_one({'venue_id': ven_id})
    template = loader.get_template('edit_venue.html')
    context = {
        'venue': e_venue,
        'account': account_a,
        'admin': admin
    }
    return HttpResponse(template.render(context, request));


def delete_venue(request, ven_id):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    d_venue = utils.venue.find_one({'venue_id': ven_id})
    utils.venue.delete_one({'venue_id': ven_id})
    venue = utils.venue.find({})
    template = loader.get_template('list_venue.html')
    glow = True;
    delete = True;
    context = {
        'venue': venue,
        'glow_uv': glow,
        'deleted': delete,
        'del_ven': d_venue,
        'account': account_a,
        'admin': admin
    }
    return HttpResponse(template.render(context, request))


def edit_concert(request, con_id):
    error = ''

    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    if request.method == 'POST':
        lines = request.POST['venue_seat_price'].splitlines()
        prices = []
        venue = utils.venue.find_one({'venue_id':int(request.POST['venueID'])})

        if len(lines)!=len(venue['seat_types']):
            error = "Number of types of seats should match the number of types in the chosen venue"
            venues = utils.venue.find({})
            concert = utils.concert.find_one({'concert_id': con_id})
            template = loader.get_template('edit_concert.html')
            context = {
                'venue': venues,
                'concert': concert,
                'account': account_a,
                'admin': admin,
                'err': error
            }
            return HttpResponse(template.render(context, request));
        total_s=0
        for line in lines:
            parts = line.split("-")

            if len(parts)==3:

                pri = {"type": parts[0].strip(), "price": float(parts[1].strip()), 'total':int(parts[2].strip()), 'booked':0}
                prices.append(pri)
                total_s+=int(parts[2].strip())
            else:
                error="Please provide all 3 arguments for seat price"
                venues = utils.venue.find({})
                concert = utils.concert.find_one({'concert_id': con_id})
                template = loader.get_template('edit_concert.html')
                context = {
                    'venue': venues,
                    'concert': concert,
                    'account': account_a,
                    'admin': admin,
                    'err': error
                }
                return HttpResponse(template.render(context, request));

        updatedConcert = {
            "venue_id": int(request.POST['venueID']),
            "concert_id": int(request.POST['concertID']),
            "concert_name": request.POST['concert_name'],
            "artist_name": request.POST['artist_name'].split(','),
            "genre": request.POST['artist_genre'].split(','),
            "image": request.POST['artist_image'],
            "date_time": (datetime.strptime(request.POST['concert_date_time'], '%Y-%m-%dT%H:%M')).strftime("%A, %B %d, %Y at %I:%M %p"),
            "doors_open": request.POST['concert_door_open'],
            "seats": prices
        }
        utils.concert.replace_one({'concert_id': con_id}, updatedConcert)

        return render(request, 'added_concert.html', {'concert': updatedConcert,'account': account_a, 'admin': admin, 'message':"Updated"})

    venue = utils.venue.find({})
    concert = utils.concert.find_one({'concert_id': con_id})
    concert['date_time'] = (datetime.strptime(concert['date_time'], "%A, %B %d, %Y at %I:%M %p")).strftime(
        "%Y-%m-%dT%H:%M")
    template = loader.get_template('edit_concert.html')
    context = {
        'venue': venue,
        'concert': concert,
        'account': account_a,
        'admin': admin,
        'err':error
    }
    return HttpResponse(template.render(context, request));


def delete_concert(request, con_id):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    d_concert = concert = utils.concert.find_one({'concert_id': con_id});
    utils.concert.delete_one({'concert_id': con_id})
    concert = list(utils.concert.find({}))
    venue = list(utils.venue.find({}))
    template = loader.get_template('list_concert.html')
    glow = True;
    delete = True;
    context = {
        'venue': venue,
        'concert': concert,
        'glow_uc': glow,
        'deleted': delete,
        'del_con': d_concert,
        'account': account_a,
        'admin': admin
    }
    return HttpResponse(template.render(context, request))


def delete_concert(request, con_id):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    d_concert = concert = utils.concert.find_one({'concert_id': con_id});
    utils.concert.delete_one({'concert_id': con_id})
    concert = list(utils.concert.find({}))
    venue = list(utils.venue.find({}))
    template = loader.get_template('list_concert.html')
    glow = True;
    delete = True;
    context = {
        'venue': venue,
        'concert': concert,
        'glow_uc': glow,
        'deleted': delete,
        'del_con': d_concert,
        'account': account_a,
        'admin': admin
    }
    return HttpResponse(template.render(context, request))


def delete_account(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            admin = False
        account_a = True
    else:
        return redirect('/signin/')
    if not check_password(request.POST['del_password'], user['password']):
        error = True
        err = "The Password is not Matching. Please Try Again."
    else:
        utils.user.delete_one({'user_id': request.session.get('user_id')})
        try:
            del request.session['user_id']
        except KeyError:
            pass
        return redirect('/')

    template = loader.get_template('account.html')
    glow = True;
    context = {
        'glow_p': glow,
        'account': account_a,
        'admin': admin,
        'error': error,
        'err': err
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.session.get('user_id'):
        user = utils.user.find_one({'user_id': request.session.get('user_id')})
        if user['account_type'] == 'admin':
            admin = True
        else:
            return redirect('/signin/')
        account_a = True
    else:
        return redirect('/signin/')

    return render(request, 'sign_up.html', {'account': account_a, 'admin': admin})
