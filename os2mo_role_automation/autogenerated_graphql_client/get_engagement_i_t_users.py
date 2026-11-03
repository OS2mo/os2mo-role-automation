from typing import Any
from uuid import UUID

from .base_model import BaseModel


class GetEngagementITUsers(BaseModel):
    itusers: "GetEngagementITUsersItusers"


class GetEngagementITUsersItusers(BaseModel):
    objects: list["GetEngagementITUsersItusersObjects"]
    page_info: "GetEngagementITUsersItusersPageInfo"


class GetEngagementITUsersItusersObjects(BaseModel):
    uuid: UUID


class GetEngagementITUsersItusersPageInfo(BaseModel):
    next_cursor: Any | None


GetEngagementITUsers.update_forward_refs()
GetEngagementITUsersItusers.update_forward_refs()
GetEngagementITUsersItusersObjects.update_forward_refs()
GetEngagementITUsersItusersPageInfo.update_forward_refs()
