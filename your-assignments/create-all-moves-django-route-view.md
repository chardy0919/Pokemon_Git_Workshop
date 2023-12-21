# Create `all_moves` route and View Function

Create the Django route and view function for the `all_moves/` endpoint. It's full route should look like:

`GET api/v1/all_moves` and use serializers to return a list of all pokemon moves.

Here is the view function code. **Don't forget to import whatever you need**:

```python
# Create a view that utilizes APIView to inherit DRF's built in functionality
class All_moves(APIView):
    # establish a get method that will be triggered by GET requests
    def get(self, request):
        # utilize your ModelSerializer to serialize your queryset and return a proper response with DRF's Response
        moves = MoveSerializer(Move.objects.all(), many=True)
        return Response(moves.data)
```

Here is the routing code for `urls.py` in the Moves Django app. **Don't forget to import whatever you need**.

```python
path("", All_moves.as_view(), name="all_moves"),
```