from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse
from django.views.defaults import page_not_found
import json
import requests
from django.conf import settings
from app.models import Device, Url


# Create your views here.


def index(request):
    if request.method == "GET":
        devices = Device.objects.all().values()
        '''return render(request, 'index.html', {
            'devices': devices,
        })'''

        print(devices)

        for device in devices:
            device['urls'] = Device.objects.get(id=device['id']).urls.all()

        return render(request, 'index.html', {'devices': devices})
