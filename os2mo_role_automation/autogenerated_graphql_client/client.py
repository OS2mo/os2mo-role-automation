from typing import Any
from uuid import UUID

from .async_base_client import AsyncBaseClient
from .base_model import UNSET
from .base_model import UnsetType
from .create_rolebinding import CreateRolebinding
from .create_rolebinding import CreateRolebindingRolebindingCreate
from .get_actual_state import GetActualState
from .get_actual_state import GetActualStateRolebindings
from .get_engagement_i_t_users import GetEngagementITUsers
from .get_engagement_i_t_users import GetEngagementITUsersItusers
from .get_org_unit_engagements import GetOrgUnitEngagements
from .get_org_unit_engagements import GetOrgUnitEngagementsEngagements
from .get_rolebinding_i_t_users import GetRolebindingITUsers
from .get_rolebinding_i_t_users import GetRolebindingITUsersItusers
from .get_root import GetRoot
from .get_root import GetRootOrg
from .input_types import EventSendInput
from .input_types import RoleBindingCreateInput
from .input_types import RoleBindingTerminateInput
from .refresh_all import RefreshAll
from .refresh_all import RefreshAllItuserRefresh
from .send_event import SendEvent
from .terminate_rolebinding import TerminateRolebinding
from .terminate_rolebinding import TerminateRolebindingRolebindingTerminate
from .whoami import Whoami
from .whoami import WhoamiMe


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

    async def refresh_all(
        self,
        owner: UUID,
        priority: int,
        cursor: Any | None | UnsetType = UNSET,
    ) -> RefreshAllItuserRefresh:
        query = gql("""
            mutation RefreshAll($cursor: Cursor, $owner: UUID!, $priority: Int!) {
              ituser_refresh(cursor: $cursor, limit: 100, owner: $owner, priority: $priority) {
                page_info {
                  next_cursor
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "cursor": cursor,
            "owner": owner,
            "priority": priority,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return RefreshAll.parse_obj(data).ituser_refresh

    async def whoami(self) -> WhoamiMe:
        query = gql("""
            query whoami {
              me {
                actor {
                  uuid
                }
              }
            }
            """)
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return Whoami.parse_obj(data).me

    async def get_rolebinding_i_t_users(
        self, uuid: UUID, cursor: Any | None | UnsetType = UNSET
    ) -> GetRolebindingITUsersItusers:
        query = gql("""
            query GetRolebindingITUsers($cursor: Cursor, $uuid: UUID!) {
              itusers(
                filter: {rolebinding: {uuids: [$uuid]}, from_date: null, to_date: null}
                cursor: $cursor
                limit: 10
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
        variables: dict[str, object] = {"cursor": cursor, "uuid": uuid}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetRolebindingITUsers.parse_obj(data).itusers

    async def create_rolebinding(
        self, input: RoleBindingCreateInput
    ) -> CreateRolebindingRolebindingCreate:
        query = gql("""
            mutation CreateRolebinding($input: RoleBindingCreateInput!) {
              rolebinding_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return CreateRolebinding.parse_obj(data).rolebinding_create

    async def terminate_rolebinding(
        self, input: RoleBindingTerminateInput
    ) -> TerminateRolebindingRolebindingTerminate:
        query = gql("""
            mutation TerminateRolebinding($input: RoleBindingTerminateInput!) {
              rolebinding_terminate(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TerminateRolebinding.parse_obj(data).rolebinding_terminate

    async def get_actual_state(
        self, ituser: UUID, user_key: str
    ) -> GetActualStateRolebindings:
        query = gql("""
            query GetActualState($ituser: UUID!, $user_key: String!) {
              rolebindings(filter: {ituser: {uuids: [$ituser]}, user_keys: [$user_key]}) {
                objects {
                  current {
                    role_response {
                      uuid
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"ituser": ituser, "user_key": user_key}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetActualState.parse_obj(data).rolebindings
