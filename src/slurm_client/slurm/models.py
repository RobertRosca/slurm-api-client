from enum import Enum
from typing import Any  # noqa
from typing import List, Optional

from pydantic import BaseModel, Field
from typing_extensions import Literal


class V0036Diag(BaseModel):
    errors: "Optional[List[V0036Error]]" = Field(None, alias="errors")
    statistics: "Optional[V0036DiagStatistics]" = Field(None, alias="statistics")


class V0036DiagStatistics(BaseModel):
    parts_packed: "Optional[int]" = Field(None, alias="parts_packed")
    req_time: "Optional[int]" = Field(None, alias="req_time")
    req_time_start: "Optional[int]" = Field(None, alias="req_time_start")
    server_thread_count: "Optional[int]" = Field(None, alias="server_thread_count")
    agent_queue_size: "Optional[int]" = Field(None, alias="agent_queue_size")
    agent_count: "Optional[int]" = Field(None, alias="agent_count")
    agent_thread_count: "Optional[int]" = Field(None, alias="agent_thread_count")
    dbd_agent_queue_size: "Optional[int]" = Field(None, alias="dbd_agent_queue_size")
    gettimeofday_latency: "Optional[int]" = Field(None, alias="gettimeofday_latency")
    schedule_cycle_max: "Optional[int]" = Field(None, alias="schedule_cycle_max")
    schedule_cycle_last: "Optional[int]" = Field(None, alias="schedule_cycle_last")
    schedule_cycle_total: "Optional[int]" = Field(None, alias="schedule_cycle_total")
    schedule_cycle_mean: "Optional[int]" = Field(None, alias="schedule_cycle_mean")
    schedule_cycle_mean_depth: "Optional[int]" = Field(
        None, alias="schedule_cycle_mean_depth"
    )
    schedule_cycle_per_minute: "Optional[int]" = Field(
        None, alias="schedule_cycle_per_minute"
    )
    schedule_queue_length: "Optional[int]" = Field(None, alias="schedule_queue_length")
    jobs_submitted: "Optional[int]" = Field(None, alias="jobs_submitted")
    jobs_started: "Optional[int]" = Field(None, alias="jobs_started")
    jobs_completed: "Optional[int]" = Field(None, alias="jobs_completed")
    jobs_canceled: "Optional[int]" = Field(None, alias="jobs_canceled")
    jobs_failed: "Optional[int]" = Field(None, alias="jobs_failed")
    jobs_pending: "Optional[int]" = Field(None, alias="jobs_pending")
    jobs_running: "Optional[int]" = Field(None, alias="jobs_running")
    job_states_ts: "Optional[int]" = Field(None, alias="job_states_ts")
    bf_backfilled_jobs: "Optional[int]" = Field(None, alias="bf_backfilled_jobs")
    bf_last_backfilled_jobs: "Optional[int]" = Field(
        None, alias="bf_last_backfilled_jobs"
    )
    bf_backfilled_het_jobs: "Optional[int]" = Field(
        None, alias="bf_backfilled_het_jobs"
    )
    bf_cycle_counter: "Optional[int]" = Field(None, alias="bf_cycle_counter")
    bf_cycle_mean: "Optional[int]" = Field(None, alias="bf_cycle_mean")
    bf_cycle_max: "Optional[int]" = Field(None, alias="bf_cycle_max")
    bf_last_depth: "Optional[int]" = Field(None, alias="bf_last_depth")
    bf_last_depth_try: "Optional[int]" = Field(None, alias="bf_last_depth_try")
    bf_depth_mean: "Optional[int]" = Field(None, alias="bf_depth_mean")
    bf_depth_mean_try: "Optional[int]" = Field(None, alias="bf_depth_mean_try")
    bf_cycle_last: "Optional[int]" = Field(None, alias="bf_cycle_last")
    bf_queue_len: "Optional[int]" = Field(None, alias="bf_queue_len")
    bf_queue_len_mean: "Optional[int]" = Field(None, alias="bf_queue_len_mean")
    bf_when_last_cycle: "Optional[int]" = Field(None, alias="bf_when_last_cycle")
    bf_active: "Optional[bool]" = Field(None, alias="bf_active")


class V0036Error(BaseModel):
    error: "Optional[str]" = Field(None, alias="error")
    errno: "Optional[int]" = Field(None, alias="errno")


