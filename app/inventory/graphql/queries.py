import strawberry
from .types import CategoryType
from typing import List
from inventory.models import Category
from .inputs import CategoryFilter, CategoryOrderFilter


@strawberry.type
class Query:
    @strawberry.field(description="Returns a list of all categories")
    def category_all(self) -> List[CategoryType]:
        return Category.objects.all()

    @strawberry.field
    def category_filter(
        self,
        where: CategoryFilter | None = None,
        orderby: CategoryOrderFilter | None = None,
    ) -> List[CategoryType]:
        queryset = Category.objects.all()
        if where:
            if where.is_active:
                queryset = queryset.filter(is_active=where.is_active)
            if where.name:
                queryset = queryset.filter(name__icontains=where.name)

        if orderby:
            if orderby.field:
                direction = "" if orderby.direction == "asc" else "-"
                queryset = queryset.order_by(f"{direction}{orderby.field}")
            else:
                raise ValueError("cant ordering")

        return queryset
