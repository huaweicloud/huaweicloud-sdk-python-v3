# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerConfigsResDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host_network': 'bool',
        'container_port_list': 'list[ContainerPortDTO]'
    }

    attribute_map = {
        'host_network': 'host_network',
        'container_port_list': 'container_port_list'
    }

    def __init__(self, host_network=None, container_port_list=None):
        """ContainerConfigsResDTO

        The model defined in huaweicloud sdk

        :param host_network: 是否使用主机网络模式
        :type host_network: bool
        :param container_port_list: 容器端口映射值
        :type container_port_list: list[:class:`huaweicloudsdkiotedge.v2.ContainerPortDTO`]
        """
        
        

        self._host_network = None
        self._container_port_list = None
        self.discriminator = None

        if host_network is not None:
            self.host_network = host_network
        if container_port_list is not None:
            self.container_port_list = container_port_list

    @property
    def host_network(self):
        """Gets the host_network of this ContainerConfigsResDTO.

        是否使用主机网络模式

        :return: The host_network of this ContainerConfigsResDTO.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this ContainerConfigsResDTO.

        是否使用主机网络模式

        :param host_network: The host_network of this ContainerConfigsResDTO.
        :type host_network: bool
        """
        self._host_network = host_network

    @property
    def container_port_list(self):
        """Gets the container_port_list of this ContainerConfigsResDTO.

        容器端口映射值

        :return: The container_port_list of this ContainerConfigsResDTO.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.ContainerPortDTO`]
        """
        return self._container_port_list

    @container_port_list.setter
    def container_port_list(self, container_port_list):
        """Sets the container_port_list of this ContainerConfigsResDTO.

        容器端口映射值

        :param container_port_list: The container_port_list of this ContainerConfigsResDTO.
        :type container_port_list: list[:class:`huaweicloudsdkiotedge.v2.ContainerPortDTO`]
        """
        self._container_port_list = container_port_list

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
        if not isinstance(other, ContainerConfigsResDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
