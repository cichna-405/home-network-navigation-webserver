# Generated by Django 3.1.5 on 2021-01-12 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210112_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='device_id',
            new_name='device',
        ),
    ]