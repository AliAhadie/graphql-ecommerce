import strawberry
from .types import CategoryType
from typing import List
from inventory.models import Category

@strawberry.type
class Query:
    @strawberry.field(description="Returns a list of all categories")
    def categories(self) -> List[CategoryType]:
        return Category.objects.all()

    