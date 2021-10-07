from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics, permissions
from.models import *
from.serializers import *

class SupplierListView(generics.ListCreateAPIView):
    queryset=Supplier.objects.all()
    serializer_class= SupplierSerializer
  
class BuyerListView(generics.ListCreateAPIView):
    queryset=Buyer.objects.all()
    serializer_class= BuyerSerializer

class SeasonListView(generics.ListCreateAPIView):
    queryset=Season.objects.all()
    serializer_class= SeasonSerializer

class DropListView(generics.ListCreateAPIView):
    queryset=Drop.objects.all()
    serializer_class= DropSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer

class OrderListView(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class= OrderSerializer

class DeliveryListView(generics.ListCreateAPIView):
    queryset=Delivery.objects.all()
    serializer_class= DeliverySerializer




#detail_view
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Supplier.objects.all()
    serializer_class= SupplierSerializer

class BuyerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Buyer.objects.all()
    serializer_class= BuyerSerializer

class SeasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Season.objects.all()
    serializer_class= SeasonSerializer

class DropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Drop.objects.all()
    serializer_class= DropSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class= OrderSerializer

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Delivery.objects.all()
    serializer_class= DeliverySerializer        