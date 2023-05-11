# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TasksResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'os_type': 'str',
        'state': 'str',
        'estimate_complete_time': 'int',
        'create_date': 'int',
        'priority': 'int',
        'speed_limit': 'int',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'start_target_server': 'bool',
        'error_json': 'str',
        'total_time': 'int',
        'migration_ip': 'str',
        'sub_tasks': 'list[SubTaskAssociatedWithTask]',
        'source_server': 'SourceServerAssociatedWithTask',
        'enterprise_project_id': 'str',
        'target_server': 'TargetServerAssociatedWithTask',
        'log_collect_status': 'str',
        'clone_server': 'CloneServerBrief',
        'syncing': 'bool',
        'network_check_info': 'NetworkCheckInfoRequestBody',
        'special_config': 'list[ConfigBody]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'os_type': 'os_type',
        'state': 'state',
        'estimate_complete_time': 'estimate_complete_time',
        'create_date': 'create_date',
        'priority': 'priority',
        'speed_limit': 'speed_limit',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'start_target_server': 'start_target_server',
        'error_json': 'error_json',
        'total_time': 'total_time',
        'migration_ip': 'migration_ip',
        'sub_tasks': 'sub_tasks',
        'source_server': 'source_server',
        'enterprise_project_id': 'enterprise_project_id',
        'target_server': 'target_server',
        'log_collect_status': 'log_collect_status',
        'clone_server': 'clone_server',
        'syncing': 'syncing',
        'network_check_info': 'network_check_info',
        'special_config': 'special_config'
    }

    def __init__(self, id=None, name=None, type=None, os_type=None, state=None, estimate_complete_time=None, create_date=None, priority=None, speed_limit=None, migrate_speed=None, compress_rate=None, start_target_server=None, error_json=None, total_time=None, migration_ip=None, sub_tasks=None, source_server=None, enterprise_project_id=None, target_server=None, log_collect_status=None, clone_server=None, syncing=None, network_check_info=None, special_config=None):
        """TasksResponseBody

        The model defined in huaweicloud sdk

        :param id: 迁移任务ID
        :type id: str
        :param name: 任务名称（用户自定义）
        :type name: str
        :param type: 任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移
        :type type: str
        :param os_type: 操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选
        :type os_type: str
        :param state: 任务状态
        :type state: str
        :param estimate_complete_time: 预估完成时间
        :type estimate_complete_time: int
        :param create_date: 任务创建时间
        :type create_date: int
        :param priority: 进程优先级 0：低 1：标准 2：高
        :type priority: int
        :param speed_limit: 迁移限速
        :type speed_limit: int
        :param migrate_speed: 迁移速率，单位：MB/S
        :type migrate_speed: float
        :param compress_rate: 压缩率
        :type compress_rate: float
        :param start_target_server: 迁移完成后是否启动目的端服务器 true：启动 false：停止
        :type start_target_server: bool
        :param error_json: 错误信息
        :type error_json: str
        :param total_time: 任务总耗时
        :type total_time: int
        :param migration_ip: 目的端服务器的IP地址。 公网迁移时请填写弹性IP地址 专线迁移时请填写私有IP地址
        :type migration_ip: str
        :param sub_tasks: 任务关联的子任务信息
        :type sub_tasks: list[:class:`huaweicloudsdksms.v3.SubTaskAssociatedWithTask`]
        :param source_server: 
        :type source_server: :class:`huaweicloudsdksms.v3.SourceServerAssociatedWithTask`
        :param enterprise_project_id: 迁移项目ID
        :type enterprise_project_id: str
        :param target_server: 
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServerAssociatedWithTask`
        :param log_collect_status: 日志收集状态 INIT TELL_AGENT_TO_COLLECT WAIT_AGENT_COLLECT_ACK AGENT_COLLECT_FAIL AGENT_COLLECT_SUCCESS WAIT_SERVER_COLLECT SERVER_COLLECT_FAIL SERVER_COLLECT_SUCCESS TELL_AGENT_RESET_ACL WAIT_AGENT_RESET_ACL_ACK
        :type log_collect_status: str
        :param clone_server: 
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServerBrief`
        :param syncing: 是否同步
        :type syncing: bool
        :param network_check_info: 
        :type network_check_info: :class:`huaweicloudsdksms.v3.NetworkCheckInfoRequestBody`
        :param special_config: 特殊配置项配置信息
        :type special_config: list[:class:`huaweicloudsdksms.v3.ConfigBody`]
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._os_type = None
        self._state = None
        self._estimate_complete_time = None
        self._create_date = None
        self._priority = None
        self._speed_limit = None
        self._migrate_speed = None
        self._compress_rate = None
        self._start_target_server = None
        self._error_json = None
        self._total_time = None
        self._migration_ip = None
        self._sub_tasks = None
        self._source_server = None
        self._enterprise_project_id = None
        self._target_server = None
        self._log_collect_status = None
        self._clone_server = None
        self._syncing = None
        self._network_check_info = None
        self._special_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if os_type is not None:
            self.os_type = os_type
        if state is not None:
            self.state = state
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if create_date is not None:
            self.create_date = create_date
        if priority is not None:
            self.priority = priority
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if error_json is not None:
            self.error_json = error_json
        if total_time is not None:
            self.total_time = total_time
        if migration_ip is not None:
            self.migration_ip = migration_ip
        if sub_tasks is not None:
            self.sub_tasks = sub_tasks
        if source_server is not None:
            self.source_server = source_server
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if target_server is not None:
            self.target_server = target_server
        if log_collect_status is not None:
            self.log_collect_status = log_collect_status
        if clone_server is not None:
            self.clone_server = clone_server
        if syncing is not None:
            self.syncing = syncing
        if network_check_info is not None:
            self.network_check_info = network_check_info
        if special_config is not None:
            self.special_config = special_config

    @property
    def id(self):
        """Gets the id of this TasksResponseBody.

        迁移任务ID

        :return: The id of this TasksResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TasksResponseBody.

        迁移任务ID

        :param id: The id of this TasksResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TasksResponseBody.

        任务名称（用户自定义）

        :return: The name of this TasksResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TasksResponseBody.

        任务名称（用户自定义）

        :param name: The name of this TasksResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this TasksResponseBody.

        任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移

        :return: The type of this TasksResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TasksResponseBody.

        任务类型，创建时必选，更新时可选 MIGRATE_FILE:文件级迁移 MIGRATE_BLOCK:块级迁移

        :param type: The type of this TasksResponseBody.
        :type type: str
        """
        self._type = type

    @property
    def os_type(self):
        """Gets the os_type of this TasksResponseBody.

        操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选

        :return: The os_type of this TasksResponseBody.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this TasksResponseBody.

        操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选

        :param os_type: The os_type of this TasksResponseBody.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def state(self):
        """Gets the state of this TasksResponseBody.

        任务状态

        :return: The state of this TasksResponseBody.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TasksResponseBody.

        任务状态

        :param state: The state of this TasksResponseBody.
        :type state: str
        """
        self._state = state

    @property
    def estimate_complete_time(self):
        """Gets the estimate_complete_time of this TasksResponseBody.

        预估完成时间

        :return: The estimate_complete_time of this TasksResponseBody.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        """Sets the estimate_complete_time of this TasksResponseBody.

        预估完成时间

        :param estimate_complete_time: The estimate_complete_time of this TasksResponseBody.
        :type estimate_complete_time: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def create_date(self):
        """Gets the create_date of this TasksResponseBody.

        任务创建时间

        :return: The create_date of this TasksResponseBody.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this TasksResponseBody.

        任务创建时间

        :param create_date: The create_date of this TasksResponseBody.
        :type create_date: int
        """
        self._create_date = create_date

    @property
    def priority(self):
        """Gets the priority of this TasksResponseBody.

        进程优先级 0：低 1：标准 2：高

        :return: The priority of this TasksResponseBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TasksResponseBody.

        进程优先级 0：低 1：标准 2：高

        :param priority: The priority of this TasksResponseBody.
        :type priority: int
        """
        self._priority = priority

    @property
    def speed_limit(self):
        """Gets the speed_limit of this TasksResponseBody.

        迁移限速

        :return: The speed_limit of this TasksResponseBody.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this TasksResponseBody.

        迁移限速

        :param speed_limit: The speed_limit of this TasksResponseBody.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this TasksResponseBody.

        迁移速率，单位：MB/S

        :return: The migrate_speed of this TasksResponseBody.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this TasksResponseBody.

        迁移速率，单位：MB/S

        :param migrate_speed: The migrate_speed of this TasksResponseBody.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        """Gets the compress_rate of this TasksResponseBody.

        压缩率

        :return: The compress_rate of this TasksResponseBody.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        """Sets the compress_rate of this TasksResponseBody.

        压缩率

        :param compress_rate: The compress_rate of this TasksResponseBody.
        :type compress_rate: float
        """
        self._compress_rate = compress_rate

    @property
    def start_target_server(self):
        """Gets the start_target_server of this TasksResponseBody.

        迁移完成后是否启动目的端服务器 true：启动 false：停止

        :return: The start_target_server of this TasksResponseBody.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this TasksResponseBody.

        迁移完成后是否启动目的端服务器 true：启动 false：停止

        :param start_target_server: The start_target_server of this TasksResponseBody.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def error_json(self):
        """Gets the error_json of this TasksResponseBody.

        错误信息

        :return: The error_json of this TasksResponseBody.
        :rtype: str
        """
        return self._error_json

    @error_json.setter
    def error_json(self, error_json):
        """Sets the error_json of this TasksResponseBody.

        错误信息

        :param error_json: The error_json of this TasksResponseBody.
        :type error_json: str
        """
        self._error_json = error_json

    @property
    def total_time(self):
        """Gets the total_time of this TasksResponseBody.

        任务总耗时

        :return: The total_time of this TasksResponseBody.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this TasksResponseBody.

        任务总耗时

        :param total_time: The total_time of this TasksResponseBody.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def migration_ip(self):
        """Gets the migration_ip of this TasksResponseBody.

        目的端服务器的IP地址。 公网迁移时请填写弹性IP地址 专线迁移时请填写私有IP地址

        :return: The migration_ip of this TasksResponseBody.
        :rtype: str
        """
        return self._migration_ip

    @migration_ip.setter
    def migration_ip(self, migration_ip):
        """Sets the migration_ip of this TasksResponseBody.

        目的端服务器的IP地址。 公网迁移时请填写弹性IP地址 专线迁移时请填写私有IP地址

        :param migration_ip: The migration_ip of this TasksResponseBody.
        :type migration_ip: str
        """
        self._migration_ip = migration_ip

    @property
    def sub_tasks(self):
        """Gets the sub_tasks of this TasksResponseBody.

        任务关联的子任务信息

        :return: The sub_tasks of this TasksResponseBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.SubTaskAssociatedWithTask`]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        """Sets the sub_tasks of this TasksResponseBody.

        任务关联的子任务信息

        :param sub_tasks: The sub_tasks of this TasksResponseBody.
        :type sub_tasks: list[:class:`huaweicloudsdksms.v3.SubTaskAssociatedWithTask`]
        """
        self._sub_tasks = sub_tasks

    @property
    def source_server(self):
        """Gets the source_server of this TasksResponseBody.

        :return: The source_server of this TasksResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.SourceServerAssociatedWithTask`
        """
        return self._source_server

    @source_server.setter
    def source_server(self, source_server):
        """Sets the source_server of this TasksResponseBody.

        :param source_server: The source_server of this TasksResponseBody.
        :type source_server: :class:`huaweicloudsdksms.v3.SourceServerAssociatedWithTask`
        """
        self._source_server = source_server

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this TasksResponseBody.

        迁移项目ID

        :return: The enterprise_project_id of this TasksResponseBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this TasksResponseBody.

        迁移项目ID

        :param enterprise_project_id: The enterprise_project_id of this TasksResponseBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def target_server(self):
        """Gets the target_server of this TasksResponseBody.

        :return: The target_server of this TasksResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.TargetServerAssociatedWithTask`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this TasksResponseBody.

        :param target_server: The target_server of this TasksResponseBody.
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServerAssociatedWithTask`
        """
        self._target_server = target_server

    @property
    def log_collect_status(self):
        """Gets the log_collect_status of this TasksResponseBody.

        日志收集状态 INIT TELL_AGENT_TO_COLLECT WAIT_AGENT_COLLECT_ACK AGENT_COLLECT_FAIL AGENT_COLLECT_SUCCESS WAIT_SERVER_COLLECT SERVER_COLLECT_FAIL SERVER_COLLECT_SUCCESS TELL_AGENT_RESET_ACL WAIT_AGENT_RESET_ACL_ACK

        :return: The log_collect_status of this TasksResponseBody.
        :rtype: str
        """
        return self._log_collect_status

    @log_collect_status.setter
    def log_collect_status(self, log_collect_status):
        """Sets the log_collect_status of this TasksResponseBody.

        日志收集状态 INIT TELL_AGENT_TO_COLLECT WAIT_AGENT_COLLECT_ACK AGENT_COLLECT_FAIL AGENT_COLLECT_SUCCESS WAIT_SERVER_COLLECT SERVER_COLLECT_FAIL SERVER_COLLECT_SUCCESS TELL_AGENT_RESET_ACL WAIT_AGENT_RESET_ACL_ACK

        :param log_collect_status: The log_collect_status of this TasksResponseBody.
        :type log_collect_status: str
        """
        self._log_collect_status = log_collect_status

    @property
    def clone_server(self):
        """Gets the clone_server of this TasksResponseBody.

        :return: The clone_server of this TasksResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.CloneServerBrief`
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        """Sets the clone_server of this TasksResponseBody.

        :param clone_server: The clone_server of this TasksResponseBody.
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServerBrief`
        """
        self._clone_server = clone_server

    @property
    def syncing(self):
        """Gets the syncing of this TasksResponseBody.

        是否同步

        :return: The syncing of this TasksResponseBody.
        :rtype: bool
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """Sets the syncing of this TasksResponseBody.

        是否同步

        :param syncing: The syncing of this TasksResponseBody.
        :type syncing: bool
        """
        self._syncing = syncing

    @property
    def network_check_info(self):
        """Gets the network_check_info of this TasksResponseBody.

        :return: The network_check_info of this TasksResponseBody.
        :rtype: :class:`huaweicloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        return self._network_check_info

    @network_check_info.setter
    def network_check_info(self, network_check_info):
        """Sets the network_check_info of this TasksResponseBody.

        :param network_check_info: The network_check_info of this TasksResponseBody.
        :type network_check_info: :class:`huaweicloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        self._network_check_info = network_check_info

    @property
    def special_config(self):
        """Gets the special_config of this TasksResponseBody.

        特殊配置项配置信息

        :return: The special_config of this TasksResponseBody.
        :rtype: list[:class:`huaweicloudsdksms.v3.ConfigBody`]
        """
        return self._special_config

    @special_config.setter
    def special_config(self, special_config):
        """Sets the special_config of this TasksResponseBody.

        特殊配置项配置信息

        :param special_config: The special_config of this TasksResponseBody.
        :type special_config: list[:class:`huaweicloudsdksms.v3.ConfigBody`]
        """
        self._special_config = special_config

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
        if not isinstance(other, TasksResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
