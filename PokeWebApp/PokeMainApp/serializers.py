from rest_framework.serializers import ModelSerializer
from .models import *


class PokemonApiSerializer(ModelSerializer):
    class Meta:
        model = UserPokemons
        fields = "__all__"