class V0036JobProperties(BaseModel):
    account: "Optional[str]" = Field(None, alias="account")
    account_gather_freqency: "Optional[str]" = Field(
        None, alias="account_gather_freqency"
    )
    argv: "Optional[List[str]]" = Field(None, alias="argv")
    array: "Optional[str]" = Field(None, alias="array")
    batch_features: "Optional[str]" = Field(None, alias="batch_features")
    begin_time: "Optional[str]" = Field(None, alias="begin_time")
    burst_buffer: "Optional[str]" = Field(None, alias="burst_buffer")
    cluster_constraints: "Optional[str]" = Field(None, alias="cluster_constraints")
    comment: "Optional[str]" = Field(None, alias="comment")
    constraints: "Optional[str]" = Field(None, alias="constraints")
    core_specification: "Optional[int]" = Field(None, alias="core_specification")
    cores_per_socket: "Optional[int]" = Field(None, alias="cores_per_socket")
    cpu_binding: "Optional[str]" = Field(None, alias="cpu_binding")
    cpu_binding_hint: "Optional[str]" = Field(None, alias="cpu_binding_hint")
    cpu_frequency: "Optional[str]" = Field(None, alias="cpu_frequency")
    cpus_per_gpu: "Optional[str]" = Field(None, alias="cpus_per_gpu")
    cpus_per_task: "Optional[int]" = Field(None, alias="cpus_per_task")
    current_working_directory: "Optional[str]" = Field(
        None, alias="current_working_directory"
    )
    deadline: "Optional[str]" = Field(None, alias="deadline")
    delay_boot: "Optional[int]" = Field(None, alias="delay_boot")
    dependency: "Optional[str]" = Field(None, alias="dependency")
    distribution: "Optional[str]" = Field(None, alias="distribution")
    environment: "Any" = Field(..., alias="environment")
    exclusive: "Literal['user', 'mcs', 'true', 'false']" = Field(
        None, alias="exclusive"
    )
    get_user_environment: "Optional[bool]" = Field(None, alias="get_user_environment")
    gres: "Optional[str]" = Field(None, alias="gres")
    gres_flags: "Literal['disable-binding', 'enforce-binding']" = Field(
        None, alias="gres_flags"
    )
    gpu_binding: "Optional[str]" = Field(None, alias="gpu_binding")
    gpu_frequency: "Optional[str]" = Field(None, alias="gpu_frequency")
    gpus: "Optional[str]" = Field(None, alias="gpus")
    gpus_per_node: "Optional[str]" = Field(None, alias="gpus_per_node")
    gpus_per_socket: "Optional[str]" = Field(None, alias="gpus_per_socket")
    gpus_per_task: "Optional[str]" = Field(None, alias="gpus_per_task")
    hold: "Optional[bool]" = Field(None, alias="hold")
    kill_on_invalid_dependency: "Optional[bool]" = Field(
        None, alias="kill_on_invalid_dependency"
    )
    licenses: "Optional[str]" = Field(None, alias="licenses")
    mail_type: "Optional[str]" = Field(None, alias="mail_type")
    mail_user: "Optional[str]" = Field(None, alias="mail_user")
    mcs_label: "Optional[str]" = Field(None, alias="mcs_label")
    memory_binding: "Optional[str]" = Field(None, alias="memory_binding")
    memory_per_cpu: "Optional[int]" = Field(None, alias="memory_per_cpu")
    memory_per_gpu: "Optional[int]" = Field(None, alias="memory_per_gpu")
    memory_per_node: "Optional[int]" = Field(None, alias="memory_per_node")
    minimum_cpus_per_node: "Optional[int]" = Field(None, alias="minimum_cpus_per_node")
    minimum_nodes: "Optional[bool]" = Field(None, alias="minimum_nodes")
    name: "Optional[str]" = Field(None, alias="name")
    nice: "Optional[str]" = Field(None, alias="nice")
    no_kill: "Optional[bool]" = Field(None, alias="no_kill")
    nodes: "Optional[List[int]]" = Field(None, alias="nodes")
    open_mode: "Literal['append', 'truncate']" = Field(None, alias="open_mode")
    partition: "Optional[str]" = Field(None, alias="partition")
    priority: "Optional[str]" = Field(None, alias="priority")
    qos: "Optional[str]" = Field(None, alias="qos")
    requeue: "Optional[bool]" = Field(None, alias="requeue")
    reservation: "Optional[str]" = Field(None, alias="reservation")
    signal: "Optional[str]" = Field(None, alias="signal")
    sockets_per_node: "Optional[int]" = Field(None, alias="sockets_per_node")
    spread_job: "Optional[bool]" = Field(None, alias="spread_job")
    standard_error: "Optional[str]" = Field(None, alias="standard_error")
    standard_in: "Optional[str]" = Field(None, alias="standard_in")
    standard_out: "Optional[str]" = Field(None, alias="standard_out")
    tasks: "Optional[int]" = Field(None, alias="tasks")
    tasks_per_core: "Optional[int]" = Field(None, alias="tasks_per_core")
    tasks_per_node: "Optional[int]" = Field(None, alias="tasks_per_node")
    tasks_per_socket: "Optional[int]" = Field(None, alias="tasks_per_socket")
    thread_specification: "Optional[int]" = Field(None, alias="thread_specification")
    threads_per_core: "Optional[int]" = Field(None, alias="threads_per_core")
    time_limit: "Optional[int]" = Field(None, alias="time_limit")
    time_minimum: "Optional[int]" = Field(None, alias="time_minimum")
    wait_all_nodes: "Optional[bool]" = Field(None, alias="wait_all_nodes")
    wckey: "Optional[str]" = Field(None, alias="wckey")


