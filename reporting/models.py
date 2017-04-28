from __future__ import unicode_literals

# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    company_contact_no = models.CharField(max_length=200)
    pic_name = models.CharField(max_length=200)
    consultant = models.CharField(max_length=200)


class Type(models.Model):
    company_name = models.CharField(max_length=200)
    point = models.CharField(max_length=200)
    work_unit = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    flow_rate = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    technique = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    classification_value = models.CharField(max_length=200)


class Parameter(models.Model):
    company_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    point = models.CharField(max_length=200)
    parameter_value = models.CharField(max_length=200)
