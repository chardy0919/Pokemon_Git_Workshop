# Create Moves Django Validator

Create the validator function for Moves. This will be used in the Moves Django Model, which another team member will create. Here is the code:

```python
from django.core.exceptions import ValidationError
import re

def validate_move_name(name):
    regex = r"^[a-zA-Z]+ ?[a-zA-Z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError("Improper Format")
```