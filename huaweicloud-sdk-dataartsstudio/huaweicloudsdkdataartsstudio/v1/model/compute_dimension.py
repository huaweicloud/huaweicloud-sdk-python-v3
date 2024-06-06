# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeDimension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_instance_id': 'str',
        'name': 'str',
        'type': 'int',
        'node_type': 'str',
        'job_id': 'int',
        'job_instance_id': 'int',
        'job_name': 'str',
        'start_time_ms': 'int',
        'end_time_ms': 'int',
        'execute_time_ms': 'int',
        'status': 'str',
        'last_start_time_ms': 'int',
        'last_end_time_ms': 'int',
        'cpu_resource_consumption_value': 'int',
        'cpu_unit': 'str',
        'memory_resource_consumption_value': 'int',
        'memory_unit': 'str',
        'last_cpu_resource_consumption_value': 'int',
        'last_cpu_unit': 'str',
        'last_memory_resource_consumption_value': 'int',
        'last_memory_unit': 'str',
        'creator': 'str',
        'warehouse_time_ms': 'int',
        'extended_fields': 'str'
    }

    attribute_map = {
        'node_instance_id': 'node_instance_id',
        'name': 'name',
        'type': 'type',
        'node_type': 'node_type',
        'job_id': 'job_id',
        'job_instance_id': 'job_instance_id',
        'job_name': 'job_name',
        'start_time_ms': 'start_time_ms',
        'end_time_ms': 'end_time_ms',
        'execute_time_ms': 'execute_time_ms',
        'status': 'status',
        'last_start_time_ms': 'last_start_time_ms',
        'last_end_time_ms': 'last_end_time_ms',
        'cpu_resource_consumption_value': 'cpu_resource_consumption_value',
        'cpu_unit': 'cpu_unit',
        'memory_resource_consumption_value': 'memory_resource_consumption_value',
        'memory_unit': 'memory_unit',
        'last_cpu_resource_consumption_value': 'last_cpu_resource_consumption_value',
        'last_cpu_unit': 'last_cpu_unit',
        'last_memory_resource_consumption_value': 'last_memory_resource_consumption_value',
        'last_memory_unit': 'last_memory_unit',
        'creator': 'creator',
        'warehouse_time_ms': 'warehouse_time_ms',
        'extended_fields': 'extended_fields'
    }

    def __init__(self, node_instance_id=None, name=None, type=None, node_type=None, job_id=None, job_instance_id=None, job_name=None, start_time_ms=None, end_time_ms=None, execute_time_ms=None, status=None, last_start_time_ms=None, last_end_time_ms=None, cpu_resource_consumption_value=None, cpu_unit=None, memory_resource_consumption_value=None, memory_unit=None, last_cpu_resource_consumption_value=None, last_cpu_unit=None, last_memory_resource_consumption_value=None, last_memory_unit=None, creator=None, warehouse_time_ms=None, extended_fields=None):
        """ComputeDimension

        The model defined in huaweicloud sdk

        :param node_instance_id: 节点实例ID
        :type node_instance_id: str
        :param name: 节点名称或脚本名称
        :type name: str
        :param type: 类型,用于区分节点实例和脚本
        :type type: int
        :param node_type: 节点类型
        :type node_type: str
        :param job_id: 作业id
        :type job_id: int
        :param job_instance_id: 作业实例id
        :type job_instance_id: int
        :param job_name: 作业名称
        :type job_name: str
        :param start_time_ms: 节点实例启动时间,单位毫秒
        :type start_time_ms: int
        :param end_time_ms: 节点实例结束时间,单位毫秒
        :type end_time_ms: int
        :param execute_time_ms: 节点实例执行时长,单位毫秒
        :type execute_time_ms: int
        :param status: 节点实例状态
        :type status: str
        :param last_start_time_ms: 节点实例上次执行开始时间,单位毫秒
        :type last_start_time_ms: int
        :param last_end_time_ms: 节点实例上次执行结束时间,单位毫秒
        :type last_end_time_ms: int
        :param cpu_resource_consumption_value: cpu消耗值
        :type cpu_resource_consumption_value: int
        :param cpu_unit: cpu消耗单位
        :type cpu_unit: str
        :param memory_resource_consumption_value: 内存消耗值
        :type memory_resource_consumption_value: int
        :param memory_unit: 内存消耗单位
        :type memory_unit: str
        :param last_cpu_resource_consumption_value: 上次cpu消耗值
        :type last_cpu_resource_consumption_value: int
        :param last_cpu_unit: 上次cpu消耗单位
        :type last_cpu_unit: str
        :param last_memory_resource_consumption_value: 上次内存消耗值
        :type last_memory_resource_consumption_value: int
        :param last_memory_unit: 上次内存消耗单位
        :type last_memory_unit: str
        :param creator: 节点实例创建者name
        :type creator: str
        :param warehouse_time_ms: 数据入库时间,单位毫秒
        :type warehouse_time_ms: int
        :param extended_fields: 扩展字段
        :type extended_fields: str
        """
        
        

        self._node_instance_id = None
        self._name = None
        self._type = None
        self._node_type = None
        self._job_id = None
        self._job_instance_id = None
        self._job_name = None
        self._start_time_ms = None
        self._end_time_ms = None
        self._execute_time_ms = None
        self._status = None
        self._last_start_time_ms = None
        self._last_end_time_ms = None
        self._cpu_resource_consumption_value = None
        self._cpu_unit = None
        self._memory_resource_consumption_value = None
        self._memory_unit = None
        self._last_cpu_resource_consumption_value = None
        self._last_cpu_unit = None
        self._last_memory_resource_consumption_value = None
        self._last_memory_unit = None
        self._creator = None
        self._warehouse_time_ms = None
        self._extended_fields = None
        self.discriminator = None

        if node_instance_id is not None:
            self.node_instance_id = node_instance_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if node_type is not None:
            self.node_type = node_type
        if job_id is not None:
            self.job_id = job_id
        if job_instance_id is not None:
            self.job_instance_id = job_instance_id
        if job_name is not None:
            self.job_name = job_name
        if start_time_ms is not None:
            self.start_time_ms = start_time_ms
        if end_time_ms is not None:
            self.end_time_ms = end_time_ms
        if execute_time_ms is not None:
            self.execute_time_ms = execute_time_ms
        if status is not None:
            self.status = status
        if last_start_time_ms is not None:
            self.last_start_time_ms = last_start_time_ms
        if last_end_time_ms is not None:
            self.last_end_time_ms = last_end_time_ms
        if cpu_resource_consumption_value is not None:
            self.cpu_resource_consumption_value = cpu_resource_consumption_value
        if cpu_unit is not None:
            self.cpu_unit = cpu_unit
        if memory_resource_consumption_value is not None:
            self.memory_resource_consumption_value = memory_resource_consumption_value
        if memory_unit is not None:
            self.memory_unit = memory_unit
        if last_cpu_resource_consumption_value is not None:
            self.last_cpu_resource_consumption_value = last_cpu_resource_consumption_value
        if last_cpu_unit is not None:
            self.last_cpu_unit = last_cpu_unit
        if last_memory_resource_consumption_value is not None:
            self.last_memory_resource_consumption_value = last_memory_resource_consumption_value
        if last_memory_unit is not None:
            self.last_memory_unit = last_memory_unit
        if creator is not None:
            self.creator = creator
        if warehouse_time_ms is not None:
            self.warehouse_time_ms = warehouse_time_ms
        if extended_fields is not None:
            self.extended_fields = extended_fields

    @property
    def node_instance_id(self):
        """Gets the node_instance_id of this ComputeDimension.

        节点实例ID

        :return: The node_instance_id of this ComputeDimension.
        :rtype: str
        """
        return self._node_instance_id

    @node_instance_id.setter
    def node_instance_id(self, node_instance_id):
        """Sets the node_instance_id of this ComputeDimension.

        节点实例ID

        :param node_instance_id: The node_instance_id of this ComputeDimension.
        :type node_instance_id: str
        """
        self._node_instance_id = node_instance_id

    @property
    def name(self):
        """Gets the name of this ComputeDimension.

        节点名称或脚本名称

        :return: The name of this ComputeDimension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputeDimension.

        节点名称或脚本名称

        :param name: The name of this ComputeDimension.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ComputeDimension.

        类型,用于区分节点实例和脚本

        :return: The type of this ComputeDimension.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComputeDimension.

        类型,用于区分节点实例和脚本

        :param type: The type of this ComputeDimension.
        :type type: int
        """
        self._type = type

    @property
    def node_type(self):
        """Gets the node_type of this ComputeDimension.

        节点类型

        :return: The node_type of this ComputeDimension.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ComputeDimension.

        节点类型

        :param node_type: The node_type of this ComputeDimension.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def job_id(self):
        """Gets the job_id of this ComputeDimension.

        作业id

        :return: The job_id of this ComputeDimension.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ComputeDimension.

        作业id

        :param job_id: The job_id of this ComputeDimension.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def job_instance_id(self):
        """Gets the job_instance_id of this ComputeDimension.

        作业实例id

        :return: The job_instance_id of this ComputeDimension.
        :rtype: int
        """
        return self._job_instance_id

    @job_instance_id.setter
    def job_instance_id(self, job_instance_id):
        """Sets the job_instance_id of this ComputeDimension.

        作业实例id

        :param job_instance_id: The job_instance_id of this ComputeDimension.
        :type job_instance_id: int
        """
        self._job_instance_id = job_instance_id

    @property
    def job_name(self):
        """Gets the job_name of this ComputeDimension.

        作业名称

        :return: The job_name of this ComputeDimension.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ComputeDimension.

        作业名称

        :param job_name: The job_name of this ComputeDimension.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def start_time_ms(self):
        """Gets the start_time_ms of this ComputeDimension.

        节点实例启动时间,单位毫秒

        :return: The start_time_ms of this ComputeDimension.
        :rtype: int
        """
        return self._start_time_ms

    @start_time_ms.setter
    def start_time_ms(self, start_time_ms):
        """Sets the start_time_ms of this ComputeDimension.

        节点实例启动时间,单位毫秒

        :param start_time_ms: The start_time_ms of this ComputeDimension.
        :type start_time_ms: int
        """
        self._start_time_ms = start_time_ms

    @property
    def end_time_ms(self):
        """Gets the end_time_ms of this ComputeDimension.

        节点实例结束时间,单位毫秒

        :return: The end_time_ms of this ComputeDimension.
        :rtype: int
        """
        return self._end_time_ms

    @end_time_ms.setter
    def end_time_ms(self, end_time_ms):
        """Sets the end_time_ms of this ComputeDimension.

        节点实例结束时间,单位毫秒

        :param end_time_ms: The end_time_ms of this ComputeDimension.
        :type end_time_ms: int
        """
        self._end_time_ms = end_time_ms

    @property
    def execute_time_ms(self):
        """Gets the execute_time_ms of this ComputeDimension.

        节点实例执行时长,单位毫秒

        :return: The execute_time_ms of this ComputeDimension.
        :rtype: int
        """
        return self._execute_time_ms

    @execute_time_ms.setter
    def execute_time_ms(self, execute_time_ms):
        """Sets the execute_time_ms of this ComputeDimension.

        节点实例执行时长,单位毫秒

        :param execute_time_ms: The execute_time_ms of this ComputeDimension.
        :type execute_time_ms: int
        """
        self._execute_time_ms = execute_time_ms

    @property
    def status(self):
        """Gets the status of this ComputeDimension.

        节点实例状态

        :return: The status of this ComputeDimension.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComputeDimension.

        节点实例状态

        :param status: The status of this ComputeDimension.
        :type status: str
        """
        self._status = status

    @property
    def last_start_time_ms(self):
        """Gets the last_start_time_ms of this ComputeDimension.

        节点实例上次执行开始时间,单位毫秒

        :return: The last_start_time_ms of this ComputeDimension.
        :rtype: int
        """
        return self._last_start_time_ms

    @last_start_time_ms.setter
    def last_start_time_ms(self, last_start_time_ms):
        """Sets the last_start_time_ms of this ComputeDimension.

        节点实例上次执行开始时间,单位毫秒

        :param last_start_time_ms: The last_start_time_ms of this ComputeDimension.
        :type last_start_time_ms: int
        """
        self._last_start_time_ms = last_start_time_ms

    @property
    def last_end_time_ms(self):
        """Gets the last_end_time_ms of this ComputeDimension.

        节点实例上次执行结束时间,单位毫秒

        :return: The last_end_time_ms of this ComputeDimension.
        :rtype: int
        """
        return self._last_end_time_ms

    @last_end_time_ms.setter
    def last_end_time_ms(self, last_end_time_ms):
        """Sets the last_end_time_ms of this ComputeDimension.

        节点实例上次执行结束时间,单位毫秒

        :param last_end_time_ms: The last_end_time_ms of this ComputeDimension.
        :type last_end_time_ms: int
        """
        self._last_end_time_ms = last_end_time_ms

    @property
    def cpu_resource_consumption_value(self):
        """Gets the cpu_resource_consumption_value of this ComputeDimension.

        cpu消耗值

        :return: The cpu_resource_consumption_value of this ComputeDimension.
        :rtype: int
        """
        return self._cpu_resource_consumption_value

    @cpu_resource_consumption_value.setter
    def cpu_resource_consumption_value(self, cpu_resource_consumption_value):
        """Sets the cpu_resource_consumption_value of this ComputeDimension.

        cpu消耗值

        :param cpu_resource_consumption_value: The cpu_resource_consumption_value of this ComputeDimension.
        :type cpu_resource_consumption_value: int
        """
        self._cpu_resource_consumption_value = cpu_resource_consumption_value

    @property
    def cpu_unit(self):
        """Gets the cpu_unit of this ComputeDimension.

        cpu消耗单位

        :return: The cpu_unit of this ComputeDimension.
        :rtype: str
        """
        return self._cpu_unit

    @cpu_unit.setter
    def cpu_unit(self, cpu_unit):
        """Sets the cpu_unit of this ComputeDimension.

        cpu消耗单位

        :param cpu_unit: The cpu_unit of this ComputeDimension.
        :type cpu_unit: str
        """
        self._cpu_unit = cpu_unit

    @property
    def memory_resource_consumption_value(self):
        """Gets the memory_resource_consumption_value of this ComputeDimension.

        内存消耗值

        :return: The memory_resource_consumption_value of this ComputeDimension.
        :rtype: int
        """
        return self._memory_resource_consumption_value

    @memory_resource_consumption_value.setter
    def memory_resource_consumption_value(self, memory_resource_consumption_value):
        """Sets the memory_resource_consumption_value of this ComputeDimension.

        内存消耗值

        :param memory_resource_consumption_value: The memory_resource_consumption_value of this ComputeDimension.
        :type memory_resource_consumption_value: int
        """
        self._memory_resource_consumption_value = memory_resource_consumption_value

    @property
    def memory_unit(self):
        """Gets the memory_unit of this ComputeDimension.

        内存消耗单位

        :return: The memory_unit of this ComputeDimension.
        :rtype: str
        """
        return self._memory_unit

    @memory_unit.setter
    def memory_unit(self, memory_unit):
        """Sets the memory_unit of this ComputeDimension.

        内存消耗单位

        :param memory_unit: The memory_unit of this ComputeDimension.
        :type memory_unit: str
        """
        self._memory_unit = memory_unit

    @property
    def last_cpu_resource_consumption_value(self):
        """Gets the last_cpu_resource_consumption_value of this ComputeDimension.

        上次cpu消耗值

        :return: The last_cpu_resource_consumption_value of this ComputeDimension.
        :rtype: int
        """
        return self._last_cpu_resource_consumption_value

    @last_cpu_resource_consumption_value.setter
    def last_cpu_resource_consumption_value(self, last_cpu_resource_consumption_value):
        """Sets the last_cpu_resource_consumption_value of this ComputeDimension.

        上次cpu消耗值

        :param last_cpu_resource_consumption_value: The last_cpu_resource_consumption_value of this ComputeDimension.
        :type last_cpu_resource_consumption_value: int
        """
        self._last_cpu_resource_consumption_value = last_cpu_resource_consumption_value

    @property
    def last_cpu_unit(self):
        """Gets the last_cpu_unit of this ComputeDimension.

        上次cpu消耗单位

        :return: The last_cpu_unit of this ComputeDimension.
        :rtype: str
        """
        return self._last_cpu_unit

    @last_cpu_unit.setter
    def last_cpu_unit(self, last_cpu_unit):
        """Sets the last_cpu_unit of this ComputeDimension.

        上次cpu消耗单位

        :param last_cpu_unit: The last_cpu_unit of this ComputeDimension.
        :type last_cpu_unit: str
        """
        self._last_cpu_unit = last_cpu_unit

    @property
    def last_memory_resource_consumption_value(self):
        """Gets the last_memory_resource_consumption_value of this ComputeDimension.

        上次内存消耗值

        :return: The last_memory_resource_consumption_value of this ComputeDimension.
        :rtype: int
        """
        return self._last_memory_resource_consumption_value

    @last_memory_resource_consumption_value.setter
    def last_memory_resource_consumption_value(self, last_memory_resource_consumption_value):
        """Sets the last_memory_resource_consumption_value of this ComputeDimension.

        上次内存消耗值

        :param last_memory_resource_consumption_value: The last_memory_resource_consumption_value of this ComputeDimension.
        :type last_memory_resource_consumption_value: int
        """
        self._last_memory_resource_consumption_value = last_memory_resource_consumption_value

    @property
    def last_memory_unit(self):
        """Gets the last_memory_unit of this ComputeDimension.

        上次内存消耗单位

        :return: The last_memory_unit of this ComputeDimension.
        :rtype: str
        """
        return self._last_memory_unit

    @last_memory_unit.setter
    def last_memory_unit(self, last_memory_unit):
        """Sets the last_memory_unit of this ComputeDimension.

        上次内存消耗单位

        :param last_memory_unit: The last_memory_unit of this ComputeDimension.
        :type last_memory_unit: str
        """
        self._last_memory_unit = last_memory_unit

    @property
    def creator(self):
        """Gets the creator of this ComputeDimension.

        节点实例创建者name

        :return: The creator of this ComputeDimension.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ComputeDimension.

        节点实例创建者name

        :param creator: The creator of this ComputeDimension.
        :type creator: str
        """
        self._creator = creator

    @property
    def warehouse_time_ms(self):
        """Gets the warehouse_time_ms of this ComputeDimension.

        数据入库时间,单位毫秒

        :return: The warehouse_time_ms of this ComputeDimension.
        :rtype: int
        """
        return self._warehouse_time_ms

    @warehouse_time_ms.setter
    def warehouse_time_ms(self, warehouse_time_ms):
        """Sets the warehouse_time_ms of this ComputeDimension.

        数据入库时间,单位毫秒

        :param warehouse_time_ms: The warehouse_time_ms of this ComputeDimension.
        :type warehouse_time_ms: int
        """
        self._warehouse_time_ms = warehouse_time_ms

    @property
    def extended_fields(self):
        """Gets the extended_fields of this ComputeDimension.

        扩展字段

        :return: The extended_fields of this ComputeDimension.
        :rtype: str
        """
        return self._extended_fields

    @extended_fields.setter
    def extended_fields(self, extended_fields):
        """Sets the extended_fields of this ComputeDimension.

        扩展字段

        :param extended_fields: The extended_fields of this ComputeDimension.
        :type extended_fields: str
        """
        self._extended_fields = extended_fields

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
        if not isinstance(other, ComputeDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
