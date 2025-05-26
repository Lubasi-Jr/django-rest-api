from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request):
    if(request.method == 'GET'):
        # Get all the drinks
        drinks = Drink.objects.all()
        # Serialize them
        serializer = DrinkSerializers(drinks,many=True)
        # Return them
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    if request.method == 'POST':
        # Take the data that was sent
        serializer = DrinkSerializers(data=request.data)
        # Deserialize it
        # Create a drink object and store it
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

api_view(['GET','PUT','DELETE'])       
def drink_details(request,id):
    # Try catch block to check if its a valid request
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Valid request; perform different function according to the method
    if (request.method == 'GET'):
        serializer = DrinkSerializers(drink)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        serializer = DrinkSerializers(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif (request.method == 'DELETE'):
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    