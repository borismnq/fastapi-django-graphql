"""
GraphQL Permission utilities

Example usage:
    @strawberry.type
    class Query:
        @strawberry.field(permission_classes=[IsAuthenticated])
        def protected_field(self, info) -> str:
            return "This is protected"
"""
from typing import Any, Awaitable, Union

from strawberry.permission import BasePermission
from strawberry.types import Info


class IsAuthenticated(BasePermission):
    """
    Permission class to check if user is authenticated
    Customize based on your authentication logic
    """
    message = "User is not authenticated"

    def has_permission(
        self, source: Any, info: Info, **kwargs
    ) -> Union[bool, Awaitable[bool]]:
        # Customize this based on your context structure
        # Example: check if user exists in context
        if hasattr(info.context, "user") and info.context.user:
            return True
        return False


class IsAdmin(BasePermission):
    """
    Permission class to check if user is an admin
    Customize based on your authorization logic
    """
    message = "User does not have admin privileges"

    def has_permission(
        self, source: Any, info: Info, **kwargs
    ) -> Union[bool, Awaitable[bool]]:
        # Customize this based on your context structure
        # Example: check if user has admin role
        if (
            hasattr(info.context, "user")
            and info.context.user
            and hasattr(info.context.user, "is_admin")
            and info.context.user.is_admin
        ):
            return True
        return False
