# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RingHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'back_ip': 'str',
        'cpu_cores': 'int',
        'memory': 'float',
        'disk_size': 'float'
    }

    attribute_map = {
        'host_name': 'host_name',
        'back_ip': 'back_ip',
        'cpu_cores': 'cpu_cores',
        'memory': 'memory',
        'disk_size': 'disk_size'
    }

    def __init__(self, host_name=None, back_ip=None, cpu_cores=None, memory=None, disk_size=None):
        r"""RingHost

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**： 主机名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type host_name: str
        :param back_ip: **参数解释**： 后端IP地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type back_ip: str
        :param cpu_cores: **参数解释**： 主机CPU核数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cpu_cores: int
        :param memory: **参数解释**： 主机内存。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type memory: float
        :param disk_size: **参数解释**： 主机磁盘大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type disk_size: float
        """
        
        

        self._host_name = None
        self._back_ip = None
        self._cpu_cores = None
        self._memory = None
        self._disk_size = None
        self.discriminator = None

        self.host_name = host_name
        self.back_ip = back_ip
        self.cpu_cores = cpu_cores
        self.memory = memory
        self.disk_size = disk_size

    @property
    def host_name(self):
        r"""Gets the host_name of this RingHost.

        **参数解释**： 主机名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The host_name of this RingHost.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this RingHost.

        **参数解释**： 主机名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param host_name: The host_name of this RingHost.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def back_ip(self):
        r"""Gets the back_ip of this RingHost.

        **参数解释**： 后端IP地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The back_ip of this RingHost.
        :rtype: str
        """
        return self._back_ip

    @back_ip.setter
    def back_ip(self, back_ip):
        r"""Sets the back_ip of this RingHost.

        **参数解释**： 后端IP地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param back_ip: The back_ip of this RingHost.
        :type back_ip: str
        """
        self._back_ip = back_ip

    @property
    def cpu_cores(self):
        r"""Gets the cpu_cores of this RingHost.

        **参数解释**： 主机CPU核数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cpu_cores of this RingHost.
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        r"""Sets the cpu_cores of this RingHost.

        **参数解释**： 主机CPU核数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cpu_cores: The cpu_cores of this RingHost.
        :type cpu_cores: int
        """
        self._cpu_cores = cpu_cores

    @property
    def memory(self):
        r"""Gets the memory of this RingHost.

        **参数解释**： 主机内存。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The memory of this RingHost.
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this RingHost.

        **参数解释**： 主机内存。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param memory: The memory of this RingHost.
        :type memory: float
        """
        self._memory = memory

    @property
    def disk_size(self):
        r"""Gets the disk_size of this RingHost.

        **参数解释**： 主机磁盘大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The disk_size of this RingHost.
        :rtype: float
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        r"""Sets the disk_size of this RingHost.

        **参数解释**： 主机磁盘大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param disk_size: The disk_size of this RingHost.
        :type disk_size: float
        """
        self._disk_size = disk_size

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
        if not isinstance(other, RingHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
