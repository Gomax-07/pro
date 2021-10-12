from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def supplier_lists(request):
  """
  List all suppliers or create a new supplier.
  """
    
  if request.method == 'GET':
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def buyer_lists(request):
  """
  List all buyers or create a new buyer.
  """
    
  if request.method == 'GET':
    buyers = Buyer.objects.all()
    serializer = BuyerSerializer(buyers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = BuyerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def season_lists(request):
  """
  List all seasons or create a new season.
  """
    
  if request.method == 'GET':
    seasons = Season.objects.all()
    serializer = SeasonSerializer(seasons, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SeasonSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def drop_lists(request):
  """
  List all drops or create a new drop.
  """
    
  if request.method == 'GET':
    drops = Drop.objects.all()
    serializer = DropSerializer(drops, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = DropSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def product_lists(request):
  """
  List all products or create a new product.
  """
    
  if request.method == 'GET':
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def order_lists(request):
  """
  List all orders or create a new order.
  """
    
  if request.method == 'GET':
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def delivery_lists(request):
  """
  List all deliverys or create a new delivery.
  """
    
  if request.method == 'GET':
    deliverys = Delivery.objects.all()
    serializer = DeliverySerializer(deliverys, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#details fn(s)

@api_view(['GET', 'PUT', 'DELETE'])
def supplier_details(request, slug):
  """
  update or delete a single supplier.
  """
  try:
    supplier = Supplier.objects.get(slug=slug)
  except Supplier.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = SupplierSerializer(supplier)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = SupplierSerializer(supplier, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    supplier.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])
def buyer_details(request, slug):
  """
  update or delete a single buyer.
  """
  try:
    buyer = Buyer.objects.get(slug=slug)
  except Buyer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = BuyerSerializer(buyer)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = BuyerSerializer(buyer, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    buyer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def season_details(request, slug):
  """
  update or delete a single season.
  """
  try:
    season = Season.objects.get(slug=slug)
  except Season.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = SeasonSerializer(season)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = SeasonSerializer(season, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    season.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def drop_details(request, slug):
  """
  update or delete a single drop.
  """
  try:
    drop = Drop.objects.get(slug=slug)
  except Drop.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = DropSerializer(drop)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = DropSerializer(drop, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    drop.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, slug):
  """
  update or delete a single product.
  """
  try:
    product = Product.objects.get(slug=slug)
  except Product.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = ProductSerializer(product)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def order_details(request, slug):
  """
  update or delete a single order.
  """
  try:
    order = Order.objects.get(slug=slug)
  except Order.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = OrderSerializer(order)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def delivery_details(request, slug):
  """
  update or delete a single delivery.
  """
  try:
    delivery = Delivery.objects.get(slug=slug)
  except Delivery.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = DeliverySerializer(delivery)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = DeliverySerializer(delivery, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    delivery.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)