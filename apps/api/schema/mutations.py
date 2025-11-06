import strawberry
from typing import Optional
from .types import ExampleType, ExampleInput
from apps.api.models import ExampleModel


@strawberry.type
class Mutation:
    """
    GraphQL Mutation root type
    Add your mutations here
    """
    
    @strawberry.mutation
    def create_example(self, input: ExampleInput) -> ExampleType:
        """Create a new example in the database"""
        obj = ExampleModel.objects.create(
            name=input.name,
            description=input.description,
            is_active=input.is_active
        )
        return ExampleType.from_model(obj)
    
    @strawberry.mutation
    def update_example(self, id: strawberry.ID, input: ExampleInput) -> Optional[ExampleType]:
        """Update an existing example in the database"""
        try:
            obj = ExampleModel.objects.get(id=int(id))
            obj.name = input.name
            obj.description = input.description
            obj.is_active = input.is_active
            obj.save()
            return ExampleType.from_model(obj)
        except ExampleModel.DoesNotExist:
            return None
    
    @strawberry.mutation
    def delete_example(self, id: strawberry.ID) -> bool:
        """Delete an example from the database"""
        try:
            obj = ExampleModel.objects.get(id=int(id))
            obj.delete()
            return True
        except ExampleModel.DoesNotExist:
            return False
