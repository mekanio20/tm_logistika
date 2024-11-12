"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sliders/', HomeSlidersView.as_view(), name='slider-list'),
    path('api/about/', AboutView.as_view(), name='about'),
    path('api/service/', ServiceView.as_view(), name='service'),
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('api/licenses/', LicensesView.as_view(), name='licenses'),
    path('api/our-service/', OurServicesView.as_view(), name='our-service'),
    path('api/cargoes/', CargoesView.as_view(), name='cargoes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)