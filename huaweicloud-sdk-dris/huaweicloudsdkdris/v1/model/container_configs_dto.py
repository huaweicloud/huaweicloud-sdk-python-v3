# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerConfigsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'privileged': 'bool',
        'host_network': 'bool',
        'restart_policy': 'str',
        'container_port_list': 'list[ContainerPortDTO]'
    }

    attribute_map = {
        'privileged': 'privileged',
        'host_network': 'host_network',
        'restart_policy': 'restart_policy',
        'container_port_list': 'container_port_list'
    }

    def __init__(self, privileged=None, host_network=None, restart_policy=None, container_port_list=None):
        """ContainerConfigsDTO

        The model defined in huaweicloud sdk

        :param privileged: **参数说明**：开启容器特权模式。
        :type privileged: bool
        :param host_network: **参数说明**：是否使用主机网络模式。
        :type host_network: bool
        :param restart_policy: **参数说明**：重启策略，容器执行健康检查后失败后的策略。
        :type restart_policy: str
        :param container_port_list: **参数说明**：容器端口映射值。
        :type container_port_list: list[:class:`huaweicloudsdkdris.v1.ContainerPortDTO`]
        """
        
        

        self._privileged = None
        self._host_network = None
        self._restart_policy = None
        self._container_port_list = None
        self.discriminator = None

        if privileged is not None:
            self.privileged = privileged
        if host_network is not None:
            self.host_network = host_network
        self.restart_policy = restart_policy
        if container_port_list is not None:
            self.container_port_list = container_port_list

    @property
    def privileged(self):
        """Gets the privileged of this ContainerConfigsDTO.

        **参数说明**：开启容器特权模式。

        :return: The privileged of this ContainerConfigsDTO.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this ContainerConfigsDTO.

        **参数说明**：开启容器特权模式。

        :param privileged: The privileged of this ContainerConfigsDTO.
        :type privileged: bool
        """
        self._privileged = privileged

    @property
    def host_network(self):
        """Gets the host_network of this ContainerConfigsDTO.

        **参数说明**：是否使用主机网络模式。

        :return: The host_network of this ContainerConfigsDTO.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this ContainerConfigsDTO.

        **参数说明**：是否使用主机网络模式。

        :param host_network: The host_network of this ContainerConfigsDTO.
        :type host_network: bool
        """
        self._host_network = host_network

    @property
    def restart_policy(self):
        """Gets the restart_policy of this ContainerConfigsDTO.

        **参数说明**：重启策略，容器执行健康检查后失败后的策略。

        :return: The restart_policy of this ContainerConfigsDTO.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this ContainerConfigsDTO.

        **参数说明**：重启策略，容器执行健康检查后失败后的策略。

        :param restart_policy: The restart_policy of this ContainerConfigsDTO.
        :type restart_policy: str
        """
        self._restart_policy = restart_policy

    @property
    def container_port_list(self):
        """Gets the container_port_list of this ContainerConfigsDTO.

        **参数说明**：容器端口映射值。

        :return: The container_port_list of this ContainerConfigsDTO.
        :rtype: list[:class:`huaweicloudsdkdris.v1.ContainerPortDTO`]
        """
        return self._container_port_list

    @container_port_list.setter
    def container_port_list(self, container_port_list):
        """Sets the container_port_list of this ContainerConfigsDTO.

        **参数说明**：容器端口映射值。

        :param container_port_list: The container_port_list of this ContainerConfigsDTO.
        :type container_port_list: list[:class:`huaweicloudsdkdris.v1.ContainerPortDTO`]
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
        if not isinstance(other, ContainerConfigsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
