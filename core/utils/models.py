from typing import List, Optional, Sequence, Tuple, Union

from django.db.models import Model


def model_to_dict(
    instance: Model,
    fields: Optional[List[str]] = None,
    exclude: Optional[Sequence[str]] = None,
) -> dict:
    instance_dict = instance.__dict__.copy()
    instance_fields_dict = {}

    del instance_dict["_state"]

    if fields is None:
        fields = tuple(instance_dict.keys())

    if exclude is None:
        exclude = ()

    if type(fields) in (list, tuple):
        for instance_field in instance_dict.keys():
            if instance_field in fields:
                instance_fields_dict[instance_field] = instance_dict[instance_field]

    instance_exclude_dict = {}

    if type(exclude) in (list, tuple):
        for instance_field in instance_fields_dict.keys():
            if instance_field not in exclude:
                instance_exclude_dict[instance_field] = instance_fields_dict[
                    instance_field
                ]

    return instance_exclude_dict