class V0036JobResources(BaseModel):
    nodes: "Optional[str]" = Field(None, alias="nodes")
    allocated_cpus: "Optional[int]" = Field(None, alias="allocated_cpus")
    allocated_hosts: "Optional[int]" = Field(None, alias="allocated_hosts")
    allocated_nodes: "Optional[List[V0036NodeAllocation]]" = Field(
        None, alias="allocated_nodes"
    )


class V0036JobResponseProperties(BaseModel):
    account: "Optional[str]" = Field(None, alias="account")
    accrue_time: "Optional[str]" = Field(None, alias="accrue_time")
    admin_comment: "Optional[str]" = Field(None, alias="admin_comment")
    array_job_id: "Optional[str]" = Field(None, alias="array_job_id")
    array_task_id: "Optional[str]" = Field(None, alias="array_task_id")
    array_max_tasks: "Optional[str]" = Field(None, alias="array_max_tasks")
    array_task_string: "Optional[str]" = Field(None, alias="array_task_string")
    association_id: "Optional[str]" = Field(None, alias="association_id")
    batch_features: "Optional[str]" = Field(None, alias="batch_features")
    batch_flag: "Optional[bool]" = Field(None, alias="batch_flag")
    batch_host: "Optional[str]" = Field(None, alias="batch_host")
    flags: "Optional[List[str]]" = Field(None, alias="flags")
    burst_buffer: "Optional[str]" = Field(None, alias="burst_buffer")
    burst_buffer_state: "Optional[str]" = Field(None, alias="burst_buffer_state")
    cluster: "Optional[str]" = Field(None, alias="cluster")
    cluster_features: "Optional[str]" = Field(None, alias="cluster_features")
    command: "Optional[str]" = Field(None, alias="command")
    comment: "Optional[str]" = Field(None, alias="comment")
    contiguous: "Optional[bool]" = Field(None, alias="contiguous")
    core_spec: "Optional[str]" = Field(None, alias="core_spec")
    thread_spec: "Optional[str]" = Field(None, alias="thread_spec")
    cores_per_socket: "Optional[str]" = Field(None, alias="cores_per_socket")
    billable_tres: "Optional[str]" = Field(None, alias="billable_tres")
    cpus_per_task: "Optional[str]" = Field(None, alias="cpus_per_task")
    cpu_frequency_minimum: "Optional[str]" = Field(None, alias="cpu_frequency_minimum")
    cpu_frequency_maximum: "Optional[str]" = Field(None, alias="cpu_frequency_maximum")
    cpu_frequency_governor: "Optional[str]" = Field(
        None, alias="cpu_frequency_governor"
    )
    cpus_per_tres: "Optional[str]" = Field(None, alias="cpus_per_tres")
    deadline: "Optional[str]" = Field(None, alias="deadline")
    delay_boot: "Optional[str]" = Field(None, alias="delay_boot")
    dependency: "Optional[str]" = Field(None, alias="dependency")
    derived_exit_code: "Optional[str]" = Field(None, alias="derived_exit_code")
    eligible_time: "Optional[str]" = Field(None, alias="eligible_time")
    end_time: "Optional[str]" = Field(None, alias="end_time")
    excluded_nodes: "Optional[str]" = Field(None, alias="excluded_nodes")
    exit_code: "Optional[int]" = Field(None, alias="exit_code")
    features: "Optional[str]" = Field(None, alias="features")
    federation_origin: "Optional[str]" = Field(None, alias="federation_origin")
    federation_siblings_active: "Optional[str]" = Field(
        None, alias="federation_siblings_active"
    )
    federation_siblings_viable: "Optional[str]" = Field(
        None, alias="federation_siblings_viable"
    )
    gres_detail: "Optional[List[str]]" = Field(None, alias="gres_detail")
    group_id: "Optional[str]" = Field(None, alias="group_id")
    job_id: "Optional[str]" = Field(None, alias="job_id")
    job_resources: "Optional[V0036JobResources]" = Field(None, alias="job_resources")
    job_state: "Optional[str]" = Field(None, alias="job_state")
    last_sched_evaluation: "Optional[str]" = Field(None, alias="last_sched_evaluation")
    licenses: "Optional[str]" = Field(None, alias="licenses")
    max_cpus: "Optional[str]" = Field(None, alias="max_cpus")
    max_nodes: "Optional[str]" = Field(None, alias="max_nodes")
    mcs_label: "Optional[str]" = Field(None, alias="mcs_label")
    memory_per_tres: "Optional[str]" = Field(None, alias="memory_per_tres")
    name: "Optional[str]" = Field(None, alias="name")
    nodes: "Optional[str]" = Field(None, alias="nodes")
    nice: "Optional[str]" = Field(None, alias="nice")
    tasks_per_core: "Optional[str]" = Field(None, alias="tasks_per_core")
    tasks_per_socket: "Optional[str]" = Field(None, alias="tasks_per_socket")
    tasks_per_board: "Optional[str]" = Field(None, alias="tasks_per_board")
    cpus: "Optional[str]" = Field(None, alias="cpus")
    node_count: "Optional[str]" = Field(None, alias="node_count")
    tasks: "Optional[str]" = Field(None, alias="tasks")
    het_job_id: "Optional[str]" = Field(None, alias="het_job_id")
    het_job_id_set: "Optional[str]" = Field(None, alias="het_job_id_set")
    het_job_offset: "Optional[str]" = Field(None, alias="het_job_offset")
    partition: "Optional[str]" = Field(None, alias="partition")
    memory_per_node: "Optional[str]" = Field(None, alias="memory_per_node")
    memory_per_cpu: "Optional[str]" = Field(None, alias="memory_per_cpu")
    minimum_cpus_per_node: "Optional[str]" = Field(None, alias="minimum_cpus_per_node")
    minimum_tmp_disk_per_node: "Optional[str]" = Field(
        None, alias="minimum_tmp_disk_per_node"
    )
    preempt_time: "Optional[str]" = Field(None, alias="preempt_time")
    pre_sus_time: "Optional[str]" = Field(None, alias="pre_sus_time")
    priority: "Optional[str]" = Field(None, alias="priority")
    profile: "Optional[List[str]]" = Field(None, alias="profile")
    qos: "Optional[str]" = Field(None, alias="qos")
    reboot: "Optional[bool]" = Field(None, alias="reboot")
    required_nodes: "Optional[str]" = Field(None, alias="required_nodes")
    requeue: "Optional[bool]" = Field(None, alias="requeue")
    resize_time: "Optional[str]" = Field(None, alias="resize_time")
    restart_cnt: "Optional[str]" = Field(None, alias="restart_cnt")
    resv_name: "Optional[str]" = Field(None, alias="resv_name")
    shared: "Optional[str]" = Field(None, alias="shared")
    show_flags: "Optional[List[str]]" = Field(None, alias="show_flags")
    sockets_per_board: "Optional[str]" = Field(None, alias="sockets_per_board")
    sockets_per_node: "Optional[str]" = Field(None, alias="sockets_per_node")
    start_time: "Optional[str]" = Field(None, alias="start_time")
    state_description: "Optional[str]" = Field(None, alias="state_description")
    state_reason: "Optional[str]" = Field(None, alias="state_reason")
    standard_error: "Optional[str]" = Field(None, alias="standard_error")
    standard_input: "Optional[str]" = Field(None, alias="standard_input")
    standard_output: "Optional[str]" = Field(None, alias="standard_output")
    submit_time: "Optional[str]" = Field(None, alias="submit_time")
    suspend_time: "Optional[str]" = Field(None, alias="suspend_time")
    system_comment: "Optional[str]" = Field(None, alias="system_comment")
    time_limit: "Optional[str]" = Field(None, alias="time_limit")
    time_minimum: "Optional[str]" = Field(None, alias="time_minimum")
    threads_per_core: "Optional[str]" = Field(None, alias="threads_per_core")
    tres_bind: "Optional[str]" = Field(None, alias="tres_bind")
    tres_freq: "Optional[str]" = Field(None, alias="tres_freq")
    tres_per_job: "Optional[str]" = Field(None, alias="tres_per_job")
    tres_per_node: "Optional[str]" = Field(None, alias="tres_per_node")
    tres_per_socket: "Optional[str]" = Field(None, alias="tres_per_socket")
    tres_per_task: "Optional[str]" = Field(None, alias="tres_per_task")
    tres_req_str: "Optional[str]" = Field(None, alias="tres_req_str")
    tres_alloc_str: "Optional[str]" = Field(None, alias="tres_alloc_str")
    user_id: "Optional[str]" = Field(None, alias="user_id")
    user_name: "Optional[str]" = Field(None, alias="user_name")
    wckey: "Optional[str]" = Field(None, alias="wckey")
    current_working_directory: "Optional[str]" = Field(
        None, alias="current_working_directory"
    )


