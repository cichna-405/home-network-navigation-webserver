from django.db import models

# Create your models here.


class Device(models.Model):
    TYPES = [
        ('UK', 'Neznámé'),
        ('RT', 'Směrovač'),
        ('AP', 'Přístupový bod'),
        ('NS', 'Síťové úložiště'),
        ('PT', 'Tiskárna'),
        ('MC', 'Multimediální centrum'),
        ('PC', 'Stolní počítač'),
        ('NB', 'Notebook'),
        ('MB', 'Mobilní telefon'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPES,
        default='UK',
    )
    ip_address = models.CharField(
        max_length=15,
        unique=True,
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    default_url = models.OneToOneField(
        'Url',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='default_for_device',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(type) + ' ' + str(self.name)


class Url(models.Model):
    device = models.ForeignKey(
        'Device',
        on_delete=models.CASCADE,
        related_name='urls',
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=80,
        null=False,
        blank=False,
        default='Neznámá URL',
    )
    url = models.URLField(
        null=False,
        blank=False,
    )
