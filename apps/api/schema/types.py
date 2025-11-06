import strawberry
from typing import Optional
from apps.api.models import ExampleModel


@strawberry.type
class ExampleType:
    """
    Example GraphQL type mapped from Django ExampleModel
    """
    id: strawberry.ID
    name: str
    description: Optional[str] = None
    is_active: bool = True
    created_at: str
    updated_at: str

    @staticmethod
    def from_model(model: ExampleModel) -> "ExampleType":
        """Convert Django model instance to GraphQL type"""
        return ExampleType(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            description=model.description,
            is_active=model.is_active,
            created_at=model.created_at.isoformat(),
            updated_at=model.updated_at.isoformat(),
        )


@strawberry.input
class ExampleInput:
    """
    Example GraphQL input type for mutations
    """
    name: str
    description: Optional[str] = None
    is_active: bool = True
