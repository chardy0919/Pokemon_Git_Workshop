# Create the "Moves" Django App

Create the Django app for Pokemon moves

1. Create the app. Important: Name it `moves_app`

2. Update `settings.py` accordingly

3. Add a route for moves to the django project `urls.py`. Here is the code, **don't forget to import whatever you need.**

```python
path('api/v1/moves/', include("move_app.urls")),
```