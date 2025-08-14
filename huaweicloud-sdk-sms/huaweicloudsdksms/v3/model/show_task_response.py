# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'os_type': 'str',
        'id': 'str',
        'priority': 'int',
        'speed_limit': 'int',
        'region_id': 'str',
        'start_target_server': 'bool',
        'enterprise_project_id': 'str',
        'migration_ip': 'str',
        'region_name': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'vm_template_id': 'str',
        'source_server': 'SourceServerResponse',
        'target_server': 'TaskTargetServer',
        'state': 'str',
        'estimate_complete_time': 'int',
        'connected': 'bool',
        'create_date': 'int',
        'start_date': 'int',
        'finish_date': 'int',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'error_json': 'str',
        'total_time': 'int',
        'float_ip': 'str',
        'remain_seconds': 'int',
        'target_snapshot_id': 'str',
        'clone_server': 'CloneServer',
        'sub_tasks': 'list[SubTask]',
        'network_check_info': 'NetworkCheckInfoRequestBody',
        'total_cpu_usage': 'float',
        'agent_cpu_usage': 'float',
        'total_mem_usage': 'float',
        'agent_mem_usage': 'float',
        'total_disk_io': 'float',
        'agent_disk_io': 'float',
        'need_migration_test': 'bool',
        'subtask_info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'os_type': 'os_type',
        'id': 'id',
        'priority': 'priority',
        'speed_limit': 'speed_limit',
        'region_id': 'region_id',
        'start_target_server': 'start_target_server',
        'enterprise_project_id': 'enterprise_project_id',
        'migration_ip': 'migration_ip',
        'region_name': 'region_name',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'vm_template_id': 'vm_template_id',
        'source_server': 'source_server',
        'target_server': 'target_server',
        'state': 'state',
        'estimate_complete_time': 'estimate_complete_time',
        'connected': 'connected',
        'create_date': 'create_date',
        'start_date': 'start_date',
        'finish_date': 'finish_date',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'error_json': 'error_json',
        'total_time': 'total_time',
        'float_ip': 'float_ip',
        'remain_seconds': 'remain_seconds',
        'target_snapshot_id': 'target_snapshot_id',
        'clone_server': 'clone_server',
        'sub_tasks': 'sub_tasks',
        'network_check_info': 'network_check_info',
        'total_cpu_usage': 'total_cpu_usage',
        'agent_cpu_usage': 'agent_cpu_usage',
        'total_mem_usage': 'total_mem_usage',
        'agent_mem_usage': 'agent_mem_usage',
        'total_disk_io': 'total_disk_io',
        'agent_disk_io': 'agent_disk_io',
        'need_migration_test': 'need_migration_test',
        'subtask_info': 'subtask_info'
    }

    def __init__(self, name=None, type=None, os_type=None, id=None, priority=None, speed_limit=None, region_id=None, start_target_server=None, enterprise_project_id=None, migration_ip=None, region_name=None, project_name=None, project_id=None, vm_template_id=None, source_server=None, target_server=None, state=None, estimate_complete_time=None, connected=None, create_date=None, start_date=None, finish_date=None, migrate_speed=None, compress_rate=None, error_json=None, total_time=None, float_ip=None, remain_seconds=None, target_snapshot_id=None, clone_server=None, sub_tasks=None, network_check_info=None, total_cpu_usage=None, agent_cpu_usage=None, total_mem_usage=None, agent_mem_usage=None, total_disk_io=None, agent_disk_io=None, need_migration_test=None, subtask_info=None):
        r"""ShowTaskResponse

        The model defined in huaweicloud sdk

        :param name: 任务名称（用户自定义）
        :type name: str
        :param type: 任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移
        :type type: str
        :param os_type: 操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选
        :type os_type: str
        :param id: 迁移任务ID
        :type id: str
        :param priority: 进程优先级  0：低  1：标准（默认）  2：高
        :type priority: int
        :param speed_limit: 迁移限速
        :type speed_limit: int
        :param region_id: 目的端服务器的区域ID
        :type region_id: str
        :param start_target_server: 迁移完成后是否启动目的端服务器  true：启动  false：停止
        :type start_target_server: bool
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param migration_ip: 目的端服务器的IP地址。  公网迁移时请填写弹性IP地址  专线迁移时请填写私有IP地址
        :type migration_ip: str
        :param region_name: 目的端服务器的区域名称
        :type region_name: str
        :param project_name: 目的端服务器所在项目名称
        :type project_name: str
        :param project_id: 目的端服务器所在项目ID
        :type project_id: str
        :param vm_template_id: 模板ID
        :type vm_template_id: str
        :param source_server: 
        :type source_server: :class:`huaweicloudsdksms.v3.SourceServerResponse`
        :param target_server: 
        :type target_server: :class:`huaweicloudsdksms.v3.TaskTargetServer`
        :param state: 任务状态
        :type state: str
        :param estimate_complete_time: 预估完成时间
        :type estimate_complete_time: int
        :param connected: 连接状态
        :type connected: bool
        :param create_date: 任务创建时间
        :type create_date: int
        :param start_date: 任务开始时间
        :type start_date: int
        :param finish_date: 任务结束时间
        :type finish_date: int
        :param migrate_speed: 迁移速率，单位：MB/S
        :type migrate_speed: float
        :param compress_rate: 压缩率
        :type compress_rate: float
        :param error_json: 错误信息
        :type error_json: str
        :param total_time: 任务总耗时
        :type total_time: int
        :param float_ip: 暂时保留float,兼容现网老版本的SMS-Agent
        :type float_ip: str
        :param remain_seconds: 迁移剩余时间（秒）
        :type remain_seconds: int
        :param target_snapshot_id: 目的端的快照ID
        :type target_snapshot_id: str
        :param clone_server: 
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        :param sub_tasks: 任务包含的子任务列表
        :type sub_tasks: list[:class:`huaweicloudsdksms.v3.SubTask`]
        :param network_check_info: 
        :type network_check_info: :class:`huaweicloudsdksms.v3.NetworkCheckInfoRequestBody`
        :param total_cpu_usage: 主机的CPU使用率，单位是百分比
        :type total_cpu_usage: float
        :param agent_cpu_usage: Agent的CPU使用率，单位是百分比
        :type agent_cpu_usage: float
        :param total_mem_usage: 主机的内存使用值，单位是MB
        :type total_mem_usage: float
        :param agent_mem_usage: Agent的内存使用值，单位是MB
        :type agent_mem_usage: float
        :param total_disk_io: 主机的磁盘I/O值，单位是MB/s
        :type total_disk_io: float
        :param agent_disk_io: Agent的磁盘I/O值，单位是MB/s
        :type agent_disk_io: float
        :param need_migration_test: 是否开启迁移演练
        :type need_migration_test: bool
        :param subtask_info: 当前子任务及进度
        :type subtask_info: str
        """
        
        super(ShowTaskResponse, self).__init__()

        self._name = None
        self._type = None
        self._os_type = None
        self._id = None
        self._priority = None
        self._speed_limit = None
        self._region_id = None
        self._start_target_server = None
        self._enterprise_project_id = None
        self._migration_ip = None
        self._region_name = None
        self._project_name = None
        self._project_id = None
        self._vm_template_id = None
        self._source_server = None
        self._target_server = None
        self._state = None
        self._estimate_complete_time = None
        self._connected = None
        self._create_date = None
        self._start_date = None
        self._finish_date = None
        self._migrate_speed = None
        self._compress_rate = None
        self._error_json = None
        self._total_time = None
        self._float_ip = None
        self._remain_seconds = None
        self._target_snapshot_id = None
        self._clone_server = None
        self._sub_tasks = None
        self._network_check_info = None
        self._total_cpu_usage = None
        self._agent_cpu_usage = None
        self._total_mem_usage = None
        self._agent_mem_usage = None
        self._total_disk_io = None
        self._agent_disk_io = None
        self._need_migration_test = None
        self._subtask_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if os_type is not None:
            self.os_type = os_type
        if id is not None:
            self.id = id
        if priority is not None:
            self.priority = priority
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if region_id is not None:
            self.region_id = region_id
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if migration_ip is not None:
            self.migration_ip = migration_ip
        if region_name is not None:
            self.region_name = region_name
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if source_server is not None:
            self.source_server = source_server
        if target_server is not None:
            self.target_server = target_server
        if state is not None:
            self.state = state
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if connected is not None:
            self.connected = connected
        if create_date is not None:
            self.create_date = create_date
        if start_date is not None:
            self.start_date = start_date
        if finish_date is not None:
            self.finish_date = finish_date
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
        if error_json is not None:
            self.error_json = error_json
        if total_time is not None:
            self.total_time = total_time
        if float_ip is not None:
            self.float_ip = float_ip
        if remain_seconds is not None:
            self.remain_seconds = remain_seconds
        if target_snapshot_id is not None:
            self.target_snapshot_id = target_snapshot_id
        if clone_server is not None:
            self.clone_server = clone_server
        if sub_tasks is not None:
            self.sub_tasks = sub_tasks
        if network_check_info is not None:
            self.network_check_info = network_check_info
        if total_cpu_usage is not None:
            self.total_cpu_usage = total_cpu_usage
        if agent_cpu_usage is not None:
            self.agent_cpu_usage = agent_cpu_usage
        if total_mem_usage is not None:
            self.total_mem_usage = total_mem_usage
        if agent_mem_usage is not None:
            self.agent_mem_usage = agent_mem_usage
        if total_disk_io is not None:
            self.total_disk_io = total_disk_io
        if agent_disk_io is not None:
            self.agent_disk_io = agent_disk_io
        if need_migration_test is not None:
            self.need_migration_test = need_migration_test
        if subtask_info is not None:
            self.subtask_info = subtask_info

    @property
    def name(self):
        r"""Gets the name of this ShowTaskResponse.

        任务名称（用户自定义）

        :return: The name of this ShowTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowTaskResponse.

        任务名称（用户自定义）

        :param name: The name of this ShowTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowTaskResponse.

        任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移

        :return: The type of this ShowTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowTaskResponse.

        任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移

        :param type: The type of this ShowTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowTaskResponse.

        操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选

        :return: The os_type of this ShowTaskResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowTaskResponse.

        操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选

        :param os_type: The os_type of this ShowTaskResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def id(self):
        r"""Gets the id of this ShowTaskResponse.

        迁移任务ID

        :return: The id of this ShowTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowTaskResponse.

        迁移任务ID

        :param id: The id of this ShowTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def priority(self):
        r"""Gets the priority of this ShowTaskResponse.

        进程优先级  0：低  1：标准（默认）  2：高

        :return: The priority of this ShowTaskResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ShowTaskResponse.

        进程优先级  0：低  1：标准（默认）  2：高

        :param priority: The priority of this ShowTaskResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def speed_limit(self):
        r"""Gets the speed_limit of this ShowTaskResponse.

        迁移限速

        :return: The speed_limit of this ShowTaskResponse.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        r"""Sets the speed_limit of this ShowTaskResponse.

        迁移限速

        :param speed_limit: The speed_limit of this ShowTaskResponse.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowTaskResponse.

        目的端服务器的区域ID

        :return: The region_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowTaskResponse.

        目的端服务器的区域ID

        :param region_id: The region_id of this ShowTaskResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def start_target_server(self):
        r"""Gets the start_target_server of this ShowTaskResponse.

        迁移完成后是否启动目的端服务器  true：启动  false：停止

        :return: The start_target_server of this ShowTaskResponse.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        r"""Sets the start_target_server of this ShowTaskResponse.

        迁移完成后是否启动目的端服务器  true：启动  false：停止

        :param start_target_server: The start_target_server of this ShowTaskResponse.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowTaskResponse.

        企业项目ID

        :return: The enterprise_project_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowTaskResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowTaskResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def migration_ip(self):
        r"""Gets the migration_ip of this ShowTaskResponse.

        目的端服务器的IP地址。  公网迁移时请填写弹性IP地址  专线迁移时请填写私有IP地址

        :return: The migration_ip of this ShowTaskResponse.
        :rtype: str
        """
        return self._migration_ip

    @migration_ip.setter
    def migration_ip(self, migration_ip):
        r"""Sets the migration_ip of this ShowTaskResponse.

        目的端服务器的IP地址。  公网迁移时请填写弹性IP地址  专线迁移时请填写私有IP地址

        :param migration_ip: The migration_ip of this ShowTaskResponse.
        :type migration_ip: str
        """
        self._migration_ip = migration_ip

    @property
    def region_name(self):
        r"""Gets the region_name of this ShowTaskResponse.

        目的端服务器的区域名称

        :return: The region_name of this ShowTaskResponse.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ShowTaskResponse.

        目的端服务器的区域名称

        :param region_name: The region_name of this ShowTaskResponse.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowTaskResponse.

        目的端服务器所在项目名称

        :return: The project_name of this ShowTaskResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowTaskResponse.

        目的端服务器所在项目名称

        :param project_name: The project_name of this ShowTaskResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowTaskResponse.

        目的端服务器所在项目ID

        :return: The project_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowTaskResponse.

        目的端服务器所在项目ID

        :param project_id: The project_id of this ShowTaskResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vm_template_id(self):
        r"""Gets the vm_template_id of this ShowTaskResponse.

        模板ID

        :return: The vm_template_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        r"""Sets the vm_template_id of this ShowTaskResponse.

        模板ID

        :param vm_template_id: The vm_template_id of this ShowTaskResponse.
        :type vm_template_id: str
        """
        self._vm_template_id = vm_template_id

    @property
    def source_server(self):
        r"""Gets the source_server of this ShowTaskResponse.

        :return: The source_server of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdksms.v3.SourceServerResponse`
        """
        return self._source_server

    @source_server.setter
    def source_server(self, source_server):
        r"""Sets the source_server of this ShowTaskResponse.

        :param source_server: The source_server of this ShowTaskResponse.
        :type source_server: :class:`huaweicloudsdksms.v3.SourceServerResponse`
        """
        self._source_server = source_server

    @property
    def target_server(self):
        r"""Gets the target_server of this ShowTaskResponse.

        :return: The target_server of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdksms.v3.TaskTargetServer`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        r"""Sets the target_server of this ShowTaskResponse.

        :param target_server: The target_server of this ShowTaskResponse.
        :type target_server: :class:`huaweicloudsdksms.v3.TaskTargetServer`
        """
        self._target_server = target_server

    @property
    def state(self):
        r"""Gets the state of this ShowTaskResponse.

        任务状态

        :return: The state of this ShowTaskResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowTaskResponse.

        任务状态

        :param state: The state of this ShowTaskResponse.
        :type state: str
        """
        self._state = state

    @property
    def estimate_complete_time(self):
        r"""Gets the estimate_complete_time of this ShowTaskResponse.

        预估完成时间

        :return: The estimate_complete_time of this ShowTaskResponse.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        r"""Sets the estimate_complete_time of this ShowTaskResponse.

        预估完成时间

        :param estimate_complete_time: The estimate_complete_time of this ShowTaskResponse.
        :type estimate_complete_time: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def connected(self):
        r"""Gets the connected of this ShowTaskResponse.

        连接状态

        :return: The connected of this ShowTaskResponse.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        r"""Sets the connected of this ShowTaskResponse.

        连接状态

        :param connected: The connected of this ShowTaskResponse.
        :type connected: bool
        """
        self._connected = connected

    @property
    def create_date(self):
        r"""Gets the create_date of this ShowTaskResponse.

        任务创建时间

        :return: The create_date of this ShowTaskResponse.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        r"""Sets the create_date of this ShowTaskResponse.

        任务创建时间

        :param create_date: The create_date of this ShowTaskResponse.
        :type create_date: int
        """
        self._create_date = create_date

    @property
    def start_date(self):
        r"""Gets the start_date of this ShowTaskResponse.

        任务开始时间

        :return: The start_date of this ShowTaskResponse.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ShowTaskResponse.

        任务开始时间

        :param start_date: The start_date of this ShowTaskResponse.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def finish_date(self):
        r"""Gets the finish_date of this ShowTaskResponse.

        任务结束时间

        :return: The finish_date of this ShowTaskResponse.
        :rtype: int
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        r"""Sets the finish_date of this ShowTaskResponse.

        任务结束时间

        :param finish_date: The finish_date of this ShowTaskResponse.
        :type finish_date: int
        """
        self._finish_date = finish_date

    @property
    def migrate_speed(self):
        r"""Gets the migrate_speed of this ShowTaskResponse.

        迁移速率，单位：MB/S

        :return: The migrate_speed of this ShowTaskResponse.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        r"""Sets the migrate_speed of this ShowTaskResponse.

        迁移速率，单位：MB/S

        :param migrate_speed: The migrate_speed of this ShowTaskResponse.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        r"""Gets the compress_rate of this ShowTaskResponse.

        压缩率

        :return: The compress_rate of this ShowTaskResponse.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        r"""Sets the compress_rate of this ShowTaskResponse.

        压缩率

        :param compress_rate: The compress_rate of this ShowTaskResponse.
        :type compress_rate: float
        """
        self._compress_rate = compress_rate

    @property
    def error_json(self):
        r"""Gets the error_json of this ShowTaskResponse.

        错误信息

        :return: The error_json of this ShowTaskResponse.
        :rtype: str
        """
        return self._error_json

    @error_json.setter
    def error_json(self, error_json):
        r"""Sets the error_json of this ShowTaskResponse.

        错误信息

        :param error_json: The error_json of this ShowTaskResponse.
        :type error_json: str
        """
        self._error_json = error_json

    @property
    def total_time(self):
        r"""Gets the total_time of this ShowTaskResponse.

        任务总耗时

        :return: The total_time of this ShowTaskResponse.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this ShowTaskResponse.

        任务总耗时

        :param total_time: The total_time of this ShowTaskResponse.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def float_ip(self):
        r"""Gets the float_ip of this ShowTaskResponse.

        暂时保留float,兼容现网老版本的SMS-Agent

        :return: The float_ip of this ShowTaskResponse.
        :rtype: str
        """
        return self._float_ip

    @float_ip.setter
    def float_ip(self, float_ip):
        r"""Sets the float_ip of this ShowTaskResponse.

        暂时保留float,兼容现网老版本的SMS-Agent

        :param float_ip: The float_ip of this ShowTaskResponse.
        :type float_ip: str
        """
        self._float_ip = float_ip

    @property
    def remain_seconds(self):
        r"""Gets the remain_seconds of this ShowTaskResponse.

        迁移剩余时间（秒）

        :return: The remain_seconds of this ShowTaskResponse.
        :rtype: int
        """
        return self._remain_seconds

    @remain_seconds.setter
    def remain_seconds(self, remain_seconds):
        r"""Sets the remain_seconds of this ShowTaskResponse.

        迁移剩余时间（秒）

        :param remain_seconds: The remain_seconds of this ShowTaskResponse.
        :type remain_seconds: int
        """
        self._remain_seconds = remain_seconds

    @property
    def target_snapshot_id(self):
        r"""Gets the target_snapshot_id of this ShowTaskResponse.

        目的端的快照ID

        :return: The target_snapshot_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._target_snapshot_id

    @target_snapshot_id.setter
    def target_snapshot_id(self, target_snapshot_id):
        r"""Sets the target_snapshot_id of this ShowTaskResponse.

        目的端的快照ID

        :param target_snapshot_id: The target_snapshot_id of this ShowTaskResponse.
        :type target_snapshot_id: str
        """
        self._target_snapshot_id = target_snapshot_id

    @property
    def clone_server(self):
        r"""Gets the clone_server of this ShowTaskResponse.

        :return: The clone_server of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        r"""Sets the clone_server of this ShowTaskResponse.

        :param clone_server: The clone_server of this ShowTaskResponse.
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        self._clone_server = clone_server

    @property
    def sub_tasks(self):
        r"""Gets the sub_tasks of this ShowTaskResponse.

        任务包含的子任务列表

        :return: The sub_tasks of this ShowTaskResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.SubTask`]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        r"""Sets the sub_tasks of this ShowTaskResponse.

        任务包含的子任务列表

        :param sub_tasks: The sub_tasks of this ShowTaskResponse.
        :type sub_tasks: list[:class:`huaweicloudsdksms.v3.SubTask`]
        """
        self._sub_tasks = sub_tasks

    @property
    def network_check_info(self):
        r"""Gets the network_check_info of this ShowTaskResponse.

        :return: The network_check_info of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        return self._network_check_info

    @network_check_info.setter
    def network_check_info(self, network_check_info):
        r"""Sets the network_check_info of this ShowTaskResponse.

        :param network_check_info: The network_check_info of this ShowTaskResponse.
        :type network_check_info: :class:`huaweicloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        self._network_check_info = network_check_info

    @property
    def total_cpu_usage(self):
        r"""Gets the total_cpu_usage of this ShowTaskResponse.

        主机的CPU使用率，单位是百分比

        :return: The total_cpu_usage of this ShowTaskResponse.
        :rtype: float
        """
        return self._total_cpu_usage

    @total_cpu_usage.setter
    def total_cpu_usage(self, total_cpu_usage):
        r"""Sets the total_cpu_usage of this ShowTaskResponse.

        主机的CPU使用率，单位是百分比

        :param total_cpu_usage: The total_cpu_usage of this ShowTaskResponse.
        :type total_cpu_usage: float
        """
        self._total_cpu_usage = total_cpu_usage

    @property
    def agent_cpu_usage(self):
        r"""Gets the agent_cpu_usage of this ShowTaskResponse.

        Agent的CPU使用率，单位是百分比

        :return: The agent_cpu_usage of this ShowTaskResponse.
        :rtype: float
        """
        return self._agent_cpu_usage

    @agent_cpu_usage.setter
    def agent_cpu_usage(self, agent_cpu_usage):
        r"""Sets the agent_cpu_usage of this ShowTaskResponse.

        Agent的CPU使用率，单位是百分比

        :param agent_cpu_usage: The agent_cpu_usage of this ShowTaskResponse.
        :type agent_cpu_usage: float
        """
        self._agent_cpu_usage = agent_cpu_usage

    @property
    def total_mem_usage(self):
        r"""Gets the total_mem_usage of this ShowTaskResponse.

        主机的内存使用值，单位是MB

        :return: The total_mem_usage of this ShowTaskResponse.
        :rtype: float
        """
        return self._total_mem_usage

    @total_mem_usage.setter
    def total_mem_usage(self, total_mem_usage):
        r"""Sets the total_mem_usage of this ShowTaskResponse.

        主机的内存使用值，单位是MB

        :param total_mem_usage: The total_mem_usage of this ShowTaskResponse.
        :type total_mem_usage: float
        """
        self._total_mem_usage = total_mem_usage

    @property
    def agent_mem_usage(self):
        r"""Gets the agent_mem_usage of this ShowTaskResponse.

        Agent的内存使用值，单位是MB

        :return: The agent_mem_usage of this ShowTaskResponse.
        :rtype: float
        """
        return self._agent_mem_usage

    @agent_mem_usage.setter
    def agent_mem_usage(self, agent_mem_usage):
        r"""Sets the agent_mem_usage of this ShowTaskResponse.

        Agent的内存使用值，单位是MB

        :param agent_mem_usage: The agent_mem_usage of this ShowTaskResponse.
        :type agent_mem_usage: float
        """
        self._agent_mem_usage = agent_mem_usage

    @property
    def total_disk_io(self):
        r"""Gets the total_disk_io of this ShowTaskResponse.

        主机的磁盘I/O值，单位是MB/s

        :return: The total_disk_io of this ShowTaskResponse.
        :rtype: float
        """
        return self._total_disk_io

    @total_disk_io.setter
    def total_disk_io(self, total_disk_io):
        r"""Sets the total_disk_io of this ShowTaskResponse.

        主机的磁盘I/O值，单位是MB/s

        :param total_disk_io: The total_disk_io of this ShowTaskResponse.
        :type total_disk_io: float
        """
        self._total_disk_io = total_disk_io

    @property
    def agent_disk_io(self):
        r"""Gets the agent_disk_io of this ShowTaskResponse.

        Agent的磁盘I/O值，单位是MB/s

        :return: The agent_disk_io of this ShowTaskResponse.
        :rtype: float
        """
        return self._agent_disk_io

    @agent_disk_io.setter
    def agent_disk_io(self, agent_disk_io):
        r"""Sets the agent_disk_io of this ShowTaskResponse.

        Agent的磁盘I/O值，单位是MB/s

        :param agent_disk_io: The agent_disk_io of this ShowTaskResponse.
        :type agent_disk_io: float
        """
        self._agent_disk_io = agent_disk_io

    @property
    def need_migration_test(self):
        r"""Gets the need_migration_test of this ShowTaskResponse.

        是否开启迁移演练

        :return: The need_migration_test of this ShowTaskResponse.
        :rtype: bool
        """
        return self._need_migration_test

    @need_migration_test.setter
    def need_migration_test(self, need_migration_test):
        r"""Sets the need_migration_test of this ShowTaskResponse.

        是否开启迁移演练

        :param need_migration_test: The need_migration_test of this ShowTaskResponse.
        :type need_migration_test: bool
        """
        self._need_migration_test = need_migration_test

    @property
    def subtask_info(self):
        r"""Gets the subtask_info of this ShowTaskResponse.

        当前子任务及进度

        :return: The subtask_info of this ShowTaskResponse.
        :rtype: str
        """
        return self._subtask_info

    @subtask_info.setter
    def subtask_info(self, subtask_info):
        r"""Sets the subtask_info of this ShowTaskResponse.

        当前子任务及进度

        :param subtask_info: The subtask_info of this ShowTaskResponse.
        :type subtask_info: str
        """
        self._subtask_info = subtask_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
