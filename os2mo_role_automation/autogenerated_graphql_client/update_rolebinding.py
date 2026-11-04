from uuid import UUID

from .base_model import BaseModel


class UpdateRolebinding(BaseModel):
    rolebinding_update: "UpdateRolebindingRolebindingUpdate"


class UpdateRolebindingRolebindingUpdate(BaseModel):
    uuid: UUID


UpdateRolebinding.update_forward_refs()
UpdateRolebindingRolebindingUpdate.update_forward_refs()
