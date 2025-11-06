import strawberry
from typing import List, Optional
from .types import ExampleType
from apps.api.models import ExampleModel


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
    def examples(self, is_active: Optional[bool] = None) -> List[ExampleType]:
        """
        Query all examples from the database
        Optionally filter by is_active status
        """
        queryset = ExampleModel.objects.all()
        
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)
        
        return [ExampleType.from_model(obj) for obj in queryset]
    
    @strawberry.field
    def example(self, id: strawberry.ID) -> Optional[ExampleType]:
        """Query a single example by ID from the database"""
        try:
            obj = ExampleModel.objects.get(id=int(id))
            return ExampleType.from_model(obj)
        except ExampleModel.DoesNotExist:
            return None
    
    @strawberry.field
    def search_examples(self, name: str) -> List[ExampleType]:
        """Search examples by name (case-insensitive contains)"""
        queryset = ExampleModel.objects.filter(name__icontains=name)
        return [ExampleType.from_model(obj) for obj in queryset]
