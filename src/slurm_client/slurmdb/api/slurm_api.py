# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from slurmdb.client import models as m

if TYPE_CHECKING:
    from slurmdb.client.api_client import ApiClient


class _SlurmApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_slurmdbd_add_clusters(
        self,
    ) -> Awaitable[m.Dbv0036ResponseClusterAdd]:
        return self.api_client.request(
            type_=m.Dbv0036ResponseClusterAdd,
            method="POST",
            url="/clusters/",
        )

    def _build_for_slurmdbd_add_wckeys(
        self,
    ) -> Awaitable[m.Dbv0036ResponseWckeyAdd]:
        return self.api_client.request(
            type_=m.Dbv0036ResponseWckeyAdd,
            method="POST",
            url="/wckeys/",
        )

    def _build_for_slurmdbd_delete_account(
        self, account_name: str
    ) -> Awaitable[m.Dbv0036ResponseAccountDelete]:
        path_params = {"account_name": str(account_name)}

        return self.api_client.request(
            type_=m.Dbv0036ResponseAccountDelete,
            method="DELETE",
            url="/account/{account_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_delete_association(
        self, account: str, user: str, cluster: str = None, partition: str = None
    ) -> Awaitable[m.Dbv0036ResponseAssociationDelete]:
        query_params = {
            "account": str(account),
            "user": str(user),
        }
        if cluster is not None:
            query_params["cluster"] = str(cluster)
        if partition is not None:
            query_params["partition"] = str(partition)

        return self.api_client.request(
            type_=m.Dbv0036ResponseAssociationDelete,
            method="DELETE",
            url="/association/",
            params=query_params,
        )

    def _build_for_slurmdbd_delete_cluster(
        self, cluster_name: str
    ) -> Awaitable[m.Dbv0036ResponseClusterDelete]:
        path_params = {"cluster_name": str(cluster_name)}

        return self.api_client.request(
            type_=m.Dbv0036ResponseClusterDelete,
            method="DELETE",
            url="/cluster/{cluster_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_delete_qos(
        self, qos_name: str
    ) -> Awaitable[m.Dbv0036ResponseQosDelete]:
        path_params = {"qos_name": str(qos_name)}

        return self.api_client.request(
            type_=m.Dbv0036ResponseQosDelete,
            method="DELETE",
            url="/qos/{qos_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_delete_user(
        self, user_name: str
    ) -> Awaitable[m.Dbv0036ResponseUserDelete]:
        path_params = {"user_name": str(user_name)}

        return self.api_client.request(
            type_=m.Dbv0036ResponseUserDelete,
            method="DELETE",
            url="/user/{user_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_delete_wckey(
        self, wckey: str
    ) -> Awaitable[m.Dbv0036ResponseWckeyDelete]:
        path_params = {"wckey": str(wckey)}

        return self.api_client.request(
            type_=m.Dbv0036ResponseWckeyDelete,
            method="DELETE",
            url="/wckey/{wckey}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_diag(
        self,
    ) -> Awaitable[m.Dbv0036Diag]:
        return self.api_client.request(
            type_=m.Dbv0036Diag,
            method="GET",
            url="/diag/",
        )

    def _build_for_slurmdbd_get_account(
        self, account_name: str
    ) -> Awaitable[m.Dbv0036AccountInfo]:
        path_params = {"account_name": str(account_name)}

        return self.api_client.request(
            type_=m.Dbv0036AccountInfo,
            method="GET",
            url="/account/{account_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_get_accounts(
        self,
    ) -> Awaitable[m.Dbv0036AccountInfo]:
        return self.api_client.request(
            type_=m.Dbv0036AccountInfo,
            method="GET",
            url="/accounts/",
        )

    def _build_for_slurmdbd_get_association(
        self,
        cluster: str = None,
        account: str = None,
        user: str = None,
        partition: str = None,
    ) -> Awaitable[m.Dbv0036AssociationsInfo]:
        query_params = {}
        if cluster is not None:
            query_params["cluster"] = str(cluster)
        if account is not None:
            query_params["account"] = str(account)
        if user is not None:
            query_params["user"] = str(user)
        if partition is not None:
            query_params["partition"] = str(partition)

        return self.api_client.request(
            type_=m.Dbv0036AssociationsInfo,
            method="GET",
            url="/association/",
            params=query_params,
        )

    def _build_for_slurmdbd_get_associations(
        self,
    ) -> Awaitable[m.Dbv0036AssociationsInfo]:
        return self.api_client.request(
            type_=m.Dbv0036AssociationsInfo,
            method="GET",
            url="/associations/",
        )

    def _build_for_slurmdbd_get_cluster(
        self, cluster_name: str
    ) -> Awaitable[m.Dbv0036ClusterInfo]:
        path_params = {"cluster_name": str(cluster_name)}

        return self.api_client.request(
            type_=m.Dbv0036ClusterInfo,
            method="GET",
            url="/cluster/{cluster_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_get_clusters(
        self,
    ) -> Awaitable[m.Dbv0036ClusterInfo]:
        return self.api_client.request(
            type_=m.Dbv0036ClusterInfo,
            method="GET",
            url="/clusters/",
        )

    def _build_for_slurmdbd_get_db_config(
        self,
    ) -> Awaitable[m.Dbv0036ConfigInfo]:
        return self.api_client.request(
            type_=m.Dbv0036ConfigInfo,
            method="GET",
            url="/config",
        )

    def _build_for_slurmdbd_get_job(self, job_id: int) -> Awaitable[m.Dbv0036JobInfo]:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.
        """
        path_params = {"job_id": str(job_id)}

        return self.api_client.request(
            type_=m.Dbv0036JobInfo,
            method="GET",
            url="/job/{job_id}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_get_jobs(
        self,
        submit_time: str = None,
        start_time: str = None,
        end_time: str = None,
        account: str = None,
        association: str = None,
        cluster: str = None,
        constraints: str = None,
        cpus_max: str = None,
        cpus_min: str = None,
        skip_steps: bool = None,
        disable_wait_for_result: bool = None,
        exit_code: str = None,
        format: str = None,
        group: str = None,
        job_name: str = None,
        nodes_max: str = None,
        nodes_min: str = None,
        partition: str = None,
        qos: str = None,
        reason: str = None,
        reservation: str = None,
        state: str = None,
        step: str = None,
        node: str = None,
        wckey: str = None,
    ) -> Awaitable[m.Dbv0036JobInfo]:
        query_params = {}
        if submit_time is not None:
            query_params["submit_time"] = str(submit_time)
        if start_time is not None:
            query_params["start_time"] = str(start_time)
        if end_time is not None:
            query_params["end_time"] = str(end_time)
        if account is not None:
            query_params["account"] = str(account)
        if association is not None:
            query_params["association"] = str(association)
        if cluster is not None:
            query_params["cluster"] = str(cluster)
        if constraints is not None:
            query_params["constraints"] = str(constraints)
        if cpus_max is not None:
            query_params["cpus_max"] = str(cpus_max)
        if cpus_min is not None:
            query_params["cpus_min"] = str(cpus_min)
        if skip_steps is not None:
            query_params["skip_steps"] = str(skip_steps)
        if disable_wait_for_result is not None:
            query_params["disable_wait_for_result"] = str(disable_wait_for_result)
        if exit_code is not None:
            query_params["exit_code"] = str(exit_code)
        if format is not None:
            query_params["format"] = str(format)
        if group is not None:
            query_params["group"] = str(group)
        if job_name is not None:
            query_params["job_name"] = str(job_name)
        if nodes_max is not None:
            query_params["nodes_max"] = str(nodes_max)
        if nodes_min is not None:
            query_params["nodes_min"] = str(nodes_min)
        if partition is not None:
            query_params["partition"] = str(partition)
        if qos is not None:
            query_params["qos"] = str(qos)
        if reason is not None:
            query_params["reason"] = str(reason)
        if reservation is not None:
            query_params["reservation"] = str(reservation)
        if state is not None:
            query_params["state"] = str(state)
        if step is not None:
            query_params["step"] = str(step)
        if node is not None:
            query_params["node"] = str(node)
        if wckey is not None:
            query_params["wckey"] = str(wckey)

        return self.api_client.request(
            type_=m.Dbv0036JobInfo,
            method="GET",
            url="/jobs/",
            params=query_params,
        )

    def _build_for_slurmdbd_get_qos(
        self,
    ) -> Awaitable[m.Dbv0036QosInfo]:
        return self.api_client.request(
            type_=m.Dbv0036QosInfo,
            method="GET",
            url="/qos/",
        )

    def _build_for_slurmdbd_get_single_qos(
        self, qos_name: str
    ) -> Awaitable[m.Dbv0036QosInfo]:
        path_params = {"qos_name": str(qos_name)}

        return self.api_client.request(
            type_=m.Dbv0036QosInfo,
            method="GET",
            url="/qos/{qos_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_get_tres(
        self,
    ) -> Awaitable[m.Dbv0036TresInfo]:
        return self.api_client.request(
            type_=m.Dbv0036TresInfo,
            method="GET",
            url="/tres/",
        )

    def _build_for_slurmdbd_get_user(
        self, user_name: str
    ) -> Awaitable[m.Dbv0036UserInfo]:
        path_params = {"user_name": str(user_name)}

        return self.api_client.request(
            type_=m.Dbv0036UserInfo,
            method="GET",
            url="/user/{user_name}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_get_users(
        self,
    ) -> Awaitable[m.Dbv0036UserInfo]:
        return self.api_client.request(
            type_=m.Dbv0036UserInfo,
            method="GET",
            url="/users/",
        )

    def _build_for_slurmdbd_get_wckey(
        self, wckey: str
    ) -> Awaitable[m.Dbv0036WckeyInfo]:
        path_params = {"wckey": str(wckey)}

        return self.api_client.request(
            type_=m.Dbv0036WckeyInfo,
            method="GET",
            url="/wckey/{wckey}",
            path_params=path_params,
        )

    def _build_for_slurmdbd_get_wckeys(
        self,
    ) -> Awaitable[m.Dbv0036WckeyInfo]:
        return self.api_client.request(
            type_=m.Dbv0036WckeyInfo,
            method="GET",
            url="/wckeys/",
        )

    def _build_for_slurmdbd_set_db_config(
        self,
    ) -> Awaitable[m.Dbv0036ConfigResponse]:
        return self.api_client.request(
            type_=m.Dbv0036ConfigResponse,
            method="POST",
            url="/config",
        )

    def _build_for_slurmdbd_update_account(
        self,
    ) -> Awaitable[m.Dbv0036AccountResponse]:
        return self.api_client.request(
            type_=m.Dbv0036AccountResponse,
            method="POST",
            url="/accounts/",
        )

    def _build_for_slurmdbd_update_tres(
        self,
    ) -> Awaitable[m.Dbv0036ResponseTres]:
        return self.api_client.request(
            type_=m.Dbv0036ResponseTres,
            method="POST",
            url="/tres/",
        )

    def _build_for_slurmdbd_update_users(
        self,
    ) -> Awaitable[m.Dbv0036ResponseUserUpdate]:
        return self.api_client.request(
            type_=m.Dbv0036ResponseUserUpdate,
            method="POST",
            url="/users/",
        )


class AsyncSlurmApi(_SlurmApi):
    async def slurmdbd_add_clusters(
        self,
    ) -> m.Dbv0036ResponseClusterAdd:
        return await self._build_for_slurmdbd_add_clusters()

    async def slurmdbd_add_wckeys(
        self,
    ) -> m.Dbv0036ResponseWckeyAdd:
        return await self._build_for_slurmdbd_add_wckeys()

    async def slurmdbd_delete_account(
        self, account_name: str
    ) -> m.Dbv0036ResponseAccountDelete:
        return await self._build_for_slurmdbd_delete_account(account_name=account_name)

    async def slurmdbd_delete_association(
        self, account: str, user: str, cluster: str = None, partition: str = None
    ) -> m.Dbv0036ResponseAssociationDelete:
        return await self._build_for_slurmdbd_delete_association(
            account=account, user=user, cluster=cluster, partition=partition
        )

    async def slurmdbd_delete_cluster(
        self, cluster_name: str
    ) -> m.Dbv0036ResponseClusterDelete:
        return await self._build_for_slurmdbd_delete_cluster(cluster_name=cluster_name)

    async def slurmdbd_delete_qos(self, qos_name: str) -> m.Dbv0036ResponseQosDelete:
        return await self._build_for_slurmdbd_delete_qos(qos_name=qos_name)

    async def slurmdbd_delete_user(self, user_name: str) -> m.Dbv0036ResponseUserDelete:
        return await self._build_for_slurmdbd_delete_user(user_name=user_name)

    async def slurmdbd_delete_wckey(self, wckey: str) -> m.Dbv0036ResponseWckeyDelete:
        return await self._build_for_slurmdbd_delete_wckey(wckey=wckey)

    async def slurmdbd_diag(
        self,
    ) -> m.Dbv0036Diag:
        return await self._build_for_slurmdbd_diag()

    async def slurmdbd_get_account(self, account_name: str) -> m.Dbv0036AccountInfo:
        return await self._build_for_slurmdbd_get_account(account_name=account_name)

    async def slurmdbd_get_accounts(
        self,
    ) -> m.Dbv0036AccountInfo:
        return await self._build_for_slurmdbd_get_accounts()

    async def slurmdbd_get_association(
        self,
        cluster: str = None,
        account: str = None,
        user: str = None,
        partition: str = None,
    ) -> m.Dbv0036AssociationsInfo:
        return await self._build_for_slurmdbd_get_association(
            cluster=cluster, account=account, user=user, partition=partition
        )

    async def slurmdbd_get_associations(
        self,
    ) -> m.Dbv0036AssociationsInfo:
        return await self._build_for_slurmdbd_get_associations()

    async def slurmdbd_get_cluster(self, cluster_name: str) -> m.Dbv0036ClusterInfo:
        return await self._build_for_slurmdbd_get_cluster(cluster_name=cluster_name)

    async def slurmdbd_get_clusters(
        self,
    ) -> m.Dbv0036ClusterInfo:
        return await self._build_for_slurmdbd_get_clusters()

    async def slurmdbd_get_db_config(
        self,
    ) -> m.Dbv0036ConfigInfo:
        return await self._build_for_slurmdbd_get_db_config()

    async def slurmdbd_get_job(self, job_id: int) -> m.Dbv0036JobInfo:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.
        """
        return await self._build_for_slurmdbd_get_job(job_id=job_id)

    async def slurmdbd_get_jobs(
        self,
        submit_time: str = None,
        start_time: str = None,
        end_time: str = None,
        account: str = None,
        association: str = None,
        cluster: str = None,
        constraints: str = None,
        cpus_max: str = None,
        cpus_min: str = None,
        skip_steps: bool = None,
        disable_wait_for_result: bool = None,
        exit_code: str = None,
        format: str = None,
        group: str = None,
        job_name: str = None,
        nodes_max: str = None,
        nodes_min: str = None,
        partition: str = None,
        qos: str = None,
        reason: str = None,
        reservation: str = None,
        state: str = None,
        step: str = None,
        node: str = None,
        wckey: str = None,
    ) -> m.Dbv0036JobInfo:
        return await self._build_for_slurmdbd_get_jobs(
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            account=account,
            association=association,
            cluster=cluster,
            constraints=constraints,
            cpus_max=cpus_max,
            cpus_min=cpus_min,
            skip_steps=skip_steps,
            disable_wait_for_result=disable_wait_for_result,
            exit_code=exit_code,
            format=format,
            group=group,
            job_name=job_name,
            nodes_max=nodes_max,
            nodes_min=nodes_min,
            partition=partition,
            qos=qos,
            reason=reason,
            reservation=reservation,
            state=state,
            step=step,
            node=node,
            wckey=wckey,
        )

    async def slurmdbd_get_qos(
        self,
    ) -> m.Dbv0036QosInfo:
        return await self._build_for_slurmdbd_get_qos()

    async def slurmdbd_get_single_qos(self, qos_name: str) -> m.Dbv0036QosInfo:
        return await self._build_for_slurmdbd_get_single_qos(qos_name=qos_name)

    async def slurmdbd_get_tres(
        self,
    ) -> m.Dbv0036TresInfo:
        return await self._build_for_slurmdbd_get_tres()

    async def slurmdbd_get_user(self, user_name: str) -> m.Dbv0036UserInfo:
        return await self._build_for_slurmdbd_get_user(user_name=user_name)

    async def slurmdbd_get_users(
        self,
    ) -> m.Dbv0036UserInfo:
        return await self._build_for_slurmdbd_get_users()

    async def slurmdbd_get_wckey(self, wckey: str) -> m.Dbv0036WckeyInfo:
        return await self._build_for_slurmdbd_get_wckey(wckey=wckey)

    async def slurmdbd_get_wckeys(
        self,
    ) -> m.Dbv0036WckeyInfo:
        return await self._build_for_slurmdbd_get_wckeys()

    async def slurmdbd_set_db_config(
        self,
    ) -> m.Dbv0036ConfigResponse:
        return await self._build_for_slurmdbd_set_db_config()

    async def slurmdbd_update_account(
        self,
    ) -> m.Dbv0036AccountResponse:
        return await self._build_for_slurmdbd_update_account()

    async def slurmdbd_update_tres(
        self,
    ) -> m.Dbv0036ResponseTres:
        return await self._build_for_slurmdbd_update_tres()

    async def slurmdbd_update_users(
        self,
    ) -> m.Dbv0036ResponseUserUpdate:
        return await self._build_for_slurmdbd_update_users()


