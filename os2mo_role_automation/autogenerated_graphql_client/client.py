from .async_base_client import AsyncBaseClient
from .get_root import GetRoot
from .get_root import GetRootOrg


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
