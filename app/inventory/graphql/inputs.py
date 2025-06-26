import strawberry
from strawberry import auto
import strawberry_django
from inventory.models import Category


@strawberry_django.input(Category)
class CategoryInput:
    name: auto
    slug: auto
    is_active: auto
    level: auto
    parent_id: int | None = None