# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsRspHostProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus': 'int',
        'cores': 'int',
        'sockets': 'int',
        'memory': 'int',
        'host_type': 'str',
        'host_type_name': 'str',
        'available_instance_capacities': 'list[ListHostsRspHostPropertiesAvailableInstanceCapacities]'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'cores': 'cores',
        'sockets': 'sockets',
        'memory': 'memory',
        'host_type': 'host_type',
        'host_type_name': 'host_type_name',
        'available_instance_capacities': 'available_instance_capacities'
    }

    def __init__(self, vcpus=None, cores=None, sockets=None, memory=None, host_type=None, host_type_name=None, available_instance_capacities=None):
        r"""ListHostsRspHostProperties

        The model defined in huaweicloud sdk

        :param vcpus: 云办公主机的vCPUs个数。
        :type vcpus: int
        :param cores: 云办公主机的物理核数。
        :type cores: int
        :param sockets: 云办公主机的物理套接字数量。
        :type sockets: int
        :param memory: 云办公主机的物理内存大小。
        :type memory: int
        :param host_type: 云办公主机类型。
        :type host_type: str
        :param host_type_name: 云办公主机类型名称。
        :type host_type_name: str
        :param available_instance_capacities: 可以创建的规格。
        :type available_instance_capacities: list[:class:`huaweicloudsdkworkspace.v2.ListHostsRspHostPropertiesAvailableInstanceCapacities`]
        """
        
        

        self._vcpus = None
        self._cores = None
        self._sockets = None
        self._memory = None
        self._host_type = None
        self._host_type_name = None
        self._available_instance_capacities = None
        self.discriminator = None

        if vcpus is not None:
            self.vcpus = vcpus
        if cores is not None:
            self.cores = cores
        if sockets is not None:
            self.sockets = sockets
        if memory is not None:
            self.memory = memory
        if host_type is not None:
            self.host_type = host_type
        if host_type_name is not None:
            self.host_type_name = host_type_name
        if available_instance_capacities is not None:
            self.available_instance_capacities = available_instance_capacities

    @property
    def vcpus(self):
        r"""Gets the vcpus of this ListHostsRspHostProperties.

        云办公主机的vCPUs个数。

        :return: The vcpus of this ListHostsRspHostProperties.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this ListHostsRspHostProperties.

        云办公主机的vCPUs个数。

        :param vcpus: The vcpus of this ListHostsRspHostProperties.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def cores(self):
        r"""Gets the cores of this ListHostsRspHostProperties.

        云办公主机的物理核数。

        :return: The cores of this ListHostsRspHostProperties.
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        r"""Sets the cores of this ListHostsRspHostProperties.

        云办公主机的物理核数。

        :param cores: The cores of this ListHostsRspHostProperties.
        :type cores: int
        """
        self._cores = cores

    @property
    def sockets(self):
        r"""Gets the sockets of this ListHostsRspHostProperties.

        云办公主机的物理套接字数量。

        :return: The sockets of this ListHostsRspHostProperties.
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        r"""Sets the sockets of this ListHostsRspHostProperties.

        云办公主机的物理套接字数量。

        :param sockets: The sockets of this ListHostsRspHostProperties.
        :type sockets: int
        """
        self._sockets = sockets

    @property
    def memory(self):
        r"""Gets the memory of this ListHostsRspHostProperties.

        云办公主机的物理内存大小。

        :return: The memory of this ListHostsRspHostProperties.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ListHostsRspHostProperties.

        云办公主机的物理内存大小。

        :param memory: The memory of this ListHostsRspHostProperties.
        :type memory: int
        """
        self._memory = memory

    @property
    def host_type(self):
        r"""Gets the host_type of this ListHostsRspHostProperties.

        云办公主机类型。

        :return: The host_type of this ListHostsRspHostProperties.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this ListHostsRspHostProperties.

        云办公主机类型。

        :param host_type: The host_type of this ListHostsRspHostProperties.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def host_type_name(self):
        r"""Gets the host_type_name of this ListHostsRspHostProperties.

        云办公主机类型名称。

        :return: The host_type_name of this ListHostsRspHostProperties.
        :rtype: str
        """
        return self._host_type_name

    @host_type_name.setter
    def host_type_name(self, host_type_name):
        r"""Sets the host_type_name of this ListHostsRspHostProperties.

        云办公主机类型名称。

        :param host_type_name: The host_type_name of this ListHostsRspHostProperties.
        :type host_type_name: str
        """
        self._host_type_name = host_type_name

    @property
    def available_instance_capacities(self):
        r"""Gets the available_instance_capacities of this ListHostsRspHostProperties.

        可以创建的规格。

        :return: The available_instance_capacities of this ListHostsRspHostProperties.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ListHostsRspHostPropertiesAvailableInstanceCapacities`]
        """
        return self._available_instance_capacities

    @available_instance_capacities.setter
    def available_instance_capacities(self, available_instance_capacities):
        r"""Sets the available_instance_capacities of this ListHostsRspHostProperties.

        可以创建的规格。

        :param available_instance_capacities: The available_instance_capacities of this ListHostsRspHostProperties.
        :type available_instance_capacities: list[:class:`huaweicloudsdkworkspace.v2.ListHostsRspHostPropertiesAvailableInstanceCapacities`]
        """
        self._available_instance_capacities = available_instance_capacities

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListHostsRspHostProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
