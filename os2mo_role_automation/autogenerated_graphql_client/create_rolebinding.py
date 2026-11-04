from uuid import UUID

from .base_model import BaseModel


class CreateRolebinding(BaseModel):
    rolebinding_create: "CreateRolebindingRolebindingCreate"


class CreateRolebindingRolebindingCreate(BaseModel):
    uuid: UUID


CreateRolebinding.update_forward_refs()
CreateRolebindingRolebindingCreate.update_forward_refs()
