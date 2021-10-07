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
    

