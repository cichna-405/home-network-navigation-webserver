from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse
from django.views.defaults import page_not_found
from django.views.decorators.http import require_http_methods
import json
import requests
from django.conf import settings
from app.models import Device, Url


# Create your views here.


@require_http_methods(['GET'])
def index(request):
    devices = Device.objects.all().values()

    for device in devices:
        if Device.objects.get(id=device['id']).urls.all().exists():
            device['urls'] = Device.objects.get(id=device['id']).urls.all()

    return render(request, 'index.html', {'devices': devices})
