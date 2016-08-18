from django.db import models
from datetime import datetime, date

class City (models.Model):
    city_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.city_name


class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length=20,  unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.portfolio_name


class Property (models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    prop_name = models.CharField(max_length=250, unique=True)
    property_sf = models.FloatField()
    property_address = models.CharField(max_length=100)
    property_city = models.CharField(max_length=100)
    property_state = models.CharField(max_length=100)
    property_zip = models.CharField(max_length=100)
    def __str__(self):
        return self.prop_name


class Tenant (models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant_name = models.CharField(max_length=100)
    tenant_emergency_name = models.CharField(max_length=100)
    tenant_emergency_email = models.CharField(max_length=100)
    tenant_emergency_phone = models.CharField(max_length=100)
    tenant_site_name = models.CharField(max_length=100)
    tenant_site_email = models.CharField(max_length=100)
    tenant_site_phone = models.CharField(max_length=100)
    def __str__(self):
        return self.tenant_name


class Vendor (models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    vendor_contact = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    vendor_phone = models.CharField(max_length=100)


class Owner (models.Model):
    owner_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.owner_name


class Project (models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, null=True)
    tenant = models.ForeignKey(Tenant, blank=True, null=True)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    startdate = models.DateField(null=True)
    contractcomplete = models.NullBooleanField(default=False, blank=True, null=True)
    enddate = models.DateField(null=True)
    invoicestatus = models.CharField(max_length=100, blank=True, null=True)
    cmfeestatus = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name