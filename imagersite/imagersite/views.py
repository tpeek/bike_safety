from django.shortcuts import render
from imager_images.models import Photo
from django.contrib.gis.geoip import GeoIP


def home_view(request):
    photos = Photo.objects.all()
    try:
        pic_url = Photo.objects.filter(
            privacy='Public').last()
    except AttributeError:
        pic_url = ''
    return render(request, 'home.html', {'pic_url': pic_url, 'photos': photos})


def auth_view(request):
    return
