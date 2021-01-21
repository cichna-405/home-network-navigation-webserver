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
    choices = Device._meta.get_field('type').choices

    for device in devices:
        current_device = Device.objects.get(id=device['id'])

        if current_device.default_url is not None:     # default url field
            device['default_url'] = {
                'url': current_device.default_url.url,
                'name': current_device.default_url.name,
            }

        for choice in choices:
            if choice[0] == current_device.type:
                device['type'] = choice[1]

        ip_add_numeric = ""  # numeric ip address for table sorting
        for octet in current_device.ip_address.split("."):
            while len(octet) < 3:
                octet = "0" + octet
            ip_add_numeric += octet
        device['ip_address_numeric'] = ip_add_numeric

    return render(request, 'index.html', {'devices': devices})
