# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodConfigs:

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
        'host_pid': 'bool',
        'migration': 'bool',
        'restart_policy': 'str',
        'toleration_seconds': 'int'
    }

    attribute_map = {
        'host_network': 'host_network',
        'host_pid': 'host_pid',
        'migration': 'migration',
        'restart_policy': 'restart_policy',
        'toleration_seconds': 'toleration_seconds'
    }

    def __init__(self, host_network=None, host_pid=None, migration=None, restart_policy=None, toleration_seconds=None):
        """PodConfigs

        The model defined in huaweicloud sdk

        :param host_network: 应用实例是否启用主机网络，不启用则使用端口映射，默认值false
        :type host_network: bool
        :param host_pid: 应用实例是否与主机共PID命名空间，默认值false
        :type host_pid: bool
        :param migration: 应用实例故障是否迁移，指定节点组部署时必选，默认值false
        :type migration: bool
        :param restart_policy: 应用实例重启策略，可选值Always、OnFailure、Never
        :type restart_policy: str
        :param toleration_seconds: 应用实例故障容忍时间，容忍时间到达后迁移应用实例，只在指定节点组部署时生效
        :type toleration_seconds: int
        """
        
        

        self._host_network = None
        self._host_pid = None
        self._migration = None
        self._restart_policy = None
        self._toleration_seconds = None
        self.discriminator = None

        if host_network is not None:
            self.host_network = host_network
        if host_pid is not None:
            self.host_pid = host_pid
        if migration is not None:
            self.migration = migration
        self.restart_policy = restart_policy
        if toleration_seconds is not None:
            self.toleration_seconds = toleration_seconds

    @property
    def host_network(self):
        """Gets the host_network of this PodConfigs.

        应用实例是否启用主机网络，不启用则使用端口映射，默认值false

        :return: The host_network of this PodConfigs.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this PodConfigs.

        应用实例是否启用主机网络，不启用则使用端口映射，默认值false

        :param host_network: The host_network of this PodConfigs.
        :type host_network: bool
        """
        self._host_network = host_network

    @property
    def host_pid(self):
        """Gets the host_pid of this PodConfigs.

        应用实例是否与主机共PID命名空间，默认值false

        :return: The host_pid of this PodConfigs.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """Sets the host_pid of this PodConfigs.

        应用实例是否与主机共PID命名空间，默认值false

        :param host_pid: The host_pid of this PodConfigs.
        :type host_pid: bool
        """
        self._host_pid = host_pid

    @property
    def migration(self):
        """Gets the migration of this PodConfigs.

        应用实例故障是否迁移，指定节点组部署时必选，默认值false

        :return: The migration of this PodConfigs.
        :rtype: bool
        """
        return self._migration

    @migration.setter
    def migration(self, migration):
        """Sets the migration of this PodConfigs.

        应用实例故障是否迁移，指定节点组部署时必选，默认值false

        :param migration: The migration of this PodConfigs.
        :type migration: bool
        """
        self._migration = migration

    @property
    def restart_policy(self):
        """Gets the restart_policy of this PodConfigs.

        应用实例重启策略，可选值Always、OnFailure、Never

        :return: The restart_policy of this PodConfigs.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this PodConfigs.

        应用实例重启策略，可选值Always、OnFailure、Never

        :param restart_policy: The restart_policy of this PodConfigs.
        :type restart_policy: str
        """
        self._restart_policy = restart_policy

    @property
    def toleration_seconds(self):
        """Gets the toleration_seconds of this PodConfigs.

        应用实例故障容忍时间，容忍时间到达后迁移应用实例，只在指定节点组部署时生效

        :return: The toleration_seconds of this PodConfigs.
        :rtype: int
        """
        return self._toleration_seconds

    @toleration_seconds.setter
    def toleration_seconds(self, toleration_seconds):
        """Sets the toleration_seconds of this PodConfigs.

        应用实例故障容忍时间，容忍时间到达后迁移应用实例，只在指定节点组部署时生效

        :param toleration_seconds: The toleration_seconds of this PodConfigs.
        :type toleration_seconds: int
        """
        self._toleration_seconds = toleration_seconds

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
        if not isinstance(other, PodConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
