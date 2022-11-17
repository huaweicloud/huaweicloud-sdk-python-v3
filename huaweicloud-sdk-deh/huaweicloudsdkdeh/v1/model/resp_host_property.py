# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespHostProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_type': 'str',
        'host_type_name': 'str',
        'vcpus': 'int',
        'cores': 'int',
        'sockets': 'int',
        'memory': 'int',
        'available_instance_capacities': 'list[RespInstanceCapacity]'
    }

    attribute_map = {
        'host_type': 'host_type',
        'host_type_name': 'host_type_name',
        'vcpus': 'vcpus',
        'cores': 'cores',
        'sockets': 'sockets',
        'memory': 'memory',
        'available_instance_capacities': 'available_instance_capacities'
    }

    def __init__(self, host_type=None, host_type_name=None, vcpus=None, cores=None, sockets=None, memory=None, available_instance_capacities=None):
        """RespHostProperty

        The model defined in huaweicloud sdk

        :param host_type: 专属主机类型。
        :type host_type: str
        :param host_type_name: 专属主机类型的名称。
        :type host_type_name: str
        :param vcpus: 专属主机的vCPUs个数。
        :type vcpus: int
        :param cores: 专属主机的物理核数。
        :type cores: int
        :param sockets: 专属主机的物理套接字数量。
        :type sockets: int
        :param memory: 专属主机的物理内存大小。
        :type memory: int
        :param available_instance_capacities: 专属主机上创建的云服务器规格。
        :type available_instance_capacities: list[:class:`huaweicloudsdkdeh.v1.RespInstanceCapacity`]
        """
        
        

        self._host_type = None
        self._host_type_name = None
        self._vcpus = None
        self._cores = None
        self._sockets = None
        self._memory = None
        self._available_instance_capacities = None
        self.discriminator = None

        self.host_type = host_type
        self.host_type_name = host_type_name
        self.vcpus = vcpus
        self.cores = cores
        self.sockets = sockets
        self.memory = memory
        self.available_instance_capacities = available_instance_capacities

    @property
    def host_type(self):
        """Gets the host_type of this RespHostProperty.

        专属主机类型。

        :return: The host_type of this RespHostProperty.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this RespHostProperty.

        专属主机类型。

        :param host_type: The host_type of this RespHostProperty.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def host_type_name(self):
        """Gets the host_type_name of this RespHostProperty.

        专属主机类型的名称。

        :return: The host_type_name of this RespHostProperty.
        :rtype: str
        """
        return self._host_type_name

    @host_type_name.setter
    def host_type_name(self, host_type_name):
        """Sets the host_type_name of this RespHostProperty.

        专属主机类型的名称。

        :param host_type_name: The host_type_name of this RespHostProperty.
        :type host_type_name: str
        """
        self._host_type_name = host_type_name

    @property
    def vcpus(self):
        """Gets the vcpus of this RespHostProperty.

        专属主机的vCPUs个数。

        :return: The vcpus of this RespHostProperty.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this RespHostProperty.

        专属主机的vCPUs个数。

        :param vcpus: The vcpus of this RespHostProperty.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def cores(self):
        """Gets the cores of this RespHostProperty.

        专属主机的物理核数。

        :return: The cores of this RespHostProperty.
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this RespHostProperty.

        专属主机的物理核数。

        :param cores: The cores of this RespHostProperty.
        :type cores: int
        """
        self._cores = cores

    @property
    def sockets(self):
        """Gets the sockets of this RespHostProperty.

        专属主机的物理套接字数量。

        :return: The sockets of this RespHostProperty.
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this RespHostProperty.

        专属主机的物理套接字数量。

        :param sockets: The sockets of this RespHostProperty.
        :type sockets: int
        """
        self._sockets = sockets

    @property
    def memory(self):
        """Gets the memory of this RespHostProperty.

        专属主机的物理内存大小。

        :return: The memory of this RespHostProperty.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this RespHostProperty.

        专属主机的物理内存大小。

        :param memory: The memory of this RespHostProperty.
        :type memory: int
        """
        self._memory = memory

    @property
    def available_instance_capacities(self):
        """Gets the available_instance_capacities of this RespHostProperty.

        专属主机上创建的云服务器规格。

        :return: The available_instance_capacities of this RespHostProperty.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.RespInstanceCapacity`]
        """
        return self._available_instance_capacities

    @available_instance_capacities.setter
    def available_instance_capacities(self, available_instance_capacities):
        """Sets the available_instance_capacities of this RespHostProperty.

        专属主机上创建的云服务器规格。

        :param available_instance_capacities: The available_instance_capacities of this RespHostProperty.
        :type available_instance_capacities: list[:class:`huaweicloudsdkdeh.v1.RespInstanceCapacity`]
        """
        self._available_instance_capacities = available_instance_capacities

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
        if not isinstance(other, RespHostProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
