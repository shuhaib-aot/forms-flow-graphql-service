import strawberry
from src.graphql.queries.formio_form import Query as Form_Query


@strawberry.type
class Query(Form_Query):  # Inherit from both query classes
    pass
