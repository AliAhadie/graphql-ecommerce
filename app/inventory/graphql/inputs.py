import strawberry
from strawberry import auto
import strawberry_django
from inventory.models import Category, Product, StockManagement
from typing import Optional


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
    is_digital: Optional[bool] = None
    is_active: Optional[bool] = None
    price: auto
    category_id: int


@strawberry_django.input(StockManagement)
class StockManagementInput:
    id: auto
    quantity: auto
    last_checked_at: auto


@strawberry.input
class ProductWithStockInput(ProductInput):
    quantity: Optional[int] = None
