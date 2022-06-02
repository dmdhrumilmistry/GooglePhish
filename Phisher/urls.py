from django.urls import path
from Phisher import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin' ),
    path('error', views.error, name='error'),
]
