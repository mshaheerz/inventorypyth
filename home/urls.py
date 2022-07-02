from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    # registration urls
    path('shop_registration', views.shop_registration, name='shop_registration'),
    path('item_category_registration', views.item_category_registration, name='item_category_registration'),
    path('item_registration', views.item_registration, name='item_registration'),
    path('vehicle_registration', views.vehicle_registration, name='vehicle_registration'),
    path('route_registration', views.route_registration, name='route_registration'),
    path('warehouse_registration', views.warehouse_registration, name='warehouse_registration'),
    path('stock_registration', views.stock_registration, name='stock_registration'),
    path('vendor_registration', views.vendor_registration, name='vendor_registration'),
    path('town_registration', views.town_registration, name='town_registration'), 


    # assignment urls

    path('route_vehicle_assignment', views.route_vehicle_assignment, name='route_vehicle_assignment'),
    path('item_vehicle_assignment', views.item_vehicle_assignment, name='item_vehicle_assignment'),
    path('warehouse_warehouse_assignment', views.warehouse_warehouse_assignment, name='warehouse_warehouse_assignment'),


    # view urls
    path('shop_view', views.shop_view, name='shop_view'),
    path('item_view', views.item_view, name='item_view'),
    path('vehicle_view', views.vehicle_view, name='vehicle_view'),
    path('route_view', views.route_view, name='route_view'),
    path('warehouse_view', views.warehouse_view, name='warehouse_view'),
    path('stock_view', views.stock_view, name='stock_view'),
    path('bill_view', views.bill_view, name='bill_view'),
    path('sales_view', views.sales_view, name='sales_view'),

    # purchase urls
    path('purchase_item_add', views.purchase_item_add, name='purchase_item_add'),
    path('purchase_add', views.purchase_add, name='purchase_add'),
    path('purchase_list', views.purchase_list, name='purchase_list'),




]
