# backend/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class HomeSlidersView(APIView):
    def get(self, request):
        slider_items = HomeSliders.objects.all()
        serializer = HomeSlidersSerializer(slider_items, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class AboutView(APIView):
    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ServiceView(APIView):
    def get(self, request):
        about = Service.objects.all()
        serializer = ServiceSerializer(about, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContactView(APIView):
    def get(self, request):
        about = Contact.objects.all()
        serializer = ContactSerializer(about, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class LicensesView(APIView):
    def get(self, request):
        about = Licenses.objects.all()
        serializer = LicensesSerializer(about, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class OurServicesView(APIView):
    def get(self, request):
        about = OurServices.objects.all()
        serializer = OurServicesSerializer(about, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CargoesView(APIView):
    def get(self, request):
        about = Cargoes.objects.all()
        serializer = CargoesSerializer(about, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)