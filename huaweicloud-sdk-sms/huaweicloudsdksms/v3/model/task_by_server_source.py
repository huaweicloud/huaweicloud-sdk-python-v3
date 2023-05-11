# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskByServerSource:

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
        'state': 'str',
        'start_date': 'int',
        'speed_limit': 'int',
        'migrate_speed': 'float',
        'start_target_server': 'bool',
        'vm_template_id': 'str',
        'region_id': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'target_server': 'TargetServerById',
        'log_collect_status': 'str',
        'exist_server': 'bool',
        'use_public_ip': 'bool',
        'clone_server': 'CloneServer'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'state': 'state',
        'start_date': 'start_date',
        'speed_limit': 'speed_limit',
        'migrate_speed': 'migrate_speed',
        'start_target_server': 'start_target_server',
        'vm_template_id': 'vm_template_id',
        'region_id': 'region_id',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'target_server': 'target_server',
        'log_collect_status': 'log_collect_status',
        'exist_server': 'exist_server',
        'use_public_ip': 'use_public_ip',
        'clone_server': 'clone_server'
    }

    def __init__(self, id=None, name=None, type=None, state=None, start_date=None, speed_limit=None, migrate_speed=None, start_target_server=None, vm_template_id=None, region_id=None, project_name=None, project_id=None, target_server=None, log_collect_status=None, exist_server=None, use_public_ip=None, clone_server=None):
        """TaskByServerSource

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param name: 任务名称
        :type name: str
        :param type: 任务类型
        :type type: str
        :param state: 任务状态
        :type state: str
        :param start_date: 开始时间
        :type start_date: int
        :param speed_limit: 限速
        :type speed_limit: int
        :param migrate_speed: 迁移速率
        :type migrate_speed: float
        :param start_target_server: 是否启动虚拟机
        :type start_target_server: bool
        :param vm_template_id: 虚拟机模板ID
        :type vm_template_id: str
        :param region_id: region_id
        :type region_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param target_server: 
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServerById`
        :param log_collect_status: 日志收集状态
        :type log_collect_status: str
        :param exist_server: 是否使用已有虚拟机
        :type exist_server: bool
        :param use_public_ip: 是否使用公网IP
        :type use_public_ip: bool
        :param clone_server: 
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._state = None
        self._start_date = None
        self._speed_limit = None
        self._migrate_speed = None
        self._start_target_server = None
        self._vm_template_id = None
        self._region_id = None
        self._project_name = None
        self._project_id = None
        self._target_server = None
        self._log_collect_status = None
        self._exist_server = None
        self._use_public_ip = None
        self._clone_server = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if start_date is not None:
            self.start_date = start_date
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if region_id is not None:
            self.region_id = region_id
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if target_server is not None:
            self.target_server = target_server
        if log_collect_status is not None:
            self.log_collect_status = log_collect_status
        if exist_server is not None:
            self.exist_server = exist_server
        if use_public_ip is not None:
            self.use_public_ip = use_public_ip
        if clone_server is not None:
            self.clone_server = clone_server

    @property
    def id(self):
        """Gets the id of this TaskByServerSource.

        任务ID

        :return: The id of this TaskByServerSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskByServerSource.

        任务ID

        :param id: The id of this TaskByServerSource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskByServerSource.

        任务名称

        :return: The name of this TaskByServerSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskByServerSource.

        任务名称

        :param name: The name of this TaskByServerSource.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this TaskByServerSource.

        任务类型

        :return: The type of this TaskByServerSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskByServerSource.

        任务类型

        :param type: The type of this TaskByServerSource.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        """Gets the state of this TaskByServerSource.

        任务状态

        :return: The state of this TaskByServerSource.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskByServerSource.

        任务状态

        :param state: The state of this TaskByServerSource.
        :type state: str
        """
        self._state = state

    @property
    def start_date(self):
        """Gets the start_date of this TaskByServerSource.

        开始时间

        :return: The start_date of this TaskByServerSource.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TaskByServerSource.

        开始时间

        :param start_date: The start_date of this TaskByServerSource.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def speed_limit(self):
        """Gets the speed_limit of this TaskByServerSource.

        限速

        :return: The speed_limit of this TaskByServerSource.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this TaskByServerSource.

        限速

        :param speed_limit: The speed_limit of this TaskByServerSource.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this TaskByServerSource.

        迁移速率

        :return: The migrate_speed of this TaskByServerSource.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this TaskByServerSource.

        迁移速率

        :param migrate_speed: The migrate_speed of this TaskByServerSource.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def start_target_server(self):
        """Gets the start_target_server of this TaskByServerSource.

        是否启动虚拟机

        :return: The start_target_server of this TaskByServerSource.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this TaskByServerSource.

        是否启动虚拟机

        :param start_target_server: The start_target_server of this TaskByServerSource.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def vm_template_id(self):
        """Gets the vm_template_id of this TaskByServerSource.

        虚拟机模板ID

        :return: The vm_template_id of this TaskByServerSource.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        """Sets the vm_template_id of this TaskByServerSource.

        虚拟机模板ID

        :param vm_template_id: The vm_template_id of this TaskByServerSource.
        :type vm_template_id: str
        """
        self._vm_template_id = vm_template_id

    @property
    def region_id(self):
        """Gets the region_id of this TaskByServerSource.

        region_id

        :return: The region_id of this TaskByServerSource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this TaskByServerSource.

        region_id

        :param region_id: The region_id of this TaskByServerSource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_name(self):
        """Gets the project_name of this TaskByServerSource.

        项目名称

        :return: The project_name of this TaskByServerSource.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TaskByServerSource.

        项目名称

        :param project_name: The project_name of this TaskByServerSource.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this TaskByServerSource.

        项目ID

        :return: The project_id of this TaskByServerSource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TaskByServerSource.

        项目ID

        :param project_id: The project_id of this TaskByServerSource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def target_server(self):
        """Gets the target_server of this TaskByServerSource.

        :return: The target_server of this TaskByServerSource.
        :rtype: :class:`huaweicloudsdksms.v3.TargetServerById`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this TaskByServerSource.

        :param target_server: The target_server of this TaskByServerSource.
        :type target_server: :class:`huaweicloudsdksms.v3.TargetServerById`
        """
        self._target_server = target_server

    @property
    def log_collect_status(self):
        """Gets the log_collect_status of this TaskByServerSource.

        日志收集状态

        :return: The log_collect_status of this TaskByServerSource.
        :rtype: str
        """
        return self._log_collect_status

    @log_collect_status.setter
    def log_collect_status(self, log_collect_status):
        """Sets the log_collect_status of this TaskByServerSource.

        日志收集状态

        :param log_collect_status: The log_collect_status of this TaskByServerSource.
        :type log_collect_status: str
        """
        self._log_collect_status = log_collect_status

    @property
    def exist_server(self):
        """Gets the exist_server of this TaskByServerSource.

        是否使用已有虚拟机

        :return: The exist_server of this TaskByServerSource.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        """Sets the exist_server of this TaskByServerSource.

        是否使用已有虚拟机

        :param exist_server: The exist_server of this TaskByServerSource.
        :type exist_server: bool
        """
        self._exist_server = exist_server

    @property
    def use_public_ip(self):
        """Gets the use_public_ip of this TaskByServerSource.

        是否使用公网IP

        :return: The use_public_ip of this TaskByServerSource.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        """Sets the use_public_ip of this TaskByServerSource.

        是否使用公网IP

        :param use_public_ip: The use_public_ip of this TaskByServerSource.
        :type use_public_ip: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def clone_server(self):
        """Gets the clone_server of this TaskByServerSource.

        :return: The clone_server of this TaskByServerSource.
        :rtype: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        """Sets the clone_server of this TaskByServerSource.

        :param clone_server: The clone_server of this TaskByServerSource.
        :type clone_server: :class:`huaweicloudsdksms.v3.CloneServer`
        """
        self._clone_server = clone_server

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
        if not isinstance(other, TaskByServerSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
