import strawberry
from strawberry import auto
import strawberry_django
from inventory.models import Category,Product


@strawberry_django.input(Category)
class CategoryInput:
    name: auto
    slug: auto
    is_active: auto
    level: auto
    parent_id: int | None = None

@strawberry_django.input(Product)
class ProductInput:
    name: auto
    slug: auto
    description: auto
    is_digital: auto
    is_active: auto
    price: auto
    category_id: int