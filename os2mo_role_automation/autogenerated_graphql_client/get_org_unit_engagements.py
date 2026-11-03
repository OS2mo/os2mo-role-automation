from typing import Any
from uuid import UUID

from .base_model import BaseModel


class GetOrgUnitEngagements(BaseModel):
    engagements: "GetOrgUnitEngagementsEngagements"


class GetOrgUnitEngagementsEngagements(BaseModel):
    objects: list["GetOrgUnitEngagementsEngagementsObjects"]
    page_info: "GetOrgUnitEngagementsEngagementsPageInfo"


class GetOrgUnitEngagementsEngagementsObjects(BaseModel):
    uuid: UUID


class GetOrgUnitEngagementsEngagementsPageInfo(BaseModel):
    next_cursor: Any | None


GetOrgUnitEngagements.update_forward_refs()
GetOrgUnitEngagementsEngagements.update_forward_refs()
GetOrgUnitEngagementsEngagementsObjects.update_forward_refs()
GetOrgUnitEngagementsEngagementsPageInfo.update_forward_refs()
