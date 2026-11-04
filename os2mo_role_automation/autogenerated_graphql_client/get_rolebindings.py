from datetime import datetime
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class GetRolebindings(BaseModel):
    rolebindings: "GetRolebindingsRolebindings"


class GetRolebindingsRolebindings(BaseModel):
    objects: list["GetRolebindingsRolebindingsObjects"]


class GetRolebindingsRolebindingsObjects(BaseModel):
    validities: list["GetRolebindingsRolebindingsObjectsValidities"]


class GetRolebindingsRolebindingsObjectsValidities(BaseModel):
    uuid: UUID
    role_response: "GetRolebindingsRolebindingsObjectsValiditiesRoleResponse"
    validity: "GetRolebindingsRolebindingsObjectsValiditiesValidity"


class GetRolebindingsRolebindingsObjectsValiditiesRoleResponse(BaseModel):
    uuid: UUID


class GetRolebindingsRolebindingsObjectsValiditiesValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: datetime | None


GetRolebindings.update_forward_refs()
GetRolebindingsRolebindings.update_forward_refs()
GetRolebindingsRolebindingsObjects.update_forward_refs()
GetRolebindingsRolebindingsObjectsValidities.update_forward_refs()
GetRolebindingsRolebindingsObjectsValiditiesRoleResponse.update_forward_refs()
GetRolebindingsRolebindingsObjectsValiditiesValidity.update_forward_refs()
