from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# index page
def index(request):

    return render(request, 'index.html')


# registration routes
def shop_registration(request):

    return render(request, 'shop-registration.html')

def item_category_registration(request):

    return render(request, 'item-category-registration.html')

def item_registration(request):

    return render(request, 'item-registration.html')

def vehicle_registration(request):

    return render(request, 'vehicle-registration.html')


def route_registration(request):

    return render(request, 'route-registration.html')


def warehouse_registration(request):

    return render(request, 'warehouse-registration.html')

def town_registration(request):

    return render(request, 'town-registration.html')

def stock_registration(request):

    return render(request, 'stock-registration.html')

def vendor_registration(request):

    return render(request, 'vendor-registration.html')



# assignment routes
def route_vehicle_assignment(request):

    return render(request, 'route-vehicle-assignment.html')

def item_vehicle_assignment(request):

    return render(request, 'item-vehicle-assignment.html')

def warehouse_warehouse_assignment(request):

    return render(request, 'warehouse-warehouse-assignment.html')



# view routes


def sales_view(request):

    return render(request, 'sales-view.html')

def stock_view(request):

    return render(request, 'stock-view.html')

def shop_view(request):

    return render(request, 'shop-view.html')

def item_view(request):

    return render(request, 'item-view.html')

def vehicle_view(request):

    return render(request, 'vehicle-view.html')

def route_view(request):

    return render(request, 'route-view.html')


def warehouse_view(request):

    return render(request, 'warehouse-view.html')

def bill_view(request):

    return render(request, 'bill-view.html')


# purchase routes
def purchase_item_add(request):
    
    return render(request, 'purchase-item-add.html')

def purchase_add(request):
    
    return render(request, 'purchase-add.html')

def purchase_list(request):
    
    return render(request, 'purchase-list.html')