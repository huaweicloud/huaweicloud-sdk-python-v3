# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceMonitoringInfo:

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
        'instance_state': 'InstanceState',
        'type': 'str',
        'cpu': 'str',
        'mem': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'cpu_usage': 'float',
        'memory_usage': 'float',
        'disk_usage': 'float',
        'tps': 'float',
        'qps': 'float',
        'iops': 'float',
        'active_connections': 'int',
        'slow_sql': 'float',
        'readonly_instance_resource_monitoring_info': 'list[ResourceMonitoringInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_state': 'instance_state',
        'type': 'type',
        'cpu': 'cpu',
        'mem': 'mem',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'cpu_usage': 'cpu_usage',
        'memory_usage': 'memory_usage',
        'disk_usage': 'disk_usage',
        'tps': 'tps',
        'qps': 'qps',
        'iops': 'iops',
        'active_connections': 'active_connections',
        'slow_sql': 'slow_sql',
        'readonly_instance_resource_monitoring_info': 'readonly_instance_resource_monitoring_info'
    }

    def __init__(self, id=None, name=None, instance_state=None, type=None, cpu=None, mem=None, engine_name=None, engine_version=None, cpu_usage=None, memory_usage=None, disk_usage=None, tps=None, qps=None, iops=None, active_connections=None, slow_sql=None, readonly_instance_resource_monitoring_info=None):
        """ResourceMonitoringInfo

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 实例名称
        :type name: str
        :param instance_state: 
        :type instance_state: :class:`huaweicloudsdkrds.v3.InstanceState`
        :param type: 实例类型
        :type type: str
        :param cpu: cpu大小
        :type cpu: str
        :param mem: 内存大小（单位：GB）
        :type mem: str
        :param engine_name: 引擎名称
        :type engine_name: str
        :param engine_version: 引擎版本
        :type engine_version: str
        :param cpu_usage: cpu使用率
        :type cpu_usage: float
        :param memory_usage: 内存使用率
        :type memory_usage: float
        :param disk_usage: 磁盘使用率
        :type disk_usage: float
        :param tps: tps
        :type tps: float
        :param qps: qps
        :type qps: float
        :param iops: iops
        :type iops: float
        :param active_connections: 活跃连接数
        :type active_connections: int
        :param slow_sql: 慢SQL
        :type slow_sql: float
        :param readonly_instance_resource_monitoring_info: 只读实例资源监控指标
        :type readonly_instance_resource_monitoring_info: list[:class:`huaweicloudsdkrds.v3.ResourceMonitoringInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._instance_state = None
        self._type = None
        self._cpu = None
        self._mem = None
        self._engine_name = None
        self._engine_version = None
        self._cpu_usage = None
        self._memory_usage = None
        self._disk_usage = None
        self._tps = None
        self._qps = None
        self._iops = None
        self._active_connections = None
        self._slow_sql = None
        self._readonly_instance_resource_monitoring_info = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.instance_state = instance_state
        self.type = type
        self.cpu = cpu
        self.mem = mem
        self.engine_name = engine_name
        self.engine_version = engine_version
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.disk_usage = disk_usage
        self.tps = tps
        if qps is not None:
            self.qps = qps
        self.iops = iops
        self.active_connections = active_connections
        if slow_sql is not None:
            self.slow_sql = slow_sql
        self.readonly_instance_resource_monitoring_info = readonly_instance_resource_monitoring_info

    @property
    def id(self):
        """Gets the id of this ResourceMonitoringInfo.

        实例id

        :return: The id of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceMonitoringInfo.

        实例id

        :param id: The id of this ResourceMonitoringInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceMonitoringInfo.

        实例名称

        :return: The name of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceMonitoringInfo.

        实例名称

        :param name: The name of this ResourceMonitoringInfo.
        :type name: str
        """
        self._name = name

    @property
    def instance_state(self):
        """Gets the instance_state of this ResourceMonitoringInfo.

        :return: The instance_state of this ResourceMonitoringInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.InstanceState`
        """
        return self._instance_state

    @instance_state.setter
    def instance_state(self, instance_state):
        """Sets the instance_state of this ResourceMonitoringInfo.

        :param instance_state: The instance_state of this ResourceMonitoringInfo.
        :type instance_state: :class:`huaweicloudsdkrds.v3.InstanceState`
        """
        self._instance_state = instance_state

    @property
    def type(self):
        """Gets the type of this ResourceMonitoringInfo.

        实例类型

        :return: The type of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceMonitoringInfo.

        实例类型

        :param type: The type of this ResourceMonitoringInfo.
        :type type: str
        """
        self._type = type

    @property
    def cpu(self):
        """Gets the cpu of this ResourceMonitoringInfo.

        cpu大小

        :return: The cpu of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ResourceMonitoringInfo.

        cpu大小

        :param cpu: The cpu of this ResourceMonitoringInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this ResourceMonitoringInfo.

        内存大小（单位：GB）

        :return: The mem of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this ResourceMonitoringInfo.

        内存大小（单位：GB）

        :param mem: The mem of this ResourceMonitoringInfo.
        :type mem: str
        """
        self._mem = mem

    @property
    def engine_name(self):
        """Gets the engine_name of this ResourceMonitoringInfo.

        引擎名称

        :return: The engine_name of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ResourceMonitoringInfo.

        引擎名称

        :param engine_name: The engine_name of this ResourceMonitoringInfo.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        """Gets the engine_version of this ResourceMonitoringInfo.

        引擎版本

        :return: The engine_version of this ResourceMonitoringInfo.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ResourceMonitoringInfo.

        引擎版本

        :param engine_version: The engine_version of this ResourceMonitoringInfo.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def cpu_usage(self):
        """Gets the cpu_usage of this ResourceMonitoringInfo.

        cpu使用率

        :return: The cpu_usage of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """Sets the cpu_usage of this ResourceMonitoringInfo.

        cpu使用率

        :param cpu_usage: The cpu_usage of this ResourceMonitoringInfo.
        :type cpu_usage: float
        """
        self._cpu_usage = cpu_usage

    @property
    def memory_usage(self):
        """Gets the memory_usage of this ResourceMonitoringInfo.

        内存使用率

        :return: The memory_usage of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        """Sets the memory_usage of this ResourceMonitoringInfo.

        内存使用率

        :param memory_usage: The memory_usage of this ResourceMonitoringInfo.
        :type memory_usage: float
        """
        self._memory_usage = memory_usage

    @property
    def disk_usage(self):
        """Gets the disk_usage of this ResourceMonitoringInfo.

        磁盘使用率

        :return: The disk_usage of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        """Sets the disk_usage of this ResourceMonitoringInfo.

        磁盘使用率

        :param disk_usage: The disk_usage of this ResourceMonitoringInfo.
        :type disk_usage: float
        """
        self._disk_usage = disk_usage

    @property
    def tps(self):
        """Gets the tps of this ResourceMonitoringInfo.

        tps

        :return: The tps of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this ResourceMonitoringInfo.

        tps

        :param tps: The tps of this ResourceMonitoringInfo.
        :type tps: float
        """
        self._tps = tps

    @property
    def qps(self):
        """Gets the qps of this ResourceMonitoringInfo.

        qps

        :return: The qps of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """Sets the qps of this ResourceMonitoringInfo.

        qps

        :param qps: The qps of this ResourceMonitoringInfo.
        :type qps: float
        """
        self._qps = qps

    @property
    def iops(self):
        """Gets the iops of this ResourceMonitoringInfo.

        iops

        :return: The iops of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this ResourceMonitoringInfo.

        iops

        :param iops: The iops of this ResourceMonitoringInfo.
        :type iops: float
        """
        self._iops = iops

    @property
    def active_connections(self):
        """Gets the active_connections of this ResourceMonitoringInfo.

        活跃连接数

        :return: The active_connections of this ResourceMonitoringInfo.
        :rtype: int
        """
        return self._active_connections

    @active_connections.setter
    def active_connections(self, active_connections):
        """Sets the active_connections of this ResourceMonitoringInfo.

        活跃连接数

        :param active_connections: The active_connections of this ResourceMonitoringInfo.
        :type active_connections: int
        """
        self._active_connections = active_connections

    @property
    def slow_sql(self):
        """Gets the slow_sql of this ResourceMonitoringInfo.

        慢SQL

        :return: The slow_sql of this ResourceMonitoringInfo.
        :rtype: float
        """
        return self._slow_sql

    @slow_sql.setter
    def slow_sql(self, slow_sql):
        """Sets the slow_sql of this ResourceMonitoringInfo.

        慢SQL

        :param slow_sql: The slow_sql of this ResourceMonitoringInfo.
        :type slow_sql: float
        """
        self._slow_sql = slow_sql

    @property
    def readonly_instance_resource_monitoring_info(self):
        """Gets the readonly_instance_resource_monitoring_info of this ResourceMonitoringInfo.

        只读实例资源监控指标

        :return: The readonly_instance_resource_monitoring_info of this ResourceMonitoringInfo.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ResourceMonitoringInfo`]
        """
        return self._readonly_instance_resource_monitoring_info

    @readonly_instance_resource_monitoring_info.setter
    def readonly_instance_resource_monitoring_info(self, readonly_instance_resource_monitoring_info):
        """Sets the readonly_instance_resource_monitoring_info of this ResourceMonitoringInfo.

        只读实例资源监控指标

        :param readonly_instance_resource_monitoring_info: The readonly_instance_resource_monitoring_info of this ResourceMonitoringInfo.
        :type readonly_instance_resource_monitoring_info: list[:class:`huaweicloudsdkrds.v3.ResourceMonitoringInfo`]
        """
        self._readonly_instance_resource_monitoring_info = readonly_instance_resource_monitoring_info

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
        if not isinstance(other, ResourceMonitoringInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
