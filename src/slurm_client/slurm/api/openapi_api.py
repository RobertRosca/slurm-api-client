# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

if TYPE_CHECKING:
    from slurm.client.api_client import ApiClient


class _OpenapiApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_openapi_get(
        self,
    ) -> Awaitable[None]:
        return self.api_client.request(
            type_=None,
            method="GET",
            url="/openapi",
        )

    def _build_for_openapi_json_get(
        self,
    ) -> Awaitable[None]:
        return self.api_client.request(
            type_=None,
            method="GET",
            url="/openapi.json",
        )

    def _build_for_openapi_v3_get(
        self,
    ) -> Awaitable[None]:
        return self.api_client.request(
            type_=None,
            method="GET",
            url="/openapi/v3",
        )

    def _build_for_openapi_yaml_get(
        self,
    ) -> Awaitable[None]:
        return self.api_client.request(
            type_=None,
            method="GET",
            url="/openapi.yaml",
        )


class AsyncOpenapiApi(_OpenapiApi):
    async def openapi_get(
        self,
    ) -> None:
        return await self._build_for_openapi_get()

    async def openapi_json_get(
        self,
    ) -> None:
        return await self._build_for_openapi_json_get()

    async def openapi_v3_get(
        self,
    ) -> None:
        return await self._build_for_openapi_v3_get()

    async def openapi_yaml_get(
        self,
    ) -> None:
        return await self._build_for_openapi_yaml_get()


class SyncOpenapiApi(_OpenapiApi):
    def openapi_get(
        self,
    ) -> None:
        coroutine = self._build_for_openapi_get()
        return get_event_loop().run_until_complete(coroutine)

    def openapi_json_get(
        self,
    ) -> None:
        coroutine = self._build_for_openapi_json_get()
        return get_event_loop().run_until_complete(coroutine)

    def openapi_v3_get(
        self,
    ) -> None:
        coroutine = self._build_for_openapi_v3_get()
        return get_event_loop().run_until_complete(coroutine)

    def openapi_yaml_get(
        self,
    ) -> None:
        coroutine = self._build_for_openapi_yaml_get()
        return get_event_loop().run_until_complete(coroutine)
