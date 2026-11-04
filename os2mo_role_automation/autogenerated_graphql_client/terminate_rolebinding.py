from uuid import UUID

from .base_model import BaseModel


class TerminateRolebinding(BaseModel):
    rolebinding_terminate: "TerminateRolebindingRolebindingTerminate"


class TerminateRolebindingRolebindingTerminate(BaseModel):
    uuid: UUID


TerminateRolebinding.update_forward_refs()
TerminateRolebindingRolebindingTerminate.update_forward_refs()
