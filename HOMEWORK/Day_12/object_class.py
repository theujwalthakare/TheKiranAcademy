# # there are few object class method

# | Method                          | Purpose / Usage                                          |
# | ------------------------------- | -------------------------------------------------------- |
# | `__init__(self, …)`             | Constructor / initializer for new instances              |
# | `__new__(cls, …)`               | Low-level instance creation before `__init__`            |
# | `__del__(self)`                 | Destructor (called when object is about to be destroyed) |
# | `__str__(self)`                 | User-friendly string representation (for `print()`)      |
# | `__repr__(self)`                | Official / unambiguous string representation             |
# | `__eq__(self, other)`           | Equality check using `==`                                |
# | `__ne__(self, other)`           | Inequality check `!=`                                    |
# | `__lt__(self, other)`           | Less than `<`                                            |
# | `__le__(self, other)`           | Less than or equal `<=`                                  |
# | `__gt__(self, other)`           | Greater than `>`                                         |
# | `__ge__(self, other)`           | Greater than or equal `>=`                               |
# | `__hash__(self)`                | Returns hash value for use in sets/dicts                 |
# | `__bool__(self)`                | Truthiness test via `bool()`                             |
# | `__format__(self, format_spec)` | Custom string formatting                                 |
# | `__sizeof__(self)`              | Returns size of the object in memory (in bytes)          |
# | `__class__`                     | Reference to the class of the instance                   |
