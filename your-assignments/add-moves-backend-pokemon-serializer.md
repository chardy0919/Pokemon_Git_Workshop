# Have the Pokemon Serializer display Moves

Update the Pokemon serializer so it will serialize pokemon moves. Here is the full code. Please don't just delete the existing `PokemonSerializer` code - actually add relevant bits of this code to it:

1. Add `get_moves`
2. Create the moves `SerializerMethodField`
3. Add "moves" to `fields`

```python
class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level', 'moves'] # specify the fields you would like this serializer to return

    def get_moves(self, instance):
        moves = instance.moves.all()
        move_names = [move.name for move in moves]
        return move_names
```