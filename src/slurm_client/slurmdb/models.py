from typing import Any  # noqa
from typing import List, Optional

from pydantic import BaseModel, Field


class Dbv0036Account(BaseModel):
    associations: "Optional[List[Dbv0036AssociationShortInfo]]" = Field(None, alias="associations")
    coordinators: "Optional[List[Dbv0036CoordinatorInfo]]" = Field(None, alias="coordinators")
    description: "Optional[str]" = Field(None, alias="description")
    name: "Optional[str]" = Field(None, alias="name")
    organization: "Optional[str]" = Field(None, alias="organization")
    flags: "Optional[List[str]]" = Field(None, alias="flags")


class Dbv0036AccountInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    accounts: "Optional[List[Dbv0036Account]]" = Field(None, alias="accounts")


class Dbv0036AccountResponse(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036Association(BaseModel):
    account: "Optional[str]" = Field(None, alias="account")
    cluster: "Optional[str]" = Field(None, alias="cluster")
    default: "Optional[Dbv0036AssociationDefault]" = Field(None, alias="default")
    flags: "Optional[List[str]]" = Field(None, alias="flags")
    max: "Optional[Dbv0036AssociationMax]" = Field(None, alias="max")
    min: "Optional[Dbv0036AssociationMin]" = Field(None, alias="min")
    parent_account: "Optional[str]" = Field(None, alias="parent_account")
    partition: "Optional[str]" = Field(None, alias="partition")
    priority: "Optional[int]" = Field(None, alias="priority")
    qos: "Optional[List[str]]" = Field(None, alias="qos")
    shares_raw: "Optional[int]" = Field(None, alias="shares_raw")
    usage: "Optional[Dbv0036AssociationUsage]" = Field(None, alias="usage")
    user: "Optional[str]" = Field(None, alias="user")


class Dbv0036AssociationDefault(BaseModel):
    qos: "Optional[str]" = Field(None, alias="qos")


class Dbv0036AssociationMax(BaseModel):
    jobs: "Optional[Dbv0036AssociationMaxJobs]" = Field(None, alias="jobs")
    per: "Optional[Dbv0036AssociationMaxPer]" = Field(None, alias="per")
    tres: "Optional[Dbv0036AssociationMaxTres]" = Field(None, alias="tres")


class Dbv0036AssociationMaxJobs(BaseModel):
    per: "Optional[Dbv0036AssociationMaxJobsPer]" = Field(None, alias="per")


class Dbv0036AssociationMaxJobsPer(BaseModel):
    wall_clock: "Optional[int]" = Field(None, alias="wall_clock")


class Dbv0036AssociationMaxPer(BaseModel):
    account: "Optional[Dbv0036AssociationMaxPerAccount]" = Field(None, alias="account")


class Dbv0036AssociationMaxPerAccount(BaseModel):
    wall_clock: "Optional[int]" = Field(None, alias="wall_clock")


class Dbv0036AssociationMaxTres(BaseModel):
    per: "Optional[Dbv0036AssociationMaxTresPer]" = Field(None, alias="per")
    total: "Optional[List[Any]]" = Field(None, alias="total")
    minutes: "Optional[Dbv0036AssociationMaxTresMinutes]" = Field(None, alias="minutes")


class Dbv0036AssociationMaxTresMinutes(BaseModel):
    per: "Optional[Dbv0036AssociationMaxTresMinutesPer]" = Field(None, alias="per")
    total: "Optional[List[Any]]" = Field(None, alias="total")


class Dbv0036AssociationMaxTresMinutesPer(BaseModel):
    job: "Optional[List[Any]]" = Field(None, alias="job")


class Dbv0036AssociationMaxTresPer(BaseModel):
    job: "Optional[List[Any]]" = Field(None, alias="job")
    node: "Optional[List[Any]]" = Field(None, alias="node")


class Dbv0036AssociationMin(BaseModel):
    priority_threshold: "Optional[int]" = Field(None, alias="priority_threshold")


class Dbv0036AssociationShortInfo(BaseModel):
    account: "Optional[str]" = Field(None, alias="account")
    cluster: "Optional[str]" = Field(None, alias="cluster")
    partition: "Optional[str]" = Field(None, alias="partition")
    user: "Optional[str]" = Field(None, alias="user")


class Dbv0036AssociationUsage(BaseModel):
    accrue_job_count: "Optional[int]" = Field(None, alias="accrue_job_count")
    group_used_wallclock: "Optional[float]" = Field(None, alias="group_used_wallclock")
    fairshare_factor: "Optional[float]" = Field(None, alias="fairshare_factor")
    fairshare_shares: "Optional[int]" = Field(None, alias="fairshare_shares")
    normalized_priority: "Optional[int]" = Field(None, alias="normalized_priority")
    normalized_shares: "Optional[float]" = Field(None, alias="normalized_shares")
    effective_normalized_usage: "Optional[float]" = Field(None, alias="effective_normalized_usage")
    raw_usage: "Optional[int]" = Field(None, alias="raw_usage")
    job_count: "Optional[int]" = Field(None, alias="job_count")
    fairshare_level: "Optional[float]" = Field(None, alias="fairshare_level")


class Dbv0036AssociationsInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    associations: "Optional[List[Dbv0036Association]]" = Field(None, alias="associations")


class Dbv0036ClusterInfo(BaseModel):
    controller: "Optional[Dbv0036ClusterInfoController]" = Field(None, alias="controller")
    flags: "Optional[List[str]]" = Field(None, alias="flags")
    name: "Optional[str]" = Field(None, alias="name")
    nodes: "Optional[str]" = Field(None, alias="nodes")
    select_plugin: "Optional[str]" = Field(None, alias="select_plugin")
    associations: "Optional[Dbv0036ClusterInfoAssociations]" = Field(None, alias="associations")
    rpc_version: "Optional[int]" = Field(None, alias="rpc_version")
    tres: "Optional[List[Dbv0036ResponseTres]]" = Field(None, alias="tres")


class Dbv0036ClusterInfoAssociations(BaseModel):
    root: "Optional[Dbv0036AssociationShortInfo]" = Field(None, alias="root")


class Dbv0036ClusterInfoController(BaseModel):
    host: "Optional[str]" = Field(None, alias="host")
    port: "Optional[int]" = Field(None, alias="port")


class Dbv0036ConfigInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    tres: "Optional[List[List[Any]]]" = Field(None, alias="tres")
    accounts: "Optional[List[Dbv0036Account]]" = Field(None, alias="accounts")
    associations: "Optional[List[Dbv0036Association]]" = Field(None, alias="associations")
    users: "Optional[List[Dbv0036User]]" = Field(None, alias="users")
    qos: "Optional[List[Dbv0036Qos]]" = Field(None, alias="qos")
    wckeys: "Optional[List[Dbv0036Wckey]]" = Field(None, alias="wckeys")


class Dbv0036ConfigResponse(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036CoordinatorInfo(BaseModel):
    name: "Optional[str]" = Field(None, alias="name")
    direct: "Optional[int]" = Field(None, alias="direct")


class Dbv0036Diag(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    time_start: "Optional[int]" = Field(None, alias="time_start")
    rollups: "Optional[List[Dbv0036DiagRollups]]" = Field(None, alias="rollups")
    rp_cs: "Optional[List[Dbv0036DiagRPCs]]" = Field(None, alias="RPCs")
    users: "Optional[List[Dbv0036DiagUsers]]" = Field(None, alias="users")


class Dbv0036DiagRollups(BaseModel):
    type: "Optional[str]" = Field(None, alias="type")
    last_run: "Optional[int]" = Field(None, alias="last_run")
    last_cycle: "Optional[int]" = Field(None, alias="last_cycle")
    max_cycle: "Optional[int]" = Field(None, alias="max_cycle")
    total_time: "Optional[int]" = Field(None, alias="total_time")
    mean_cycles: "Optional[int]" = Field(None, alias="mean_cycles")


class Dbv0036DiagRPCs(BaseModel):
    rpc: "Optional[str]" = Field(None, alias="rpc")
    count: "Optional[int]" = Field(None, alias="count")
    time: "Optional[Dbv0036DiagTime]" = Field(None, alias="time")


class Dbv0036DiagTime(BaseModel):
    average: "Optional[int]" = Field(None, alias="average")
    total: "Optional[int]" = Field(None, alias="total")


class Dbv0036DiagUsers(BaseModel):
    user: "Optional[str]" = Field(None, alias="user")
    count: "Optional[int]" = Field(None, alias="count")
    time: "Optional[Dbv0036DiagTime]" = Field(None, alias="time")


class Dbv0036Error(BaseModel):
    errno: "Optional[int]" = Field(None, alias="errno")
    error: "Optional[str]" = Field(None, alias="error")


class Dbv0036Job(BaseModel):
    account: "Optional[str]" = Field(None, alias="account")
    comment: "Optional[Dbv0036JobComment]" = Field(None, alias="comment")
    allocation_nodes: "Optional[str]" = Field(None, alias="allocation_nodes")
    array: "Optional[Dbv0036JobArray]" = Field(None, alias="array")
    time: "Optional[Dbv0036JobTime]" = Field(None, alias="time")
    association: "Optional[Dbv0036AssociationShortInfo]" = Field(None, alias="association")
    cluster: "Optional[str]" = Field(None, alias="cluster")
    constraints: "Optional[str]" = Field(None, alias="constraints")
    derived_exit_code: "Optional[Dbv0036JobExitCode]" = Field(None, alias="derived_exit_code")
    exit_code: "Optional[Dbv0036JobExitCode]" = Field(None, alias="exit_code")
    flags: "Optional[List[str]]" = Field(None, alias="flags")
    group: "Optional[str]" = Field(None, alias="group")
    het: "Optional[Dbv0036JobHet]" = Field(None, alias="het")
    job_id: "Optional[int]" = Field(None, alias="job_id")
    name: "Optional[str]" = Field(None, alias="name")
    mcs: "Optional[Dbv0036JobMcs]" = Field(None, alias="mcs")
    nodes: "Optional[str]" = Field(None, alias="nodes")
    partition: "Optional[str]" = Field(None, alias="partition")
    priority: "Optional[int]" = Field(None, alias="priority")
    qos: "Optional[str]" = Field(None, alias="qos")
    required: "Optional[Dbv0036JobRequired]" = Field(None, alias="required")
    kill_request_user: "Optional[str]" = Field(None, alias="kill_request_user")
    reservation: "Optional[Dbv0036JobReservation]" = Field(None, alias="reservation")
    state: "Optional[Dbv0036JobState]" = Field(None, alias="state")
    steps: "Optional[List[Dbv0036JobStep]]" = Field(None, alias="steps")
    tres: "Optional[Dbv0036JobTres]" = Field(None, alias="tres")
    user: "Optional[str]" = Field(None, alias="user")
    wckey: "Optional[Dbv0036JobWckey]" = Field(None, alias="wckey")
    working_directory: "Optional[str]" = Field(None, alias="working_directory")


class Dbv0036JobArray(BaseModel):
    job_id: "Optional[int]" = Field(None, alias="job_id")
    limits: "Optional[Dbv0036JobArrayLimits]" = Field(None, alias="limits")
    task: "Optional[str]" = Field(None, alias="task")
    task_id: "Optional[int]" = Field(None, alias="task_id")


class Dbv0036JobArrayLimits(BaseModel):
    max: "Optional[Dbv0036JobArrayLimitsMax]" = Field(None, alias="max")


class Dbv0036JobArrayLimitsMax(BaseModel):
    running: "Optional[Dbv0036JobArrayLimitsMaxRunning]" = Field(None, alias="running")


class Dbv0036JobArrayLimitsMaxRunning(BaseModel):
    tasks: "Optional[int]" = Field(None, alias="tasks")


class Dbv0036JobComment(BaseModel):
    administrator: "Optional[str]" = Field(None, alias="administrator")
    job: "Optional[str]" = Field(None, alias="job")
    system: "Optional[str]" = Field(None, alias="system")


class Dbv0036JobExitCode(BaseModel):
    status: "Optional[str]" = Field(None, alias="status")
    return_code: "Optional[int]" = Field(None, alias="return_code")
    signal: "Optional[Dbv0036JobExitCodeSignal]" = Field(None, alias="signal")


class Dbv0036JobExitCodeSignal(BaseModel):
    signal_id: "Optional[int]" = Field(None, alias="signal_id")
    name: "Optional[str]" = Field(None, alias="name")


class Dbv0036JobHet(BaseModel):
    job_id: "Optional[Any]" = Field(None, alias="job_id")
    job_offset: "Optional[Any]" = Field(None, alias="job_offset")


class Dbv0036JobInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    jobs: "Optional[List[Dbv0036Job]]" = Field(None, alias="jobs")


class Dbv0036JobMcs(BaseModel):
    label: "Optional[str]" = Field(None, alias="label")


class Dbv0036JobRequired(BaseModel):
    cp_us: "Optional[int]" = Field(None, alias="CPUs")
    memory: "Optional[int]" = Field(None, alias="memory")


class Dbv0036JobReservation(BaseModel):
    id: "Optional[int]" = Field(None, alias="id")
    name: "Optional[int]" = Field(None, alias="name")


class Dbv0036JobState(BaseModel):
    current: "Optional[str]" = Field(None, alias="current")
    previous: "Optional[str]" = Field(None, alias="previous")


class Dbv0036JobStep(BaseModel):
    time: "Optional[Dbv0036JobStepTime]" = Field(None, alias="time")
    exit_code: "Optional[Dbv0036JobExitCode]" = Field(None, alias="exit_code")
    nodes: "Optional[Dbv0036JobStepNodes]" = Field(None, alias="nodes")
    tasks: "Optional[Dbv0036JobStepTasks]" = Field(None, alias="tasks")
    pid: "Optional[str]" = Field(None, alias="pid")
    cpu: "Optional[Dbv0036JobStepCPU]" = Field(None, alias="CPU")
    kill_request_user: "Optional[str]" = Field(None, alias="kill_request_user")
    state: "Optional[str]" = Field(None, alias="state")
    statistics: "Optional[Dbv0036JobStepStatistics]" = Field(None, alias="statistics")
    step: "Optional[Dbv0036JobStepStep]" = Field(None, alias="step")


class Dbv0036JobStepCPU(BaseModel):
    requested_frequency: "Optional[Dbv0036JobStepCPURequestedFrequency]" = Field(None, alias="requested_frequency")
    governor: "Optional[List[str]]" = Field(None, alias="governor")


class Dbv0036JobStepCPURequestedFrequency(BaseModel):
    min: "Optional[int]" = Field(None, alias="min")
    max: "Optional[int]" = Field(None, alias="max")


class Dbv0036JobStepNodes(BaseModel):
    count: "Optional[int]" = Field(None, alias="count")
    range: "Optional[str]" = Field(None, alias="range")


class Dbv0036JobStepStatistics(BaseModel):
    cpu: "Optional[Dbv0036JobStepStatisticsCPU]" = Field(None, alias="CPU")
    energy: "Optional[Dbv0036JobStepStatisticsEnergy]" = Field(None, alias="energy")


class Dbv0036JobStepStatisticsCPU(BaseModel):
    actual_frequency: "Optional[int]" = Field(None, alias="actual_frequency")


class Dbv0036JobStepStatisticsEnergy(BaseModel):
    consumed: "Optional[int]" = Field(None, alias="consumed")


class Dbv0036JobStepStep(BaseModel):
    job_id: "Optional[int]" = Field(None, alias="job_id")
    het: "Optional[Dbv0036JobStepStepHet]" = Field(None, alias="het")
    id: "Optional[str]" = Field(None, alias="id")
    name: "Optional[str]" = Field(None, alias="name")
    task: "Optional[Dbv0036JobStepStepTask]" = Field(None, alias="task")
    tres: "Optional[Dbv0036JobStepStepTres]" = Field(None, alias="tres")


class Dbv0036JobStepStepHet(BaseModel):
    component: "Optional[int]" = Field(None, alias="component")


class Dbv0036JobStepStepTask(BaseModel):
    distribution: "Optional[str]" = Field(None, alias="distribution")


class Dbv0036JobStepStepTres(BaseModel):
    requested: "Optional[Dbv0036JobStepStepTresRequested]" = Field(None, alias="requested")
    consumed: "Optional[Dbv0036JobStepStepTresRequested]" = Field(None, alias="consumed")
    allocated: "Optional[List[Any]]" = Field(None, alias="allocated")


class Dbv0036JobStepStepTresRequested(BaseModel):
    average: "Optional[List[Any]]" = Field(None, alias="average")
    max: "Optional[List[Any]]" = Field(None, alias="max")
    min: "Optional[List[Any]]" = Field(None, alias="min")
    total: "Optional[List[Any]]" = Field(None, alias="total")


class Dbv0036JobStepTasks(BaseModel):
    count: "Optional[int]" = Field(None, alias="count")


class Dbv0036JobStepTime(BaseModel):
    elapsed: "Optional[int]" = Field(None, alias="elapsed")
    end: "Optional[int]" = Field(None, alias="end")
    start: "Optional[int]" = Field(None, alias="start")
    suspended: "Optional[int]" = Field(None, alias="suspended")
    system: "Optional[Dbv0036JobTimeSystem]" = Field(None, alias="system")
    total: "Optional[Dbv0036JobTimeTotal]" = Field(None, alias="total")
    user: "Optional[Dbv0036JobTimeUser]" = Field(None, alias="user")


class Dbv0036JobTime(BaseModel):
    elapsed: "Optional[int]" = Field(None, alias="elapsed")
    eligible: "Optional[int]" = Field(None, alias="eligible")
    end: "Optional[int]" = Field(None, alias="end")
    start: "Optional[int]" = Field(None, alias="start")
    submission: "Optional[int]" = Field(None, alias="submission")
    suspended: "Optional[int]" = Field(None, alias="suspended")
    system: "Optional[Dbv0036JobTimeSystem]" = Field(None, alias="system")
    total: "Optional[Dbv0036JobTimeTotal]" = Field(None, alias="total")
    user: "Optional[Dbv0036JobTimeUser]" = Field(None, alias="user")
    limit: "Optional[int]" = Field(None, alias="limit")


class Dbv0036JobTimeSystem(BaseModel):
    seconds: "Optional[int]" = Field(None, alias="seconds")
    microseconds: "Optional[int]" = Field(None, alias="microseconds")


class Dbv0036JobTimeTotal(BaseModel):
    seconds: "Optional[int]" = Field(None, alias="seconds")
    microseconds: "Optional[int]" = Field(None, alias="microseconds")


class Dbv0036JobTimeUser(BaseModel):
    seconds: "Optional[int]" = Field(None, alias="seconds")
    microseconds: "Optional[int]" = Field(None, alias="microseconds")


class Dbv0036JobTres(BaseModel):
    allocated: "Optional[List[Any]]" = Field(None, alias="allocated")
    requested: "Optional[List[Any]]" = Field(None, alias="requested")


class Dbv0036JobWckey(BaseModel):
    wckey: "Optional[str]" = Field(None, alias="wckey")
    flags: "Optional[List[str]]" = Field(None, alias="flags")


class Dbv0036Qos(BaseModel):
    description: "Optional[str]" = Field(None, alias="description")
    flags: "Optional[List[str]]" = Field(None, alias="flags")
    id: "Optional[str]" = Field(None, alias="id")
    limits: "Optional[Dbv0036QosLimits]" = Field(None, alias="limits")
    preempt: "Optional[Dbv0036QosPreempt]" = Field(None, alias="preempt")
    priority: "Optional[int]" = Field(None, alias="priority")
    usage_factor: "Optional[float]" = Field(None, alias="usage_factor")
    usage_threshold: "Optional[float]" = Field(None, alias="usage_threshold")


class Dbv0036QosInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    qos: "Optional[List[Dbv0036Qos]]" = Field(None, alias="qos")


class Dbv0036QosLimits(BaseModel):
    max: "Optional[Dbv0036QosLimitsMax]" = Field(None, alias="max")
    min: "Optional[Dbv0036QosLimitsMin]" = Field(None, alias="min")


class Dbv0036QosLimitsMax(BaseModel):
    wall_clock: "Optional[Dbv0036QosLimitsMaxWallClock]" = Field(None, alias="wall_clock")
    jobs: "Optional[Dbv0036QosLimitsMaxJobs]" = Field(None, alias="jobs")
    accruing: "Optional[Dbv0036QosLimitsMaxAccruing]" = Field(None, alias="accruing")
    tres: "Optional[Dbv0036QosLimitsMaxTres]" = Field(None, alias="tres")


class Dbv0036QosLimitsMaxAccruing(BaseModel):
    per: "Optional[Dbv0036QosLimitsMaxAccruingPer]" = Field(None, alias="per")


class Dbv0036QosLimitsMaxAccruingPer(BaseModel):
    account: "Optional[int]" = Field(None, alias="account")
    user: "Optional[int]" = Field(None, alias="user")


class Dbv0036QosLimitsMaxJobs(BaseModel):
    per: "Optional[Dbv0036QosLimitsMaxJobsPer]" = Field(None, alias="per")


class Dbv0036QosLimitsMaxJobsPer(BaseModel):
    account: "Optional[int]" = Field(None, alias="account")
    user: "Optional[int]" = Field(None, alias="user")


class Dbv0036QosLimitsMaxTres(BaseModel):
    minutes: "Optional[Dbv0036QosLimitsMaxTresMinutes]" = Field(None, alias="minutes")
    per: "Optional[Dbv0036QosLimitsMaxTresPer]" = Field(None, alias="per")


class Dbv0036QosLimitsMaxTresMinutes(BaseModel):
    per: "Optional[Dbv0036QosLimitsMaxTresMinutesPer]" = Field(None, alias="per")


class Dbv0036QosLimitsMaxTresMinutesPer(BaseModel):
    job: "Optional[List[Any]]" = Field(None, alias="job")
    account: "Optional[List[Any]]" = Field(None, alias="account")
    user: "Optional[List[Any]]" = Field(None, alias="user")


class Dbv0036QosLimitsMaxTresPer(BaseModel):
    account: "Optional[List[Any]]" = Field(None, alias="account")
    job: "Optional[List[Any]]" = Field(None, alias="job")
    node: "Optional[List[Any]]" = Field(None, alias="node")
    user: "Optional[List[Any]]" = Field(None, alias="user")


class Dbv0036QosLimitsMaxWallClock(BaseModel):
    per: "Optional[Dbv0036QosLimitsMaxWallClockPer]" = Field(None, alias="per")


class Dbv0036QosLimitsMaxWallClockPer(BaseModel):
    qos: "Optional[int]" = Field(None, alias="qos")
    job: "Optional[int]" = Field(None, alias="job")


class Dbv0036QosLimitsMin(BaseModel):
    priority_threshold: "Optional[int]" = Field(None, alias="priority_threshold")
    tres: "Optional[Dbv0036QosLimitsMinTres]" = Field(None, alias="tres")


class Dbv0036QosLimitsMinTres(BaseModel):
    per: "Optional[Dbv0036QosLimitsMinTresPer]" = Field(None, alias="per")


class Dbv0036QosLimitsMinTresPer(BaseModel):
    job: "Optional[List[Any]]" = Field(None, alias="job")


class Dbv0036QosPreempt(BaseModel):
    list: "Optional[List[str]]" = Field(None, alias="list")
    mode: "Optional[List[str]]" = Field(None, alias="mode")
    exempt_time: "Optional[int]" = Field(None, alias="exempt_time")


class Dbv0036ResponseAccountDelete(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseAssociationDelete(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseClusterAdd(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseClusterDelete(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseQosDelete(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseTres(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseUserDelete(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseUserUpdate(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseWckeyAdd(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036ResponseWckeyDelete(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")


class Dbv0036TresInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    tres: "Optional[List[List[Any]]]" = Field(None, alias="tres")


class Dbv0036User(BaseModel):
    administrator_level: "Optional[str]" = Field(None, alias="administrator_level")
    associations: "Optional[Dbv0036UserAssociations]" = Field(None, alias="associations")
    coordinators: "Optional[List[Dbv0036CoordinatorInfo]]" = Field(None, alias="coordinators")
    default: "Optional[Dbv0036UserDefault]" = Field(None, alias="default")
    name: "Optional[str]" = Field(None, alias="name")


class Dbv0036UserAssociations(BaseModel):
    root: "Optional[Dbv0036AssociationShortInfo]" = Field(None, alias="root")


class Dbv0036UserDefault(BaseModel):
    account: "Optional[str]" = Field(None, alias="account")
    wckey: "Optional[str]" = Field(None, alias="wckey")


class Dbv0036UserInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    users: "Optional[List[Dbv0036User]]" = Field(None, alias="users")


class Dbv0036Wckey(BaseModel):
    accounts: "Optional[List[str]]" = Field(None, alias="accounts")
    cluster: "Optional[str]" = Field(None, alias="cluster")
    id: "Optional[int]" = Field(None, alias="id")
    name: "Optional[str]" = Field(None, alias="name")
    user: "Optional[str]" = Field(None, alias="user")
    flags: "Optional[List[str]]" = Field(None, alias="flags")


class Dbv0036WckeyInfo(BaseModel):
    errors: "Optional[List[Dbv0036Error]]" = Field(None, alias="errors")
    wckeys: "Optional[List[Dbv0036Wckey]]" = Field(None, alias="wckeys")
