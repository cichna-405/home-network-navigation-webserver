# Generated by Django 3.1.4 on 2021-01-21 12:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_device_default_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='default_url',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_for_device', to='app.url', validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='device',
            name='ip_address',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(7)]),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='url',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
