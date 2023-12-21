# Create `a_move` route and View Function

Create the Django route and view function for the `a_move/` endpoint. It's full route should look like:

`GET api/v1/a_move/<str:name>/` and use serializers to return a list of all pokemon moves.

Here is the view function code. **Don't forget to import whatever you need**:

```python
class A_move(APIView):
    def get(self, request, name):
        move = Move.objects.get(name = name.title())
        return Response(MoveSerializer(move).data)
```

Here is the routing code for `urls.py` in the Moves Django app. **Don't forget to import whatever you need**.

```python
path("<str:name>/", A_move.as_view(), name="a_move"),
```