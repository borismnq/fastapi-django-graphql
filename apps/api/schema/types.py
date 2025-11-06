import strawberry
from typing import Optional


@strawberry.type
class ExampleType:
    """
    Example GraphQL type - replace with your own types
    """
    id: strawberry.ID
    name: str
    description: Optional[str] = None
    is_active: bool = True


@strawberry.input
class ExampleInput:
    """
    Example GraphQL input type for mutations
    """
    name: str
    description: Optional[str] = None
    is_active: bool = True
