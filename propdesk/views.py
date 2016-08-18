from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Property, City, Portfolio
from .forms import ProjectForm, VendorForm, TenantForm
import operator
from django.db.models import Q

def index(request):
    all_cities = City.objects.prefetch_related('portfolio_set').all()
    context = {
        'all_cities': all_cities,
    }
    return render(request, 'propdesk/index.html', context)


def portview(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'propdesk/portview.html', {'portfolio': portfolio })


def prop(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    property_related = Property.objects.prefetch_related('property_set').all()
    return render(request, 'propdesk/prop.html', {'property': property, 'property_related': property_related })


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
    else:
        form = ProjectForm()
    return render(request, 'propdesk/project_new.html', {'form': form})


def tenant_new(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            tenant.save()
    else:
        form = TenantForm()
    return render(request, 'propdesk/tenant_new.html', {'form': form})


def vendor_new(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.save()
    else:
        form = VendorForm()
    return render(request, 'propdesk/vendor_new.html', {'form': form})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        properties = Property.objects.filter(prop_name__icontains=q)
        return render(request, 'propdesk/search_results.html',
            {'properties': properties, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')