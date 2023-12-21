# Add moves to Django Pokemon model

Update our Pokemon model to have moves. Also update pokemon fixture data to have some moves if you can.
Here's the code you'll want to add to the pokemon model:

```python
moves = models.ManyToManyField(Move, related_name="pokemon")

**Don't forget to run migrations**. Don't forget to import what you need.

```