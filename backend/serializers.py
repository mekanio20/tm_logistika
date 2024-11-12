# backend/serializers.py

from rest_framework import serializers
from .models import *

class HomeSlidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSliders
        fields = '__all__'

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
    
    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.header_image:
            return request.build_absolute_uri(obj.header_image.url)
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.header_image:
            return request.build_absolute_uri(obj.header_image.url)
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.header_image:
            return request.build_absolute_uri(obj.header_image.url)
        return None

class LicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenses
        fields = '__all__'

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = '__all__'

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class CargoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargoes
        fields = '__all__'

    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None