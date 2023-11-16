from django.shortcuts import render, redirect
from django.http import HttpResponse
import utils


# Create your views here.
def checkout(request):
    if request.session.get('user_id'):
        account = True
        users = utils.user
        user = users.find_one({'user_id': request.session.get('user_id')})

        if 'cart' in user:
            user_data = user['cart']
        else:
            user_data = {'total': 0, 'tickets': []}
        user_data['tax'] = user_data['total'] * 0.13


        if request.method == 'POST':
            data = request.POST
            concert_id = int(data['concert'])
            concert = utils.concert.find_one({'concert_id': concert_id})
            inCart = []
            for ticket in user_data['tickets']:
                if ticket['concert_id'] == concert_id:
                    inCart.append(ticket)
            for seat in concert['seats']:
                seat_type = seat['type']
                seat_price = seat['price']

                seat_qty = int(data[seat_type])
                if seat_qty > 0:
                    user_data['tickets'].append({
                        'concert_id': concert_id,
                        "concert": concert['concert_name'],
                        'type': seat_type,
                        'price': seat_price,
                        'quantity': seat_qty,
                        'subtotal': seat_qty * seat_price
                    })
                    user_data['total'] += seat_qty * seat_price
                    user_data['tax'] = user_data['total'] * 0.13
                    user_data['amount_paid'] = user_data['total'] + user_data['tax']
                    seat['booked'] += seat_qty

            utils.concert.update_one(
                {'concert_id': concert_id},
                {'$set': concert})
            users.update_one(
                {'username': user['username']},
                {'$set': {'cart': user_data}})

            user = users.find_one({'user_id': request.session.get('user_id')})
            return render(request, 'checkout.html', {'account': account, 'user': user})

        else:
            user = users.find_one({'user_id': request.session.get('user_id')})
            return render(request, 'checkout.html', {'account': account, 'user': user})
    else:
        return redirect('/signin/')


def delete(request):
    users = utils.user
    user = users.find_one({'user_id': request.session.get('user_id')})
    user_data = {'total': 0, 'tickets': []}
    user_data['tax'] = user_data['total'] * 0.13
    users.update_one(
        {'username': user['username']},
        {'$set': {'cart': user_data}})
    user = users.find_one({'user_id': request.session.get('user_id')})
    return render(request, 'checkout.html', {'account': True, 'user': user})


def add(request, ticket):
    users = utils.user
    user = users.find_one({'user_id': request.session.get('user_id')})
    return render(request, 'checkout.html', {'account': True, 'user': user})


def deleteTicket(request, ticket):
    users = utils.user
    user = users.find_one({'user_id': request.session.get('user_id')})
    user['cart']['tickets'].remove(ticket)
    user = users.find_one({'user_id': request.session.get('user_id')})
    return render(request, 'checkout.html', {'account': True, 'user': user})

def clear(request):
    if request.session.get('user_id'):
        account = True
        users = utils.user
        concerts = utils.concert
        user = users.find_one({'user_id': request.session.get('user_id')})
        if 'cart' in user:
            data = user['cart']
        else:
            return redirect('/')
        newtickets = data['tickets']
        if 'tickets' in user:
            for x in user['tickets']:
                newtickets.append(x)
        users.update_one(
            {'user_id': request.session.get('user_id')},
            {'$set': {'tickets': newtickets}}
        )
        users.update_one(
            {'user_id': request.session.get('user_id')},
            {'$unset': {'cart': ""}}
        )
        return render(request, 'confirm.html', {'account': account})
