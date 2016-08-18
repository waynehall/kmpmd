from django import forms
from .models import Project, Tenant, Vendor


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('property', 'portfolio', 'tenant', 'type', 'name', 'startdate', 'contractcomplete', 'enddate', 'invoicestatus', 'cmfeestatus')


class TenantForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = ('property', 'tenant_name', 'tenant_emergency_name', 'tenant_emergency_email', 'tenant_emergency_phone', 'tenant_site_name', 'tenant_site_email', 'tenant_site_phone')

class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ('property', 'vendor_name', 'vendor_contact', 'vendor_email', 'vendor_phone')