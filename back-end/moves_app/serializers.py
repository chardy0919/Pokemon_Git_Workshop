from rest_framework import serializers # import serializers from DRF
from .models import Move # import Pokemon model from models.py

class MoveSerializer(serializers.ModelSerializer):
    pokemon = serializers.SerializerMethodField()

    class Meta:
        model = Move
        fields = ['id', 'name', 'power', 'accuracy', 'pokemon']

    def get_pokemon(self, obj):
        pokemon = obj.pokemon.all()
        pokemon = [x.name for x in pokemon]
        return pokemon