class SyncSlurmApi(_SlurmApi):
    def slurmdbd_add_clusters(
        self,
    ) -> m.Dbv0036ResponseClusterAdd:
        coroutine = self._build_for_slurmdbd_add_clusters()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_add_wckeys(
        self,
    ) -> m.Dbv0036ResponseWckeyAdd:
        coroutine = self._build_for_slurmdbd_add_wckeys()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_delete_account(
        self, account_name: str
    ) -> m.Dbv0036ResponseAccountDelete:
        coroutine = self._build_for_slurmdbd_delete_account(account_name=account_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_delete_association(
        self, account: str, user: str, cluster: str = None, partition: str = None
    ) -> m.Dbv0036ResponseAssociationDelete:
        coroutine = self._build_for_slurmdbd_delete_association(
            account=account, user=user, cluster=cluster, partition=partition
        )
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_delete_cluster(
        self, cluster_name: str
    ) -> m.Dbv0036ResponseClusterDelete:
        coroutine = self._build_for_slurmdbd_delete_cluster(cluster_name=cluster_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_delete_qos(self, qos_name: str) -> m.Dbv0036ResponseQosDelete:
        coroutine = self._build_for_slurmdbd_delete_qos(qos_name=qos_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_delete_user(self, user_name: str) -> m.Dbv0036ResponseUserDelete:
        coroutine = self._build_for_slurmdbd_delete_user(user_name=user_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_delete_wckey(self, wckey: str) -> m.Dbv0036ResponseWckeyDelete:
        coroutine = self._build_for_slurmdbd_delete_wckey(wckey=wckey)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_diag(
        self,
    ) -> m.Dbv0036Diag:
        coroutine = self._build_for_slurmdbd_diag()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_account(self, account_name: str) -> m.Dbv0036AccountInfo:
        coroutine = self._build_for_slurmdbd_get_account(account_name=account_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_accounts(
        self,
    ) -> m.Dbv0036AccountInfo:
        coroutine = self._build_for_slurmdbd_get_accounts()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_association(
        self,
        cluster: str = None,
        account: str = None,
        user: str = None,
        partition: str = None,
    ) -> m.Dbv0036AssociationsInfo:
        coroutine = self._build_for_slurmdbd_get_association(
            cluster=cluster, account=account, user=user, partition=partition
        )
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_associations(
        self,
    ) -> m.Dbv0036AssociationsInfo:
        coroutine = self._build_for_slurmdbd_get_associations()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_cluster(self, cluster_name: str) -> m.Dbv0036ClusterInfo:
        coroutine = self._build_for_slurmdbd_get_cluster(cluster_name=cluster_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_clusters(
        self,
    ) -> m.Dbv0036ClusterInfo:
        coroutine = self._build_for_slurmdbd_get_clusters()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_db_config(
        self,
    ) -> m.Dbv0036ConfigInfo:
        coroutine = self._build_for_slurmdbd_get_db_config()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_job(self, job_id: int) -> m.Dbv0036JobInfo:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.
        """
        coroutine = self._build_for_slurmdbd_get_job(job_id=job_id)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_jobs(
        self,
        submit_time: str = None,
        start_time: str = None,
        end_time: str = None,
        account: str = None,
        association: str = None,
        cluster: str = None,
        constraints: str = None,
        cpus_max: str = None,
        cpus_min: str = None,
        skip_steps: bool = None,
        disable_wait_for_result: bool = None,
        exit_code: str = None,
        format: str = None,
        group: str = None,
        job_name: str = None,
        nodes_max: str = None,
        nodes_min: str = None,
        partition: str = None,
        qos: str = None,
        reason: str = None,
        reservation: str = None,
        state: str = None,
        step: str = None,
        node: str = None,
        wckey: str = None,
    ) -> m.Dbv0036JobInfo:
        coroutine = self._build_for_slurmdbd_get_jobs(
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            account=account,
            association=association,
            cluster=cluster,
            constraints=constraints,
            cpus_max=cpus_max,
            cpus_min=cpus_min,
            skip_steps=skip_steps,
            disable_wait_for_result=disable_wait_for_result,
            exit_code=exit_code,
            format=format,
            group=group,
            job_name=job_name,
            nodes_max=nodes_max,
            nodes_min=nodes_min,
            partition=partition,
            qos=qos,
            reason=reason,
            reservation=reservation,
            state=state,
            step=step,
            node=node,
            wckey=wckey,
        )
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_qos(
        self,
    ) -> m.Dbv0036QosInfo:
        coroutine = self._build_for_slurmdbd_get_qos()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_single_qos(self, qos_name: str) -> m.Dbv0036QosInfo:
        coroutine = self._build_for_slurmdbd_get_single_qos(qos_name=qos_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_tres(
        self,
    ) -> m.Dbv0036TresInfo:
        coroutine = self._build_for_slurmdbd_get_tres()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_user(self, user_name: str) -> m.Dbv0036UserInfo:
        coroutine = self._build_for_slurmdbd_get_user(user_name=user_name)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_users(
        self,
    ) -> m.Dbv0036UserInfo:
        coroutine = self._build_for_slurmdbd_get_users()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_wckey(self, wckey: str) -> m.Dbv0036WckeyInfo:
        coroutine = self._build_for_slurmdbd_get_wckey(wckey=wckey)
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_get_wckeys(
        self,
    ) -> m.Dbv0036WckeyInfo:
        coroutine = self._build_for_slurmdbd_get_wckeys()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_set_db_config(
        self,
    ) -> m.Dbv0036ConfigResponse:
        coroutine = self._build_for_slurmdbd_set_db_config()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_update_account(
        self,
    ) -> m.Dbv0036AccountResponse:
        coroutine = self._build_for_slurmdbd_update_account()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_update_tres(
        self,
    ) -> m.Dbv0036ResponseTres:
        coroutine = self._build_for_slurmdbd_update_tres()
        return get_event_loop().run_until_complete(coroutine)

    def slurmdbd_update_users(
        self,
    ) -> m.Dbv0036ResponseUserUpdate:
        coroutine = self._build_for_slurmdbd_update_users()
        return get_event_loop().run_until_complete(coroutine)
