import strawberry
from inventory.models import Category,Product
from inventory.graphql.inputs import CategoryInput,ProductInput
from inventory.graphql.types import CategoryType,ProductType


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

    @strawberry.mutation
    def create_product(self, input: ProductInput) -> ProductType:
        category = Category.objects.filter(id=input.category_id).first()

        if not category:
            raise ValueError("Invalid category ID provided.")

        product = Product.objects.create(
            name=input.name,
            slug=input.slug,
            description=input.description,
            is_digital=input.is_digital,
            is_active=input.is_active,
            price=input.price,
            category=category,
        )
        return product