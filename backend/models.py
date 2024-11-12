from django.conf import settings
from django.db import models
import os


class HomeSliders(models.Model):
    image = models.ImageField(upload_to='images/')

    def get_full_image_url(self):
        if self.image:
            return f"{settings.MEDIA_URL}{self.image.url}"
        return None

    def __str__(self):
        return f"image -- {self.image}"


class About(models.Model):
    header_image = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    def get_full_header_image_path(self):
        if self.header_image:
            return os.path.join(settings.IMAGE_ROOT, self.header_image.name)
        return None
    def get_full_image_path(self):
        if self.image:
            return os.path.join(settings.IMAGE_ROOT, self.image.name)
        return None
    def __str__(self):
        return f"header_image -- {self.header_image}: image -- {self.image}"

class Service(models.Model):
    header_image = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    def get_full_header_image_path(self):
        if self.header_image:
            return os.path.join(settings.IMAGE_ROOT, self.header_image.name)
        return None
    def get_full_image_path(self):
        if self.image:
            return os.path.join(settings.IMAGE_ROOT, self.image.name)
        return None
    def __str__(self):
        return f"header_image -- {self.header_image}: image -- {self.image}"

class Contact(models.Model):
    header_image = models.ImageField(upload_to='images/')
    def get_full_header_image_path(self):
        if self.header_image:
            return os.path.join(settings.IMAGE_ROOT, self.header_image.name)
        return None
    def __str__(self):
        return f"header_image -- {self.header_image}"

class Licenses(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    def get_full_image_path(self):
        if self.image:
            return os.path.join(settings.IMAGE_ROOT, self.image.name)
        return None
    def __str__(self):
        return f"{self.name}: {self.image}"

class OurServices(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    def get_full_image_path(self):
        if self.image:
            return os.path.join(settings.IMAGE_ROOT, self.image.name)
        return None
    def __str__(self):
        return f"{self.name}: {self.image}"

class Cargoes(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    def get_full_image_path(self):
        if self.image:
            return os.path.join(settings.IMAGE_ROOT, self.image.name)
        return None
    def __str__(self):
        return f"{self.name}: {self.image}"