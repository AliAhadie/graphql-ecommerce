from django.urls import path,include
from strawberry.django.views import GraphQLView
from inventory.graphql.schema import schema
urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema)),
]