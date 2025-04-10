# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostContainerPortMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_port': 'int',
        'host_port': 'int',
        'host_ip': 'str',
        'host_port_range': 'HostPortRange'
    }

    attribute_map = {
        'container_port': 'container_port',
        'host_port': 'host_port',
        'host_ip': 'host_ip',
        'host_port_range': 'host_port_range'
    }

    def __init__(self, container_port=None, host_port=None, host_ip=None, host_port_range=None):
        r"""HostContainerPortMapping

        The model defined in huaweicloud sdk

        :param container_port: 构成一堆映射的容器端口
        :type container_port: int
        :param host_port: 构成一对映射的物理机对应网卡端口
        :type host_port: int
        :param host_ip: 对应网卡地址
        :type host_ip: str
        :param host_port_range: 
        :type host_port_range: :class:`huaweicloudsdkief.v1.HostPortRange`
        """
        
        

        self._container_port = None
        self._host_port = None
        self._host_ip = None
        self._host_port_range = None
        self.discriminator = None

        self.container_port = container_port
        if host_port is not None:
            self.host_port = host_port
        if host_ip is not None:
            self.host_ip = host_ip
        if host_port_range is not None:
            self.host_port_range = host_port_range

    @property
    def container_port(self):
        r"""Gets the container_port of this HostContainerPortMapping.

        构成一堆映射的容器端口

        :return: The container_port of this HostContainerPortMapping.
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        r"""Sets the container_port of this HostContainerPortMapping.

        构成一堆映射的容器端口

        :param container_port: The container_port of this HostContainerPortMapping.
        :type container_port: int
        """
        self._container_port = container_port

    @property
    def host_port(self):
        r"""Gets the host_port of this HostContainerPortMapping.

        构成一对映射的物理机对应网卡端口

        :return: The host_port of this HostContainerPortMapping.
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        r"""Sets the host_port of this HostContainerPortMapping.

        构成一对映射的物理机对应网卡端口

        :param host_port: The host_port of this HostContainerPortMapping.
        :type host_port: int
        """
        self._host_port = host_port

    @property
    def host_ip(self):
        r"""Gets the host_ip of this HostContainerPortMapping.

        对应网卡地址

        :return: The host_ip of this HostContainerPortMapping.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this HostContainerPortMapping.

        对应网卡地址

        :param host_ip: The host_ip of this HostContainerPortMapping.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_port_range(self):
        r"""Gets the host_port_range of this HostContainerPortMapping.

        :return: The host_port_range of this HostContainerPortMapping.
        :rtype: :class:`huaweicloudsdkief.v1.HostPortRange`
        """
        return self._host_port_range

    @host_port_range.setter
    def host_port_range(self, host_port_range):
        r"""Sets the host_port_range of this HostContainerPortMapping.

        :param host_port_range: The host_port_range of this HostContainerPortMapping.
        :type host_port_range: :class:`huaweicloudsdkief.v1.HostPortRange`
        """
        self._host_port_range = host_port_range

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
        if not isinstance(other, HostContainerPortMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
