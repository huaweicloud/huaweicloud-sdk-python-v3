# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskByServerSources:


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
        'estimate_complete_time': 'int',
        'start_date': 'int',
        'speed_limit': 'int',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'start_target_server': 'bool',
        'vm_template_id': 'str',
        'region_id': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'target_server': 'TargetServerById',
        'log_collect_status': 'str',
        'exist_server': 'bool',
        'use_public_ip': 'bool',
        'clone_server': 'CloneServer',
        'remain_seconds': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'state': 'state',
        'estimate_complete_time': 'estimate_complete_time',
        'start_date': 'start_date',
        'speed_limit': 'speed_limit',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'start_target_server': 'start_target_server',
        'vm_template_id': 'vm_template_id',
        'region_id': 'region_id',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'target_server': 'target_server',
        'log_collect_status': 'log_collect_status',
        'exist_server': 'exist_server',
        'use_public_ip': 'use_public_ip',
        'clone_server': 'clone_server',
        'remain_seconds': 'remain_seconds'
    }

    def __init__(self, id=None, name=None, type=None, state=None, estimate_complete_time=None, start_date=None, speed_limit=None, migrate_speed=None, compress_rate=None, start_target_server=None, vm_template_id=None, region_id=None, project_name=None, project_id=None, target_server=None, log_collect_status=None, exist_server=None, use_public_ip=None, clone_server=None, remain_seconds=None):
        """TaskByServerSources - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._type = None
        self._state = None
        self._estimate_complete_time = None
        self._start_date = None
        self._speed_limit = None
        self._migrate_speed = None
        self._compress_rate = None
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
        self._remain_seconds = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if start_date is not None:
            self.start_date = start_date
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
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
        if remain_seconds is not None:
            self.remain_seconds = remain_seconds

    @property
    def id(self):
        """Gets the id of this TaskByServerSources.

        任务id

        :return: The id of this TaskByServerSources.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskByServerSources.

        任务id

        :param id: The id of this TaskByServerSources.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskByServerSources.

        任务名称

        :return: The name of this TaskByServerSources.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskByServerSources.

        任务名称

        :param name: The name of this TaskByServerSources.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this TaskByServerSources.

        任务类型

        :return: The type of this TaskByServerSources.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskByServerSources.

        任务类型

        :param type: The type of this TaskByServerSources.
        :type: str
        """
        self._type = type

    @property
    def state(self):
        """Gets the state of this TaskByServerSources.

        任务状态

        :return: The state of this TaskByServerSources.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskByServerSources.

        任务状态

        :param state: The state of this TaskByServerSources.
        :type: str
        """
        self._state = state

    @property
    def estimate_complete_time(self):
        """Gets the estimate_complete_time of this TaskByServerSources.

        预估结束时间

        :return: The estimate_complete_time of this TaskByServerSources.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        """Sets the estimate_complete_time of this TaskByServerSources.

        预估结束时间

        :param estimate_complete_time: The estimate_complete_time of this TaskByServerSources.
        :type: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def start_date(self):
        """Gets the start_date of this TaskByServerSources.

        开始时间

        :return: The start_date of this TaskByServerSources.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TaskByServerSources.

        开始时间

        :param start_date: The start_date of this TaskByServerSources.
        :type: int
        """
        self._start_date = start_date

    @property
    def speed_limit(self):
        """Gets the speed_limit of this TaskByServerSources.

        限速

        :return: The speed_limit of this TaskByServerSources.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this TaskByServerSources.

        限速

        :param speed_limit: The speed_limit of this TaskByServerSources.
        :type: int
        """
        self._speed_limit = speed_limit

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this TaskByServerSources.

        迁移速率

        :return: The migrate_speed of this TaskByServerSources.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this TaskByServerSources.

        迁移速率

        :param migrate_speed: The migrate_speed of this TaskByServerSources.
        :type: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        """Gets the compress_rate of this TaskByServerSources.

        压缩率

        :return: The compress_rate of this TaskByServerSources.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        """Sets the compress_rate of this TaskByServerSources.

        压缩率

        :param compress_rate: The compress_rate of this TaskByServerSources.
        :type: float
        """
        self._compress_rate = compress_rate

    @property
    def start_target_server(self):
        """Gets the start_target_server of this TaskByServerSources.

        是否启动虚拟机

        :return: The start_target_server of this TaskByServerSources.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this TaskByServerSources.

        是否启动虚拟机

        :param start_target_server: The start_target_server of this TaskByServerSources.
        :type: bool
        """
        self._start_target_server = start_target_server

    @property
    def vm_template_id(self):
        """Gets the vm_template_id of this TaskByServerSources.

        虚拟机模板id

        :return: The vm_template_id of this TaskByServerSources.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        """Sets the vm_template_id of this TaskByServerSources.

        虚拟机模板id

        :param vm_template_id: The vm_template_id of this TaskByServerSources.
        :type: str
        """
        self._vm_template_id = vm_template_id

    @property
    def region_id(self):
        """Gets the region_id of this TaskByServerSources.

        region_id

        :return: The region_id of this TaskByServerSources.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this TaskByServerSources.

        region_id

        :param region_id: The region_id of this TaskByServerSources.
        :type: str
        """
        self._region_id = region_id

    @property
    def project_name(self):
        """Gets the project_name of this TaskByServerSources.

        项目名称

        :return: The project_name of this TaskByServerSources.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TaskByServerSources.

        项目名称

        :param project_name: The project_name of this TaskByServerSources.
        :type: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this TaskByServerSources.

        项目id

        :return: The project_id of this TaskByServerSources.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TaskByServerSources.

        项目id

        :param project_id: The project_id of this TaskByServerSources.
        :type: str
        """
        self._project_id = project_id

    @property
    def target_server(self):
        """Gets the target_server of this TaskByServerSources.


        :return: The target_server of this TaskByServerSources.
        :rtype: TargetServerById
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this TaskByServerSources.


        :param target_server: The target_server of this TaskByServerSources.
        :type: TargetServerById
        """
        self._target_server = target_server

    @property
    def log_collect_status(self):
        """Gets the log_collect_status of this TaskByServerSources.

        日志收集状态

        :return: The log_collect_status of this TaskByServerSources.
        :rtype: str
        """
        return self._log_collect_status

    @log_collect_status.setter
    def log_collect_status(self, log_collect_status):
        """Sets the log_collect_status of this TaskByServerSources.

        日志收集状态

        :param log_collect_status: The log_collect_status of this TaskByServerSources.
        :type: str
        """
        self._log_collect_status = log_collect_status

    @property
    def exist_server(self):
        """Gets the exist_server of this TaskByServerSources.

        是否使用已有虚拟机

        :return: The exist_server of this TaskByServerSources.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        """Sets the exist_server of this TaskByServerSources.

        是否使用已有虚拟机

        :param exist_server: The exist_server of this TaskByServerSources.
        :type: bool
        """
        self._exist_server = exist_server

    @property
    def use_public_ip(self):
        """Gets the use_public_ip of this TaskByServerSources.

        是否使用公网ip

        :return: The use_public_ip of this TaskByServerSources.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        """Sets the use_public_ip of this TaskByServerSources.

        是否使用公网ip

        :param use_public_ip: The use_public_ip of this TaskByServerSources.
        :type: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def clone_server(self):
        """Gets the clone_server of this TaskByServerSources.


        :return: The clone_server of this TaskByServerSources.
        :rtype: CloneServer
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        """Sets the clone_server of this TaskByServerSources.


        :param clone_server: The clone_server of this TaskByServerSources.
        :type: CloneServer
        """
        self._clone_server = clone_server

    @property
    def remain_seconds(self):
        """Gets the remain_seconds of this TaskByServerSources.

        已迁移时长

        :return: The remain_seconds of this TaskByServerSources.
        :rtype: int
        """
        return self._remain_seconds

    @remain_seconds.setter
    def remain_seconds(self, remain_seconds):
        """Sets the remain_seconds of this TaskByServerSources.

        已迁移时长

        :param remain_seconds: The remain_seconds of this TaskByServerSources.
        :type: int
        """
        self._remain_seconds = remain_seconds

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
        if not isinstance(other, TaskByServerSources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
