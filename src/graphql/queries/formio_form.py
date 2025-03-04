from typing import List
import strawberry
from src.graphql.types import Form
from src.graphql.resolvers import get_forms_from_formio


@strawberry.type
class Query:
    @strawberry.field(name="getForms")
    def get_forms(self) -> List[Form]:
        result = get_forms_from_formio()
        return result
