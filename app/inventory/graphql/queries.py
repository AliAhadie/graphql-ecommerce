import strawberry
from .types import CategoryType
from typing import List

@strawberry.type
class Query:
    @strawberry.field(description="Returns a list of all categories")
    def categories(self) -> List[CategoryType]:
        return [CategoryType(
            id='1',
            parent_id=None,
            name='books',
            slug='books',
            is_active=True,
            level=0

        )]
    