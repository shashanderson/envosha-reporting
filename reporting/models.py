from __future__ import unicode_literals

from django.core.urlresolvers import reverse
# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    COUNTRIES = (
        ('MY', 'Malaysia'),
        ('SG', 'Singapore'),
    )
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    company_country = models.CharField(max_length=200, null=True, blank=True, choices=COUNTRIES)
    company_contact_no = models.CharField(max_length=200)
    company_pic = models.CharField(max_length=200)
    consultant = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ('company_name', 'company_country')

    def __unicode__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('company_edit', kwargs={'pk': self.pk})


class AreaPersonalType(models.Model):
    AREA_PERSONAL_TYPE = (('area', 'Area'),
                          ('personal', 'Personal'),
                          )
    CLASSIFICATION_TYPE = (('twa', 'TWA'),
                           ('mel', 'MEL'),
                           ('cl', 'CL'),
                           )
    company = models.ForeignKey(Company)
    point = models.CharField(max_length=200)
    work_unit = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    flow_rate = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    technique = models.CharField(max_length=200)
    area_personal_type = models.CharField(max_length=200, null=True, blank=True, choices=AREA_PERSONAL_TYPE)
    classification_type = models.CharField(max_length=200, null=True, blank=True, choices=CLASSIFICATION_TYPE)
    classification_value = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.CharField(max_length=200, null=True, blank=True)


    def __unicode__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('cem_edit', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('book_list', kwargs={'pk': self.pk})


class Parameter(models.Model):
    company = models.CharField(max_length=200)
    area_personal_type = models.CharField(max_length=200)
    point = models.CharField(max_length=200)
    parameter_value = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.CharField(max_length=200, null=True, blank=True)
