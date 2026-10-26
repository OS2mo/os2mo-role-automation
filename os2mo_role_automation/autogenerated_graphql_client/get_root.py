from .base_model import BaseModel


class GetRoot(BaseModel):
    org: "GetRootOrg"


class GetRootOrg(BaseModel):
    user_key: str


GetRoot.update_forward_refs()
GetRootOrg.update_forward_refs()
