# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from fastapi.encoders import jsonable_encoder
from slurm.client import models as m

if TYPE_CHECKING:
    from slurm.client.api_client import ApiClient


class _SlurmApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_slurmctld_cancel_job(
        self, job_id: int, signal: m.V0036Signal = None
    ) -> Awaitable[None]:
        path_params = {"job_id": str(job_id)}

        query_params = {}
        if signal is not None:
            query_params["signal"] = str(signal)

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/job/{job_id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_slurmctld_diag(
        self,
    ) -> Awaitable[m.V0036Diag]:
        return self.api_client.request(
            type_=m.V0036Diag,
            method="GET",
            url="/diag/",
        )

    def _build_for_slurmctld_get_job(
        self, job_id: int
    ) -> Awaitable[m.V0036JobsResponse]:
        path_params = {"job_id": str(job_id)}

        return self.api_client.request(
            type_=m.V0036JobsResponse,
            method="GET",
            url="/job/{job_id}",
            path_params=path_params,
        )

    def _build_for_slurmctld_get_jobs(
        self,
    ) -> Awaitable[m.V0036JobsResponse]:
        return self.api_client.request(
            type_=m.V0036JobsResponse,
            method="GET",
            url="/jobs/",
        )

    def _build_for_slurmctld_get_node(
        self, node_name: str
    ) -> Awaitable[m.V0036NodesResponse]:
        path_params = {"node_name": str(node_name)}

        return self.api_client.request(
            type_=m.V0036NodesResponse,
            method="GET",
            url="/node/{node_name}",
            path_params=path_params,
        )

    def _build_for_slurmctld_get_nodes(
        self,
    ) -> Awaitable[m.V0036NodesResponse]:
        return self.api_client.request(
            type_=m.V0036NodesResponse,
            method="GET",
            url="/nodes/",
        )

    def _build_for_slurmctld_get_partition(
        self, partition_name: str
    ) -> Awaitable[m.V0036PartitionsResponse]:
        path_params = {"partition_name": str(partition_name)}

        return self.api_client.request(
            type_=m.V0036PartitionsResponse,
            method="GET",
            url="/partition/{partition_name}",
            path_params=path_params,
        )

    def _build_for_slurmctld_get_partitions(
        self,
    ) -> Awaitable[m.V0036PartitionsResponse]:
        return self.api_client.request(
            type_=m.V0036PartitionsResponse,
            method="GET",
            url="/partitions/",
        )

    def _build_for_slurmctld_ping(
        self,
    ) -> Awaitable[m.V0036Pings]:
        return self.api_client.request(
            type_=m.V0036Pings,
            method="GET",
            url="/ping/",
        )

    def _build_for_slurmctld_submit_job(
        self, v0036_job_submission: m.V0036JobSubmission
    ) -> Awaitable[m.V0036JobSubmissionResponse]:
        body = jsonable_encoder(v0036_job_submission)

        return self.api_client.request(
            type_=m.V0036JobSubmissionResponse,
            method="POST",
            url="/job/submit",
            json=body,
        )

    def _build_for_slurmctld_update_job(
        self, job_id: int, v0036_job_properties: m.V0036JobProperties
    ) -> Awaitable[None]:
        path_params = {"job_id": str(job_id)}

        body = jsonable_encoder(v0036_job_properties)

        return self.api_client.request(
            type_=None,
            method="POST",
            url="/job/{job_id}",
            path_params=path_params,
            json=body,
        )


class AsyncSlurmApi(_SlurmApi):
    async def slurmctld_cancel_job(
        self, job_id: int, signal: m.V0036Signal = None
    ) -> None:
        return await self._build_for_slurmctld_cancel_job(job_id=job_id, signal=signal)

    async def slurmctld_diag(
        self,
    ) -> m.V0036Diag:
        return await self._build_for_slurmctld_diag()

    async def slurmctld_get_job(self, job_id: int) -> m.V0036JobsResponse:
        return await self._build_for_slurmctld_get_job(job_id=job_id)

    async def slurmctld_get_jobs(
        self,
    ) -> m.V0036JobsResponse:
        return await self._build_for_slurmctld_get_jobs()

    async def slurmctld_get_node(self, node_name: str) -> m.V0036NodesResponse:
        return await self._build_for_slurmctld_get_node(node_name=node_name)

    async def slurmctld_get_nodes(
        self,
    ) -> m.V0036NodesResponse:
        return await self._build_for_slurmctld_get_nodes()

    async def slurmctld_get_partition(
        self, partition_name: str
    ) -> m.V0036PartitionsResponse:
        return await self._build_for_slurmctld_get_partition(
            partition_name=partition_name
        )

    async def slurmctld_get_partitions(
        self,
    ) -> m.V0036PartitionsResponse:
        return await self._build_for_slurmctld_get_partitions()

    async def slurmctld_ping(
        self,
    ) -> m.V0036Pings:
        return await self._build_for_slurmctld_ping()

    async def slurmctld_submit_job(
        self, v0036_job_submission: m.V0036JobSubmission
    ) -> m.V0036JobSubmissionResponse:
        return await self._build_for_slurmctld_submit_job(
            v0036_job_submission=v0036_job_submission
        )

    async def slurmctld_update_job(
        self, job_id: int, v0036_job_properties: m.V0036JobProperties
    ) -> None:
        return await self._build_for_slurmctld_update_job(
            job_id=job_id, v0036_job_properties=v0036_job_properties
        )


class SyncSlurmApi(_SlurmApi):
    def slurmctld_cancel_job(self, job_id: int, signal: m.V0036Signal = None) -> None:
        coroutine = self._build_for_slurmctld_cancel_job(job_id=job_id, signal=signal)
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_diag(
        self,
    ) -> m.V0036Diag:
        coroutine = self._build_for_slurmctld_diag()
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_get_job(self, job_id: int) -> m.V0036JobsResponse:
        coroutine = self._build_for_slurmctld_get_job(job_id=job_id)
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_get_jobs(
        self,
    ) -> m.V0036JobsResponse:
        coroutine = self._build_for_slurmctld_get_jobs()
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_get_node(self, node_name: str) -> m.V0036NodesResponse:
        coroutine = self._build_for_slurmctld_get_node(node_name=node_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_get_nodes(
        self,
    ) -> m.V0036NodesResponse:
        coroutine = self._build_for_slurmctld_get_nodes()
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_get_partition(self, partition_name: str) -> m.V0036PartitionsResponse:
        coroutine = self._build_for_slurmctld_get_partition(
            partition_name=partition_name
        )
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_get_partitions(
        self,
    ) -> m.V0036PartitionsResponse:
        coroutine = self._build_for_slurmctld_get_partitions()
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_ping(
        self,
    ) -> m.V0036Pings:
        coroutine = self._build_for_slurmctld_ping()
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_submit_job(
        self, v0036_job_submission: m.V0036JobSubmission
    ) -> m.V0036JobSubmissionResponse:
        coroutine = self._build_for_slurmctld_submit_job(
            v0036_job_submission=v0036_job_submission
        )
        return get_event_loop().run_until_complete(coroutine)

    def slurmctld_update_job(
        self, job_id: int, v0036_job_properties: m.V0036JobProperties
    ) -> None:
        coroutine = self._build_for_slurmctld_update_job(
            job_id=job_id, v0036_job_properties=v0036_job_properties
        )
        return get_event_loop().run_until_complete(coroutine)
