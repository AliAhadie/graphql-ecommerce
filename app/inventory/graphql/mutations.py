import strawberry
from inventory.models import Category, Product, StockManagement
from inventory.graphql.inputs import CategoryInput, ProductInput, ProductWithStockInput,UpdateProductInput,PartialUpdateProductInput
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
    @strawberry.mutation
    def update_product(self,input:UpdateProductInput) -> ProductType:
        with transaction.atomic():
            try:
                product=Product.objects.get(id=input.id)
            except Product.DoesNotExist:
                raise ValueError("Invalid product ID provided.")

            try:
                category=Category.objects.get(id=input.category_id)
            except Category.DoesNotExist:
                raise ValueError("Invalid category ID provided.")

            product.name = input.name
            product.slug = input.slug
            product.description = input.description
            product.is_digital = input.is_digital
            product.is_active = input.is_active
            product.price = input.price
            product.category_id = input.category_id
            product.save()

            return product
    @strawberry.mutation
    def partial_product_update(self,input:PartialUpdateProductInput)->ProductType:
        with transaction.atomic():
            try:
                product=Product.objects.get(id=input.id)
            except Product.DoesNotExist:
                raise ValueError("Invalid product ID provided.")
            if input.name is not None:
                product.name = input.name
            if input.slug is not None:
                product.slug = input.slug
            if input.description is not None:
                product.description = input.description
            if input.is_digital is not None:
                product.is_digital = input.is_digital
            if input.is_active is not None:
                product.is_active = input.is_active
            if input.price is not None:
                product.price = input.price
            if input.category_id is not None:
                product.category_id = input.category_id
            product.save()

            return product