class V0036JobSubmission(BaseModel):
    script: "str" = Field(..., alias="script")
    job: "Optional[V0036JobProperties]" = Field(None, alias="job")
    jobs: "Optional[List[V0036JobProperties]]" = Field(None, alias="jobs")


class V0036JobSubmissionResponse(BaseModel):
    errors: "Optional[List[V0036Error]]" = Field(None, alias="errors")
    job_id: "Optional[int]" = Field(None, alias="job_id")
    step_id: "Optional[str]" = Field(None, alias="step_id")
    job_submit_user_msg: "Optional[str]" = Field(None, alias="job_submit_user_msg")


class V0036JobsResponse(BaseModel):
    errors: "Optional[List[V0036Error]]" = Field(None, alias="errors")
    jobs: "Optional[List[V0036JobResponseProperties]]" = Field(None, alias="jobs")


class V0036Node(BaseModel):
    architecture: "Optional[str]" = Field(None, alias="architecture")
    burstbuffer_network_address: "Optional[str]" = Field(
        None, alias="burstbuffer_network_address"
    )
    boards: "Optional[int]" = Field(None, alias="boards")
    boot_time: "Optional[int]" = Field(None, alias="boot_time")
    comment: "Optional[str]" = Field(None, alias="comment")
    cores: "Optional[int]" = Field(None, alias="cores")
    cpu_binding: "Optional[int]" = Field(None, alias="cpu_binding")
    cpu_load: "Optional[int]" = Field(None, alias="cpu_load")
    free_memory: "Optional[int]" = Field(None, alias="free_memory")
    cpus: "Optional[int]" = Field(None, alias="cpus")
    features: "Optional[str]" = Field(None, alias="features")
    active_features: "Optional[str]" = Field(None, alias="active_features")
    gres: "Optional[str]" = Field(None, alias="gres")
    gres_drained: "Optional[str]" = Field(None, alias="gres_drained")
    gres_used: "Optional[str]" = Field(None, alias="gres_used")
    mcs_label: "Optional[str]" = Field(None, alias="mcs_label")
    name: "Optional[str]" = Field(None, alias="name")
    next_state_after_reboot: "Optional[str]" = Field(
        None, alias="next_state_after_reboot"
    )
    address: "Optional[str]" = Field(None, alias="address")
    hostname: "Optional[str]" = Field(None, alias="hostname")
    state: "Optional[str]" = Field(None, alias="state")
    operating_system: "Optional[str]" = Field(None, alias="operating_system")
    owner: "Optional[str]" = Field(None, alias="owner")
    port: "Optional[int]" = Field(None, alias="port")
    real_memory: "Optional[int]" = Field(None, alias="real_memory")
    reason: "Optional[str]" = Field(None, alias="reason")
    reason_changed_at: "Optional[int]" = Field(None, alias="reason_changed_at")
    reason_set_by_user: "Optional[str]" = Field(None, alias="reason_set_by_user")
    slurmd_start_time: "Optional[int]" = Field(None, alias="slurmd_start_time")
    sockets: "Optional[int]" = Field(None, alias="sockets")
    threads: "Optional[int]" = Field(None, alias="threads")
    temporary_disk: "Optional[int]" = Field(None, alias="temporary_disk")
    weight: "Optional[int]" = Field(None, alias="weight")
    tres: "Optional[str]" = Field(None, alias="tres")
    slurmd_version: "Optional[str]" = Field(None, alias="slurmd_version")


