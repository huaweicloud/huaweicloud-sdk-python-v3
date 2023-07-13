# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterUpgradeResponseAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'target_version': 'str',
        'target_platform_version': 'str',
        'strategy': 'UpgradeStrategy',
        'config': 'object'
    }

    attribute_map = {
        'version': 'version',
        'target_version': 'targetVersion',
        'target_platform_version': 'targetPlatformVersion',
        'strategy': 'strategy',
        'config': 'config'
    }

    def __init__(self, version=None, target_version=None, target_platform_version=None, strategy=None, config=None):
        """ClusterUpgradeResponseAction

        The model defined in huaweicloud sdk

        :param version: 当前集群版本
        :type version: str
        :param target_version: 目标集群版本，例如\&quot;v1.23\&quot;
        :type target_version: str
        :param target_platform_version: 目标集群的平台版本号，表示集群版本(version)下的内部版本，不支持用户指定。
        :type target_platform_version: str
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        :param config: 升级过程中指定的集群配置
        :type config: object
        """
        
        

        self._version = None
        self._target_version = None
        self._target_platform_version = None
        self._strategy = None
        self._config = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if target_version is not None:
            self.target_version = target_version
        if target_platform_version is not None:
            self.target_platform_version = target_platform_version
        if strategy is not None:
            self.strategy = strategy
        if config is not None:
            self.config = config

    @property
    def version(self):
        """Gets the version of this ClusterUpgradeResponseAction.

        当前集群版本

        :return: The version of this ClusterUpgradeResponseAction.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterUpgradeResponseAction.

        当前集群版本

        :param version: The version of this ClusterUpgradeResponseAction.
        :type version: str
        """
        self._version = version

    @property
    def target_version(self):
        """Gets the target_version of this ClusterUpgradeResponseAction.

        目标集群版本，例如\"v1.23\"

        :return: The target_version of this ClusterUpgradeResponseAction.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ClusterUpgradeResponseAction.

        目标集群版本，例如\"v1.23\"

        :param target_version: The target_version of this ClusterUpgradeResponseAction.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def target_platform_version(self):
        """Gets the target_platform_version of this ClusterUpgradeResponseAction.

        目标集群的平台版本号，表示集群版本(version)下的内部版本，不支持用户指定。

        :return: The target_platform_version of this ClusterUpgradeResponseAction.
        :rtype: str
        """
        return self._target_platform_version

    @target_platform_version.setter
    def target_platform_version(self, target_platform_version):
        """Sets the target_platform_version of this ClusterUpgradeResponseAction.

        目标集群的平台版本号，表示集群版本(version)下的内部版本，不支持用户指定。

        :param target_platform_version: The target_platform_version of this ClusterUpgradeResponseAction.
        :type target_platform_version: str
        """
        self._target_platform_version = target_platform_version

    @property
    def strategy(self):
        """Gets the strategy of this ClusterUpgradeResponseAction.

        :return: The strategy of this ClusterUpgradeResponseAction.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this ClusterUpgradeResponseAction.

        :param strategy: The strategy of this ClusterUpgradeResponseAction.
        :type strategy: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        """
        self._strategy = strategy

    @property
    def config(self):
        """Gets the config of this ClusterUpgradeResponseAction.

        升级过程中指定的集群配置

        :return: The config of this ClusterUpgradeResponseAction.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ClusterUpgradeResponseAction.

        升级过程中指定的集群配置

        :param config: The config of this ClusterUpgradeResponseAction.
        :type config: object
        """
        self._config = config

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
        if not isinstance(other, ClusterUpgradeResponseAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
