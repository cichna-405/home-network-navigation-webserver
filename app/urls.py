"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .controllers import home, device, users

urlpatterns = [
    path('', home.index, name="index"),
    path('admin/', admin.site.urls),
    path('users/login', users.login, name="login"),
    path('users/logout', users.logout, name="logout"),
    path('device/create', device.create, name="device create"),
    path('device/<device_id>/urls', device.urls, name="device urls"),
    path('device/<device_id>/urls/create', device.create_url, name="device create_url"),
    path('device/<device_id>/urls/<url_id>/delete', device.delete_url, name="device delete_url"),
    path('device/<device_id>/urls/<url_id>/edit', device.edit_url, name="device edit_url"),
    path('device/<device_id>/edit', device.edit, name="device edit"),
    path('device/<device_id>/delete', device.delete, name="device delete"),
]