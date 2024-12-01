from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inventory
from .serializers import InventorySerializer


class InventoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        else:
            inventory = Inventory.objects.all()
            serializer = InventorySerializer(inventory, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
