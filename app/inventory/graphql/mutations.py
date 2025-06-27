import strawberry
from inventory.models import Category, Product, StockManagement
from inventory.graphql.inputs import CategoryInput, ProductInput, ProductWithStockInput
from inventory.graphql.types import CategoryType, ProductType, ProductWithStockType
import datetime
from django.db import transaction
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
            price=input.price,
            category=category,
        )
        return product

    @strawberry.mutation
    def create_product_with_stock(
        self, input: ProductWithStockInput
    ) -> ProductWithStockType:
        with transaction.atomic():
            
            category = Category.objects.filter(id=input.category_id).first()

            if not category:
                raise ValueError("Invalid category ID provided.")

            product = Product.objects.create(
                name=input.name,
                slug=input.slug,
                description=input.description,
                price=input.price,
                is_digital=input.is_digital,
                is_active=input.is_active,
                category=category,
            )

            stock = StockManagement.objects.create(
                product=product,
                quantity=input.quantity if input.quantity is not None else 0,
                last_checked_at=datetime.datetime.now(),
            )

            return ProductWithStockType(product=product, stock=stock, category=category)
