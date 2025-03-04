import strawberry


@strawberry.type
class Form:
    id: strawberry.ID
    name: str
    path: str
    type: str
    display: str
