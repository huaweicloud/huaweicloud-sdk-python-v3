# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_kbps': 'str',
        'output_kbps': 'str',
        'instance_id': 'str',
        'keys': 'int',
        'used_memory': 'int',
        'max_memory': 'int',
        'cmd_get_count': 'int',
        'cmd_set_count': 'int',
        'used_cpu': 'str'
    }

    attribute_map = {
        'input_kbps': 'input_kbps',
        'output_kbps': 'output_kbps',
        'instance_id': 'instance_id',
        'keys': 'keys',
        'used_memory': 'used_memory',
        'max_memory': 'max_memory',
        'cmd_get_count': 'cmd_get_count',
        'cmd_set_count': 'cmd_set_count',
        'used_cpu': 'used_cpu'
    }

    def __init__(self, input_kbps=None, output_kbps=None, instance_id=None, keys=None, used_memory=None, max_memory=None, cmd_get_count=None, cmd_set_count=None, used_cpu=None):
        r"""InstanceStatistic

        The model defined in huaweicloud sdk

        :param input_kbps: 缓存实例网络入流量，单位：Kbps。
        :type input_kbps: str
        :param output_kbps: 缓存实例网络出流量，单位：Kbps。
        :type output_kbps: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param keys: 缓存存储的数据条数。
        :type keys: int
        :param used_memory: 缓存已经使用内存，单位：MB。
        :type used_memory: int
        :param max_memory: 缓存的总内存，单位：MB。
        :type max_memory: int
        :param cmd_get_count: 缓存get命令被调用次数。
        :type cmd_get_count: int
        :param cmd_set_count: 缓存set命令被调用次数。
        :type cmd_set_count: int
        :param used_cpu: CPU使用率，单位：百分比。
        :type used_cpu: str
        """
        
        

        self._input_kbps = None
        self._output_kbps = None
        self._instance_id = None
        self._keys = None
        self._used_memory = None
        self._max_memory = None
        self._cmd_get_count = None
        self._cmd_set_count = None
        self._used_cpu = None
        self.discriminator = None

        if input_kbps is not None:
            self.input_kbps = input_kbps
        if output_kbps is not None:
            self.output_kbps = output_kbps
        if instance_id is not None:
            self.instance_id = instance_id
        if keys is not None:
            self.keys = keys
        if used_memory is not None:
            self.used_memory = used_memory
        if max_memory is not None:
            self.max_memory = max_memory
        if cmd_get_count is not None:
            self.cmd_get_count = cmd_get_count
        if cmd_set_count is not None:
            self.cmd_set_count = cmd_set_count
        if used_cpu is not None:
            self.used_cpu = used_cpu

    @property
    def input_kbps(self):
        r"""Gets the input_kbps of this InstanceStatistic.

        缓存实例网络入流量，单位：Kbps。

        :return: The input_kbps of this InstanceStatistic.
        :rtype: str
        """
        return self._input_kbps

    @input_kbps.setter
    def input_kbps(self, input_kbps):
        r"""Sets the input_kbps of this InstanceStatistic.

        缓存实例网络入流量，单位：Kbps。

        :param input_kbps: The input_kbps of this InstanceStatistic.
        :type input_kbps: str
        """
        self._input_kbps = input_kbps

    @property
    def output_kbps(self):
        r"""Gets the output_kbps of this InstanceStatistic.

        缓存实例网络出流量，单位：Kbps。

        :return: The output_kbps of this InstanceStatistic.
        :rtype: str
        """
        return self._output_kbps

    @output_kbps.setter
    def output_kbps(self, output_kbps):
        r"""Sets the output_kbps of this InstanceStatistic.

        缓存实例网络出流量，单位：Kbps。

        :param output_kbps: The output_kbps of this InstanceStatistic.
        :type output_kbps: str
        """
        self._output_kbps = output_kbps

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceStatistic.

        实例ID。

        :return: The instance_id of this InstanceStatistic.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceStatistic.

        实例ID。

        :param instance_id: The instance_id of this InstanceStatistic.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def keys(self):
        r"""Gets the keys of this InstanceStatistic.

        缓存存储的数据条数。

        :return: The keys of this InstanceStatistic.
        :rtype: int
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this InstanceStatistic.

        缓存存储的数据条数。

        :param keys: The keys of this InstanceStatistic.
        :type keys: int
        """
        self._keys = keys

    @property
    def used_memory(self):
        r"""Gets the used_memory of this InstanceStatistic.

        缓存已经使用内存，单位：MB。

        :return: The used_memory of this InstanceStatistic.
        :rtype: int
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        r"""Sets the used_memory of this InstanceStatistic.

        缓存已经使用内存，单位：MB。

        :param used_memory: The used_memory of this InstanceStatistic.
        :type used_memory: int
        """
        self._used_memory = used_memory

    @property
    def max_memory(self):
        r"""Gets the max_memory of this InstanceStatistic.

        缓存的总内存，单位：MB。

        :return: The max_memory of this InstanceStatistic.
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        r"""Sets the max_memory of this InstanceStatistic.

        缓存的总内存，单位：MB。

        :param max_memory: The max_memory of this InstanceStatistic.
        :type max_memory: int
        """
        self._max_memory = max_memory

    @property
    def cmd_get_count(self):
        r"""Gets the cmd_get_count of this InstanceStatistic.

        缓存get命令被调用次数。

        :return: The cmd_get_count of this InstanceStatistic.
        :rtype: int
        """
        return self._cmd_get_count

    @cmd_get_count.setter
    def cmd_get_count(self, cmd_get_count):
        r"""Sets the cmd_get_count of this InstanceStatistic.

        缓存get命令被调用次数。

        :param cmd_get_count: The cmd_get_count of this InstanceStatistic.
        :type cmd_get_count: int
        """
        self._cmd_get_count = cmd_get_count

    @property
    def cmd_set_count(self):
        r"""Gets the cmd_set_count of this InstanceStatistic.

        缓存set命令被调用次数。

        :return: The cmd_set_count of this InstanceStatistic.
        :rtype: int
        """
        return self._cmd_set_count

    @cmd_set_count.setter
    def cmd_set_count(self, cmd_set_count):
        r"""Sets the cmd_set_count of this InstanceStatistic.

        缓存set命令被调用次数。

        :param cmd_set_count: The cmd_set_count of this InstanceStatistic.
        :type cmd_set_count: int
        """
        self._cmd_set_count = cmd_set_count

    @property
    def used_cpu(self):
        r"""Gets the used_cpu of this InstanceStatistic.

        CPU使用率，单位：百分比。

        :return: The used_cpu of this InstanceStatistic.
        :rtype: str
        """
        return self._used_cpu

    @used_cpu.setter
    def used_cpu(self, used_cpu):
        r"""Sets the used_cpu of this InstanceStatistic.

        CPU使用率，单位：百分比。

        :param used_cpu: The used_cpu of this InstanceStatistic.
        :type used_cpu: str
        """
        self._used_cpu = used_cpu

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
        if not isinstance(other, InstanceStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
