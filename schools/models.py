from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

PROVINCE_CHOICES = [
    ('Northern Province', 'Northern Province'),
    ('Eastern Province', 'Eastern Province'),
    ('Western Province', 'Western Province'),
    ('Southern Province', 'Southern Province'),
    ('Kigali City', 'Kigali City'),

]

LEVEL_CHOICES = [
    ('Pre-Nursery', 'Pre-Nursery'),
    ('Nursery', 'Nursery'),
    ('Primary', 'Primary'),
    ('General Secondary', 'General Secondary'),
    ('TVET', 'TVET'),
    ('General Tertiary', 'General Tertiary'),
    ('Adult Literacy', 'Adult Literacy'),

]


class School(models.Model):
    name = models.CharField(_('School Name'), max_length=100, unique=True)
    province = models.CharField(
        _('School Province'), max_length=30, choices=PROVINCE_CHOICES)
    district = models.CharField(_('School District'), max_length=50)
    level = models.CharField(
        _('School Level'), max_length=30, choices=LEVEL_CHOICES)
    male = models.IntegerField(_('Male Students'), default=0)
    female = models.IntegerField(_('Female Students'), default=0)
    electricity_availability = models.BooleanField(
        _('Electricity Availability'), default=False)
    school_code = models.IntegerField(_('School Code'), default=0)
    location = models.PointField(_('School location'), srid=4326)
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Date Updated'), auto_now=False)

    def __str__(self):
        return self.name

    def get_school_first_name(self):
        return self.name.split()[0]
