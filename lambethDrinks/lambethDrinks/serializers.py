# Describes process of going from Python to JSON object
from rest_framework import serializers
from .models import Drink

class DrinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']