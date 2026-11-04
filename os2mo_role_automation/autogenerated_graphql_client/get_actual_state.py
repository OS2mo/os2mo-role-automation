from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class GetActualState(BaseModel):
    rolebindings: "GetActualStateRolebindings"


class GetActualStateRolebindings(BaseModel):
    objects: list["GetActualStateRolebindingsObjects"]


class GetActualStateRolebindingsObjects(BaseModel):
    current: Optional["GetActualStateRolebindingsObjectsCurrent"]


class GetActualStateRolebindingsObjectsCurrent(BaseModel):
    role_response: "GetActualStateRolebindingsObjectsCurrentRoleResponse"


class GetActualStateRolebindingsObjectsCurrentRoleResponse(BaseModel):
    uuid: UUID


GetActualState.update_forward_refs()
GetActualStateRolebindings.update_forward_refs()
GetActualStateRolebindingsObjects.update_forward_refs()
GetActualStateRolebindingsObjectsCurrent.update_forward_refs()
GetActualStateRolebindingsObjectsCurrentRoleResponse.update_forward_refs()
