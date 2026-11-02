from typing import Any
from uuid import UUID

from .base_model import BaseModel


class GetRolebindingITUsers(BaseModel):
    itusers: "GetRolebindingITUsersItusers"


class GetRolebindingITUsersItusers(BaseModel):
    objects: list["GetRolebindingITUsersItusersObjects"]
    page_info: "GetRolebindingITUsersItusersPageInfo"


class GetRolebindingITUsersItusersObjects(BaseModel):
    uuid: UUID


class GetRolebindingITUsersItusersPageInfo(BaseModel):
    next_cursor: Any | None


GetRolebindingITUsers.update_forward_refs()
GetRolebindingITUsersItusers.update_forward_refs()
GetRolebindingITUsersItusersObjects.update_forward_refs()
GetRolebindingITUsersItusersPageInfo.update_forward_refs()
