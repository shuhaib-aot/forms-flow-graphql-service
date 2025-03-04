import strawberry
from strawberry.fastapi import GraphQLRouter
from src.graphql.queries import Query

schema = strawberry.Schema(query=Query)
grphql_app = GraphQLRouter(schema)
