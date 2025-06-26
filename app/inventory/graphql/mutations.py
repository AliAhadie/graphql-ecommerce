import strawberry
from inventory.models import Category
from inventory.graphql.inputs import CategoryInput
from inventory.graphql.types import CategoryType


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_category(self, input: CategoryInput) -> CategoryType:
        category = Category.objects.create(
            name=input.name,
            slug=input.slug,
            is_active=input.is_active,
            level=input.level,
            parent=input.parent_id,
        )
        return category