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
    type = models.CharField(max_length=2, choices=TYPES, default='UK')
    ip_address = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(type) + ' ' + str(self.name)


class Url(models.Model):
    device_id = models.ForeignKey('Device', on_delete=models.CASCADE, related_name='urls')
    name = models.CharField(max_length=80, default='Neznámá URL')
    url = models.URLField()
