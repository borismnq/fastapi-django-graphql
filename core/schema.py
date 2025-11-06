import strawberry
from strawberry.schema.config import StrawberryConfig

from apps.api.schema.mutations import Mutation
from apps.api.schema.queries import Query

schema = strawberry.federation.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
    enable_federation_2=True,
)
