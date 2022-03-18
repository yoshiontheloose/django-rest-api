from pyexpat import model
from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'description', 'created_at', 'updated_at')
    model = Pokemon