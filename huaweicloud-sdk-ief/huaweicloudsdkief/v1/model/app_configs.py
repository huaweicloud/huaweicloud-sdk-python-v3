# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppConfigs:

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
        'run_as_user': 'int',
        'host_network': 'bool',
        'restart_policy': 'str',
        'ports': 'list[Ports]',
        'host_pid': 'bool',
        'dns_policy': 'str'
    }

    attribute_map = {
        'privileged': 'privileged',
        'run_as_user': 'run_as_user',
        'host_network': 'host_network',
        'restart_policy': 'restart_policy',
        'ports': 'ports',
        'host_pid': 'host_pid',
        'dns_policy': 'dns_policy'
    }

    def __init__(self, privileged=None, run_as_user=None, host_network=None, restart_policy=None, ports=None, host_pid=None, dns_policy=None):
        """AppConfigs

        The model defined in huaweicloud sdk

        :param privileged: 默认为false，表示是否开启特权模式
        :type privileged: bool
        :param run_as_user: 容器运行用户ID，输入范围为0~65534的整数
        :type run_as_user: int
        :param host_network: 默认为true，其中true表示主机网络，而false表示端口映射
        :type host_network: bool
        :param restart_policy: 应用实例重启模式： - Always：当容器终止退出后，总是重启容器 - Onfailure：容器异常退出（退出码非0）时才重启容器 - Never：容器终止退出后，不重启容器
        :type restart_policy: str
        :param ports: 容器端口映射值
        :type ports: list[:class:`huaweicloudsdkief.v1.Ports`]
        :param host_pid: 应用实例是否与主机共PID命名空间，默认值false
        :type host_pid: bool
        :param dns_policy: 应用实例DNS策略，可选值Default、ClusterFirst、ClusterFirstWithHostNet，默认为Default。应用实例启用主机网络时只能选填Default、ClusterFirstWithHostNet，不启用主机网络时只能选填Default、ClusterFirst
        :type dns_policy: str
        """
        
        

        self._privileged = None
        self._run_as_user = None
        self._host_network = None
        self._restart_policy = None
        self._ports = None
        self._host_pid = None
        self._dns_policy = None
        self.discriminator = None

        if privileged is not None:
            self.privileged = privileged
        if run_as_user is not None:
            self.run_as_user = run_as_user
        if host_network is not None:
            self.host_network = host_network
        if restart_policy is not None:
            self.restart_policy = restart_policy
        if ports is not None:
            self.ports = ports
        if host_pid is not None:
            self.host_pid = host_pid
        if dns_policy is not None:
            self.dns_policy = dns_policy

    @property
    def privileged(self):
        """Gets the privileged of this AppConfigs.

        默认为false，表示是否开启特权模式

        :return: The privileged of this AppConfigs.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this AppConfigs.

        默认为false，表示是否开启特权模式

        :param privileged: The privileged of this AppConfigs.
        :type privileged: bool
        """
        self._privileged = privileged

    @property
    def run_as_user(self):
        """Gets the run_as_user of this AppConfigs.

        容器运行用户ID，输入范围为0~65534的整数

        :return: The run_as_user of this AppConfigs.
        :rtype: int
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """Sets the run_as_user of this AppConfigs.

        容器运行用户ID，输入范围为0~65534的整数

        :param run_as_user: The run_as_user of this AppConfigs.
        :type run_as_user: int
        """
        self._run_as_user = run_as_user

    @property
    def host_network(self):
        """Gets the host_network of this AppConfigs.

        默认为true，其中true表示主机网络，而false表示端口映射

        :return: The host_network of this AppConfigs.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this AppConfigs.

        默认为true，其中true表示主机网络，而false表示端口映射

        :param host_network: The host_network of this AppConfigs.
        :type host_network: bool
        """
        self._host_network = host_network

    @property
    def restart_policy(self):
        """Gets the restart_policy of this AppConfigs.

        应用实例重启模式： - Always：当容器终止退出后，总是重启容器 - Onfailure：容器异常退出（退出码非0）时才重启容器 - Never：容器终止退出后，不重启容器

        :return: The restart_policy of this AppConfigs.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this AppConfigs.

        应用实例重启模式： - Always：当容器终止退出后，总是重启容器 - Onfailure：容器异常退出（退出码非0）时才重启容器 - Never：容器终止退出后，不重启容器

        :param restart_policy: The restart_policy of this AppConfigs.
        :type restart_policy: str
        """
        self._restart_policy = restart_policy

    @property
    def ports(self):
        """Gets the ports of this AppConfigs.

        容器端口映射值

        :return: The ports of this AppConfigs.
        :rtype: list[:class:`huaweicloudsdkief.v1.Ports`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this AppConfigs.

        容器端口映射值

        :param ports: The ports of this AppConfigs.
        :type ports: list[:class:`huaweicloudsdkief.v1.Ports`]
        """
        self._ports = ports

    @property
    def host_pid(self):
        """Gets the host_pid of this AppConfigs.

        应用实例是否与主机共PID命名空间，默认值false

        :return: The host_pid of this AppConfigs.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """Sets the host_pid of this AppConfigs.

        应用实例是否与主机共PID命名空间，默认值false

        :param host_pid: The host_pid of this AppConfigs.
        :type host_pid: bool
        """
        self._host_pid = host_pid

    @property
    def dns_policy(self):
        """Gets the dns_policy of this AppConfigs.

        应用实例DNS策略，可选值Default、ClusterFirst、ClusterFirstWithHostNet，默认为Default。应用实例启用主机网络时只能选填Default、ClusterFirstWithHostNet，不启用主机网络时只能选填Default、ClusterFirst

        :return: The dns_policy of this AppConfigs.
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        """Sets the dns_policy of this AppConfigs.

        应用实例DNS策略，可选值Default、ClusterFirst、ClusterFirstWithHostNet，默认为Default。应用实例启用主机网络时只能选填Default、ClusterFirstWithHostNet，不启用主机网络时只能选填Default、ClusterFirst

        :param dns_policy: The dns_policy of this AppConfigs.
        :type dns_policy: str
        """
        self._dns_policy = dns_policy

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
        if not isinstance(other, AppConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
