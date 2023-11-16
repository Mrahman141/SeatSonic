from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.template import loader
from django.http import HttpResponse
import utils


def signin(request):
    if request.session.get('user_id'):
        return redirect('/')
    else:
        account = False
    if request.method == 'POST':
        if not utils.user.find_one({'username': request.POST['login_username']}) is not None:
            errors = True;
            error = "Password or username is incorrect."
            template = loader.get_template('sign_in.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))
        user_account = utils.user.find_one({'username': request.POST['login_username']})
        if not check_password(request.POST['login_password'], user_account['password']):
            errors = True;
            error = "Password or username is incorrect."
            template = loader.get_template('sign_in.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))
        request.session['user_id'] = user_account['user_id']
        return redirect('/')

    return render(request, 'sign_in.html', {'account': account})


def signup(request):
    if request.session.get('user_id'):
        account = True
    else:
        account = False
    if request.method == 'POST':
        user_count = utils.user.count_documents({});
        user_count = user_count + 1;
        while (utils.user.find_one({'user_id': user_count}) is not None):
            user_count = user_count + 1;

        if not check_password(request.POST['user_confirm_password'], make_password(request.POST['user_password'])):
            errors = True;
            error = "The Password is not matching."
            template = loader.get_template('sign_up.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))

        if utils.user.find_one({'email': request.POST['user_email']}) is not None:
            errors = True;
            error = "The E-mail is already associated with another account."
            template = loader.get_template('sign_up.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))

        if utils.user.find_one({'username': request.POST['username']}) is not None:
            errors = True;
            error = "The username is already associated with another account."
            template = loader.get_template('sign_up.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))




        newuser = {
            'user_id': user_count,
            'username': request.POST['username'],
            'fname': request.POST['user_f_name'],
            'lname': request.POST['user_l_name'],
            'email': request.POST['user_email'],
            'password': make_password(request.POST['user_password']),
            'gender': request.POST['user_gender'],
            'province': request.POST['user_province'],
            'street_address': request.POST['user_street_address'],
            'country': request.POST['user_country'],
            'account_type': request.POST['user_account_type'],
        }
        utils.user.insert_many([newuser])
        created = True;
        msg = "Account Created Successfully."
        if account==True:
            return redirect('/')
        else:
            template = loader.get_template('sign_in.html')
        context = {
            'created': created,
            'account': account,
            'msg': msg
        }
        return HttpResponse(template.render(context, request))

    return render(request, 'sign_up.html', {'account': account})


def forgotpassword(request):
    if request.session.get('user_id'):
        return redirect('/')
    else:
        account = False
    if request.method == 'POST':
        username = request.POST['forgot_username']
        email = request.POST['forgot_user_email']

        if not (utils.user.find_one({'username': username}) and utils.user.find_one({'email': email})):
            errors = True
            error = "Email or username is not associated with the same account."
            template = loader.get_template('forgot_password.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))

        if not (request.POST['user_password'] == request.POST['user_confirm_password']):
            errors = True;
            error = "Passwords are not matching."
            template = loader.get_template('forgot_password.html')
            context = {
                'error': error,
                'errors': errors,
                'account': account
            }
            return HttpResponse(template.render(context, request))

        utils.user.update_one({'username': request.POST['forgot_username']}, {'$set': {'password': make_password(request.POST['user_password'])}})
        created = True;
        msg = "Password reset successful."
        template = loader.get_template('sign_in.html')
        context = {
            'created': created,
            'account': account,
            'msg': msg
        }
        return HttpResponse(template.render(context, request))

    return render(request, 'forgot_password.html', {'account': account})
