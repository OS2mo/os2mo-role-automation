from uuid import UUID

from .base_model import BaseModel


class Whoami(BaseModel):
    me: "WhoamiMe"


class WhoamiMe(BaseModel):
    actor: "WhoamiMeActor"


class WhoamiMeActor(BaseModel):
    uuid: UUID


Whoami.update_forward_refs()
WhoamiMe.update_forward_refs()
WhoamiMeActor.update_forward_refs()
