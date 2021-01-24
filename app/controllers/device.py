from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.defaults import page_not_found
import json
import requests
from django.conf import settings
from app.models import Device, Url


# Create your views here.


@require_http_methods(['GET', 'POST'])
def create(request):
    # TODO: validation
    if request.user.is_authenticated:
        if request.method == "GET":
            choices = Device._meta.get_field('type').choices
            return render(request, 'device/create.html', {'choices': choices})  # choices = array of possible device types

        else:
            device_type = request.POST.get('type')                              # device type
            if not device_type:
                device_type = 'UK'

            new_device = Device.objects.create(                                 # device creation
                type=device_type,
                ip_address=request.POST.get('ip_address'),
                name=request.POST.get('name'),
                description=request.POST.get('description'),
            )
            new_device.save()

            i = 1
            while True:                                                         # urls creation
                url_name = request.POST.get('url_' + str(i) + '_name')
                url_url = request.POST.get('url_' + str(i) + '_url')
                if not url_name or not url_url:
                    break
                new_url = Url.objects.create(
                    name=url_name,
                    url=url_url,
                    device=new_device,
                )
                new_url.save()

                if i is 1:                                                      # set default_url for the device
                    Device.objects.filter(ip_address=new_device.ip_address).update(default_url=new_url)

                i += 1

            messages.success(request, 'Vytvořeno zařízení ' + new_device.name + ".")
            return redirect('index')

    else:
        messages.error(request, 'Přístup zablokován.')
        return redirect('index')


# TODO: write edit method

@require_http_methods(['GET', 'POST'])
def edit(request, device_id):
    # TODO: validation
    if request.user.is_authenticated:
        device = Device.objects.get(id=device_id)
        if request.method == "GET":
            if device.urls.all().exists():
                device['urls'] = device.urls.all()
            return render(request, 'device/edit.html', {'device': device})
        else:
            messages.success(request, 'Změněno zařízení ' + str(device.name) + ".")
            return redirect('index')
    else:
        messages.error(request, "Přístup zablokován.")
        return redirect('index')


@require_http_methods(['POST'])
def delete(request, device_id):
    if request.user.is_authenticated:
        device = Device.objects.get(id=device_id)
        deleted = Device.objects.get(id=device_id).delete()
        if deleted:
            messages.success(request, "Smazáno zařízení " + device.name + ".")
        else:
            messages.error(request, "Nelze smazat zařízení " + device.name + ".")
        return redirect('index')
    else:
        messages.error(request, "Přístup zablokován.")
        return redirect('index')


@require_http_methods(['GET'])
def urls(request, device_id):
    device = Device.objects.get(id=device_id)

    return render(request, 'device/urls.html', {
        'device': device,
        'urls': device.urls.all(),
    })
