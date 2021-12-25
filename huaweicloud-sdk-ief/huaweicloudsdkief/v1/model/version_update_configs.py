# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionUpdateConfigs:


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
        'ports': 'list[AppPorts]'
    }

    attribute_map = {
        'privileged': 'privileged',
        'host_network': 'host_network',
        'restart_policy': 'restart_policy',
        'ports': 'ports'
    }

    def __init__(self, privileged=None, host_network=None, restart_policy=None, ports=None):
        """VersionUpdateConfigs - a model defined in huaweicloud sdk"""
        
        

        self._privileged = None
        self._host_network = None
        self._restart_policy = None
        self._ports = None
        self.discriminator = None

        if privileged is not None:
            self.privileged = privileged
        if host_network is not None:
            self.host_network = host_network
        if restart_policy is not None:
            self.restart_policy = restart_policy
        if ports is not None:
            self.ports = ports

    @property
    def privileged(self):
        """Gets the privileged of this VersionUpdateConfigs.

        默认为false，表示是否开启特权模式

        :return: The privileged of this VersionUpdateConfigs.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this VersionUpdateConfigs.

        默认为false，表示是否开启特权模式

        :param privileged: The privileged of this VersionUpdateConfigs.
        :type: bool
        """
        self._privileged = privileged

    @property
    def host_network(self):
        """Gets the host_network of this VersionUpdateConfigs.

        默认为true，其中true表示主机网络，而false表示端口映射

        :return: The host_network of this VersionUpdateConfigs.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this VersionUpdateConfigs.

        默认为true，其中true表示主机网络，而false表示端口映射

        :param host_network: The host_network of this VersionUpdateConfigs.
        :type: bool
        """
        self._host_network = host_network

    @property
    def restart_policy(self):
        """Gets the restart_policy of this VersionUpdateConfigs.

        应用实例重启模式： 1. Always：当容器终止退出后，总是重启容器； 2. Onfailure：容器异常退出（退出码非0）时才重启容器； 3. Never：容器终止退出后，不重启容器；

        :return: The restart_policy of this VersionUpdateConfigs.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this VersionUpdateConfigs.

        应用实例重启模式： 1. Always：当容器终止退出后，总是重启容器； 2. Onfailure：容器异常退出（退出码非0）时才重启容器； 3. Never：容器终止退出后，不重启容器；

        :param restart_policy: The restart_policy of this VersionUpdateConfigs.
        :type: str
        """
        self._restart_policy = restart_policy

    @property
    def ports(self):
        """Gets the ports of this VersionUpdateConfigs.

        容器端口映射值

        :return: The ports of this VersionUpdateConfigs.
        :rtype: list[AppPorts]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this VersionUpdateConfigs.

        容器端口映射值

        :param ports: The ports of this VersionUpdateConfigs.
        :type: list[AppPorts]
        """
        self._ports = ports

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
        if not isinstance(other, VersionUpdateConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
