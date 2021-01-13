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
    if request.method == "GET":
        choices = Device._meta.get_field('type').choices
        return render(request, 'device/create.html', {'choices': choices})      # choices = array of possible device types
    else:
        device_type = request.POST.get('type')

        if not device_type:
            device_type = 'Neznámé'

        new_device = Device.objects.create(
            type=device_type,
            ip_address=request.POST.get('ip_address'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        new_device.save()
        messages.success(request, 'Created device ' + new_device.name)
        return redirect('index')


# DOPSAT

@require_http_methods(['GET', 'POST'])
def edit(request, device_id):
    device = Device.objects.get(id=device_id)
    if request.method == "GET":
        return render(request, 'device/edit.html', {'device': device})
    else:
        messages.success(request, 'Edited device ' + str(device.name))
        return redirect('index')


# DOPSAT

@require_http_methods(['POST'])
def delete(request, device_id):
    device = Device.objects.get(id=device_id)
    messages.success(request, 'Deleted device ' + device.name)
    return redirect('index')


# DOPSAT

def urls(request, device_id):
    device = Device.objects.get(id=device_id)
    return render(request, 'device/urls.html', {'device': device})