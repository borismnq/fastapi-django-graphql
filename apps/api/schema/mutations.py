import strawberry
from typing import Optional
from .types import ExampleType, ExampleInput


@strawberry.type
class Mutation:
    """
    GraphQL Mutation root type
    Add your mutations here
    """
    
    @strawberry.mutation
    def create_example(self, input: ExampleInput) -> ExampleType:
        """Example mutation that creates an item"""
        # Replace with actual database mutation
        return ExampleType(
            id=strawberry.ID("new-id"),
            name=input.name,
            description=input.description,
            is_active=input.is_active
        )
    
    @strawberry.mutation
    def update_example(self, id: strawberry.ID, input: ExampleInput) -> ExampleType:
        """Example mutation that updates an item"""
        # Replace with actual database mutation
        return ExampleType(
            id=id,
            name=input.name,
            description=input.description,
            is_active=input.is_active
        )
    
    @strawberry.mutation
    def delete_example(self, id: strawberry.ID) -> bool:
        """Example mutation that deletes an item"""
        # Replace with actual database mutation
        return True