class V0036NodeAllocation(BaseModel):
    memory: "Optional[int]" = Field(None, alias="memory")
    cpus: "Optional[Any]" = Field(None, alias="cpus")
    sockets: "Optional[Any]" = Field(None, alias="sockets")
    cores: "Optional[Any]" = Field(None, alias="cores")


class V0036NodesResponse(BaseModel):
    errors: "Optional[List[V0036Error]]" = Field(None, alias="errors")
    nodes: "Optional[List[V0036Node]]" = Field(None, alias="nodes")


class V0036Partition(BaseModel):
    flags: "Optional[List[str]]" = Field(None, alias="flags")
    preemption_mode: "Optional[str]" = Field(None, alias="preemption_mode")
    allowed_allocation_nodes: "Optional[str]" = Field(
        None, alias="allowed_allocation_nodes"
    )
    allowed_accounts: "Optional[str]" = Field(None, alias="allowed_accounts")
    allowed_groups: "Optional[str]" = Field(None, alias="allowed_groups")
    allowed_qos: "Optional[str]" = Field(None, alias="allowed_qos")
    alternative: "Optional[str]" = Field(None, alias="alternative")
    billing_weights: "Optional[str]" = Field(None, alias="billing_weights")
    default_memory_per_cpu: "Optional[int]" = Field(
        None, alias="default_memory_per_cpu"
    )
    default_time_limit: "Optional[int]" = Field(None, alias="default_time_limit")
    denied_accounts: "Optional[str]" = Field(None, alias="denied_accounts")
    denied_qos: "Optional[str]" = Field(None, alias="denied_qos")
    preemption_grace_time: "Optional[int]" = Field(None, alias="preemption_grace_time")
    maximum_cpus_per_node: "Optional[int]" = Field(None, alias="maximum_cpus_per_node")
    maximum_memory_per_node: "Optional[int]" = Field(
        None, alias="maximum_memory_per_node"
    )
    maximum_nodes_per_job: "Optional[int]" = Field(None, alias="maximum_nodes_per_job")
    max_time_limit: "Optional[int]" = Field(None, alias="max_time_limit")
    min_nodes_per_job: "Optional[int]" = Field(None, alias="min_nodes_per_job")
    name: "Optional[str]" = Field(None, alias="name")
    nodes: "Optional[str]" = Field(None, alias="nodes")
    over_time_limit: "Optional[int]" = Field(None, alias="over_time_limit")
    priority_job_factor: "Optional[int]" = Field(None, alias="priority_job_factor")
    priority_tier: "Optional[int]" = Field(None, alias="priority_tier")
    qos: "Optional[str]" = Field(None, alias="qos")
    nodes_online: "Optional[int]" = Field(None, alias="nodes_online")
    total_cpus: "Optional[int]" = Field(None, alias="total_cpus")
    total_nodes: "Optional[int]" = Field(None, alias="total_nodes")
    tres: "Optional[str]" = Field(None, alias="tres")


class V0036PartitionsResponse(BaseModel):
    errors: "Optional[List[V0036Error]]" = Field(None, alias="errors")
    partitions: "Optional[List[V0036Partition]]" = Field(None, alias="partitions")


class V0036Ping(BaseModel):
    hostname: "Optional[str]" = Field(None, alias="hostname")
    ping: "Literal['UP', 'DOWN']" = Field(None, alias="ping")
    mode: "Optional[str]" = Field(None, alias="mode")
    status: "Optional[int]" = Field(None, alias="status")


class V0036Pings(BaseModel):
    errors: "Optional[List[V0036Error]]" = Field(None, alias="errors")
    pings: "Optional[List[V0036Ping]]" = Field(None, alias="pings")


class V0036Signal(str, Enum):
    HUP = "HUP"
    INT = "INT"
    QUIT = "QUIT"
    ABRT = "ABRT"
    KILL = "KILL"
    ALRM = "ALRM"
    TERM = "TERM"
    USR1 = "USR1"
    USR2 = "USR2"
    URG = "URG"
    CONT = "CONT"
    STOP = "STOP"
    TSTP = "TSTP"
    TTIN = "TTIN"
    TTOU = "TTOU"
