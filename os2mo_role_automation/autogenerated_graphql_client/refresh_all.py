from typing import Any

from .base_model import BaseModel


class RefreshAll(BaseModel):
    ituser_refresh: "RefreshAllItuserRefresh"


class RefreshAllItuserRefresh(BaseModel):
    page_info: "RefreshAllItuserRefreshPageInfo"


class RefreshAllItuserRefreshPageInfo(BaseModel):
    next_cursor: Any | None


RefreshAll.update_forward_refs()
RefreshAllItuserRefresh.update_forward_refs()
RefreshAllItuserRefreshPageInfo.update_forward_refs()
