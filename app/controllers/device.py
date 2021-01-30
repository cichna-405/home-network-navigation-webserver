from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.defaults import page_not_found
import json
import requests
from django.conf import settings
from app.models import Device, Url
from app.decorators import login_required
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# Create your views here.


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "GET":
        choices = Device._meta.get_field('type').choices
        return render(request, 'device/create.html', {'choices': choices})  # choices = array of possible device types

    else:
        device_type = request.POST.get('type')  # device type
        if not device_type:
            device_type = 'UK'

        new_device = Device.objects.create(  # device creation
            type=device_type,
            ip_address=request.POST.get('ip_address'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        new_device.save()
        messages.success(request, 'Vytvořeno zařízení ' + new_device.name + ".")

        i = 1
        x = 0
        validate = URLValidator()

        while True:  # urls creation
            url_name = request.POST.get('url_' + str(i) + '_name')
            url_url = request.POST.get('url_' + str(i) + '_url')

            if not url_name or not url_url:
                break
            try:
                validate(url_url)
                x += 1
                new_url = Url.objects.create(
                    name=url_name,
                    url=url_url,
                    device=new_device,
                )
                new_url.save()
                messages.success(request, 'URL ' + url_name + ' byla úspěšně vytvořena.')

                if x == 1:  # set default_url for the device
                    Device.objects.filter(ip_address=new_device.ip_address).update(default_url=new_url)

            except ValidationError:
                messages.error(request, 'URL ' + url_name + ' byla ve špatném formátu. Vytvořte novou na stránce pro'
                                                            ' editaci zařízení.')

            i += 1

        return redirect('index')


@login_required
@require_http_methods(['GET', 'POST'])
def edit(request, device_id):
    device = Device.objects.get(id=device_id)

    if request.method == "GET":
        choices = Device._meta.get_field('type').choices

        return render(request, 'device/edit.html', {
            'device': device,
            'urls': device.urls.all(),
            'choices': choices,
        })

    else:
        updated_device = {
            "name": request.POST.get('name'),
            "ip_address": request.POST.get('ip_address'),
            "description": request.POST.get('description'),
        }

        device_type = request.POST.get('type')
        if not device_type:
            updated_device["type"] = "UK"
        else:
            updated_device["type"] = device_type,

        default_url = request.POST.get('default_url')
        if default_url:
            updated_device["default_url"] = Url.objects.get(id=int(default_url))
        else:
            updated_device["default_url"] = None

        if updated_device["name"] != device.name and updated_device["name"]:
            device.name = updated_device["name"]
        device.type = updated_device["type"][0]
        if updated_device["ip_address"] != device.ip_address and updated_device["ip_address"]:
            device.ip_address = updated_device["ip_address"]
        if updated_device["default_url"] != device.default_url:
            device.default_url = updated_device["default_url"]
        if updated_device["description"] != device.description:
            device.description = updated_device["description"]

        device.save()

        messages.success(request, 'Změněno zařízení ' + device.name + ".")
        return redirect('device edit', device_id)


@login_required
@require_http_methods(['POST'])
def delete(request, device_id):
    device = Device.objects.get(id=device_id)
    deleted = device.delete()
    if deleted:
        messages.success(request, "Smazáno zařízení " + device.name + ".")
    else:
        messages.error(request, "Nelze smazat zařízení " + device.name + ".")
    return redirect('index')


@require_http_methods(['GET'])
def urls(request, device_id):
    device = Device.objects.get(id=device_id)

    return render(request, 'device/urls.html', {
        'device': device,
        'urls': device.urls.all(),
    })


@login_required
@require_http_methods(['POST'])
def delete_url(request, device_id, url_id):
    deleted = Url.objects.get(id=int(url_id)).delete()
    if deleted:
        messages.success(request, 'URL ' + url_id + ' byla smazána.')
    else:
        messages.error(request, 'URL ' + url_id + ' nelze smazat.')
    return redirect('device edit', device_id)


@login_required
@require_http_methods(['POST'])
def edit_url(request, device_id, url_id):
    validate = URLValidator()
    url_name = request.POST.get('name')
    url_url = request.POST.get('url')
    try:
        validate(url_url)
        url = Url.objects.get(id=int(url_id))
        url.name = url_name
        url.url = url_url
        url.save()
        messages.success(request, 'URL ' + url_id + ' byla změněna.')
    except ValidationError:
        messages.error(request, 'Adresa URL ' + url_name + " nemá platný formát.")
    return redirect('device edit', device_id)


@login_required
@require_http_methods(['POST'])
def create_url(request, device_id):
    validate = URLValidator()
    new_url_device = Device.objects.get(id=int(device_id))
    new_url_name = request.POST.get('new_name')
    new_url_url = request.POST.get('new_url')
    try:
        validate(new_url_url)
        new_url = Url.objects.create(
            device=new_url_device,
            name=new_url_name,
            url=new_url_url,
        )
        new_url.save()
        messages.success(request, 'URL ' + new_url_name + ' byla vytvořena.')
    except ValidationError:
        messages.error(request, 'Adresa URL ' + new_url_name + " nemá platný formát.")
    return redirect('device edit', device_id)
