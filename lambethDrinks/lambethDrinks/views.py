from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers

def drink_list(request):
    # Get all the drinks
    drinks = Drink.objects.all()
    # Serialize them
    serializer = DrinkSerializers(drinks,many=True)
    # Return them
    return JsonResponse({'drinks': serializer.data}, safe=False)