import strawberry
from typing import List, Optional
from .types import ExampleType


@strawberry.type
class Query:
    """
    GraphQL Query root type
    Add your queries here
    """
    
    @strawberry.field
    def hello(self, name: Optional[str] = None) -> str:
        """Example query that returns a greeting"""
        if name:
            return f"Hello, {name}!"
        return "Hello, World!"
    
    @strawberry.field
    def examples(self) -> List[ExampleType]:
        """Example query that returns a list of items"""
        # Replace with actual database queries
        return [
            ExampleType(
                id=strawberry.ID("1"),
                name="Example 1",
                description="This is an example",
                is_active=True
            ),
            ExampleType(
                id=strawberry.ID("2"),
                name="Example 2",
                description="Another example",
                is_active=True
            ),
        ]
    
    @strawberry.field
    def example(self, id: strawberry.ID) -> Optional[ExampleType]:
        """Example query that returns a single item by ID"""
        # Replace with actual database query
        return ExampleType(
            id=id,
            name=f"Example {id}",
            description="This is an example",
            is_active=True
        )
