from typing import Any
from uuid import UUID

from .async_base_client import AsyncBaseClient
from .base_model import UNSET
from .base_model import UnsetType
from .get_engagement_i_t_users import GetEngagementITUsers
from .get_engagement_i_t_users import GetEngagementITUsersItusers
from .get_org_unit_engagements import GetOrgUnitEngagements
from .get_org_unit_engagements import GetOrgUnitEngagementsEngagements
from .get_root import GetRoot
from .get_root import GetRootOrg
from .input_types import EventSendInput
from .send_event import SendEvent


def gql(q: str) -> str:
    return q


class GraphQLClient(AsyncBaseClient):
    async def get_root(self) -> GetRootOrg:
        query = gql("""
            query GetRoot {
              org {
                user_key
              }
            }
            """)
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetRoot.parse_obj(data).org

    async def send_event(self, input: EventSendInput) -> bool:
        query = gql("""
            mutation SendEvent($input: EventSendInput!) {
              event_send(input: $input)
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return SendEvent.parse_obj(data).event_send

    async def get_engagement_i_t_users(
        self, engagement: UUID, cursor: Any | None | UnsetType = UNSET
    ) -> GetEngagementITUsersItusers:
        query = gql("""
            query GetEngagementITUsers($cursor: Cursor, $engagement: UUID!) {
              itusers(
                cursor: $cursor
                limit: 100
                filter: {engagement: {uuids: [$engagement], from_date: null, to_date: null}, from_date: null, to_date: null}
              ) {
                objects {
                  uuid
                }
                page_info {
                  next_cursor
                }
              }
            }
            """)
        variables: dict[str, object] = {"cursor": cursor, "engagement": engagement}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetEngagementITUsers.parse_obj(data).itusers

    async def get_org_unit_engagements(
        self, org_unit: UUID, cursor: Any | None | UnsetType = UNSET
    ) -> GetOrgUnitEngagementsEngagements:
        query = gql("""
            query GetOrgUnitEngagements($cursor: Cursor, $org_unit: UUID!) {
              engagements(
                cursor: $cursor
                limit: 100
                filter: {org_unit: {ancestor: {uuids: [$org_unit]}}}
              ) {
                objects {
                  uuid
                }
                page_info {
                  next_cursor
                }
              }
            }
            """)
        variables: dict[str, object] = {"cursor": cursor, "org_unit": org_unit}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetOrgUnitEngagements.parse_obj(data).engagements
