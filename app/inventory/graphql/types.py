import strawberry
import strawberry_django
from strawberry import auto
from inventory.models import Category, Product,StockManagement


@strawberry_django.type(Category)
class CategoryType:
    id: auto
    name: auto
    slug: auto
    is_active: auto
    level: auto


@strawberry_django.type(Product)
class ProductType:
    
    id: auto
    name: auto
    slug: auto
    description: auto
    is_digital: auto
    is_active: auto 
    created_at: auto
    updated_at: auto
    price: auto
    category: CategoryType

@strawberry_django.type(StockManagement)
class StockManagementType:
    id: auto
    quantity: auto
    last_checked_at: auto

@strawberry.type
class ProductWithStockType:
    product: ProductType
    stock: StockManagementType
    category: CategoryType    

