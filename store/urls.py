from django.urls import path
from.views import *
from store import function_views
from store.class_based_views import*
urlpatterns=[
  #supplier
  path('supplier/<int:pk>/', SupplierDetail.as_view(), name='supplier_detail'),
  path('supplier/', SupplierListView.as_view(), name='supplier_list'),
  #Buyer
  path('buyer/<int:pk>/', BuyerDetail.as_view(), name='buyer_detail'),
  path('buyer/', BuyerListView.as_view(), name='buyer_detail'),
  #Season
  path('season/<int:pk>/', SeasonDetail.as_view(), name='season_detail'),
  path('buyer/', SeasonListView.as_view(), name='season_list'),
  #Drop
  path('drop/<int:pk>/', DropDetail.as_view(), name='drop_detail'),
  path('buyer/', DropListView.as_view(), name='drop_list'),
  #Product
  path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
  path('product/', ProductListView.as_view(), name='product_list'),
  #Order
  path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
  path('order/', OrderListView.as_view(), name='order_list'),
  #Delivery
  path('delivery/<int:pk>/', DeliveryDetail.as_view(), name='delivery_detail'),
  path('delivery/', DeliveryListView.as_view(), name='delivery_list'),

  ]