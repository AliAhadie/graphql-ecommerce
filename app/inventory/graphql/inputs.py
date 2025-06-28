import strawberry
from strawberry import auto
import strawberry_django
from inventory.models import Category, Product, StockManagement
from typing import Optional
from decimal import Decimal


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

@strawberry.input
class UpdateProductInput:
    id: int  # required to look up the product
    name: str
    slug: str
    description: str
    is_digital: bool
    is_active: bool
    price: Decimal
    category_id: int

@strawberry.input
class PartialUpdateProductInput:
    id: int
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    is_digital: bool | None = None
    is_active: bool | None = None
    price: Decimal | None = None
    category_id: int | None = None

@strawberry.input
class CategoryFilter:
    is_active: bool |None=None
    name: str |None=None

@strawberry.input
class CategoryOrderFilter:
    field:str 
    direction:str  