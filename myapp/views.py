from rest_framework import viewsets  # Viewsets ko import karenge
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# ItemViewSet class ko define karenge
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # Saare items ko query karega
    serializer_class = ItemSerializer

# Create Item function for POST request
@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()  # Item ko save karega
            return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)  # Find the item by primary key
    except Item.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    item.delete()  # Delete the item
    return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content on success

@api_view(['PUT'])  # Only allow PUT method for update
def update_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)  # Find the item by primary key
    except Item.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    # Use the serializer to validate and save the updated data
    serializer = ItemSerializer(item, data=request.data)  # Full update, no partial=True

    if serializer.is_valid():
        serializer.save()  # Save the updated data to the database
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)