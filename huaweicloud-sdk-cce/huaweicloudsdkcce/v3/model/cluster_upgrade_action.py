# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterUpgradeAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addons': 'list[UpgradeAddonConfig]',
        'node_order': 'dict(str, list[NodePriority])',
        'node_pool_order': 'dict(str, int)',
        'strategy': 'UpgradeStrategy',
        'target_version': 'str',
        'is_only_upgrade': 'bool'
    }

    attribute_map = {
        'addons': 'addons',
        'node_order': 'nodeOrder',
        'node_pool_order': 'nodePoolOrder',
        'strategy': 'strategy',
        'target_version': 'targetVersion',
        'is_only_upgrade': 'isOnlyUpgrade'
    }

    def __init__(self, addons=None, node_order=None, node_pool_order=None, strategy=None, target_version=None, is_only_upgrade=None):
        r"""ClusterUpgradeAction

        The model defined in huaweicloud sdk

        :param addons: 插件配置列表
        :type addons: list[:class:`huaweicloudsdkcce.v3.UpgradeAddonConfig`]
        :param node_order: 节点池内节点升级顺序配置。 &gt; key表示节点池ID，默认节点池取值为\&quot;DefaultPool\&quot; 
        :type node_order: dict(str, list[NodePriority])
        :param node_pool_order: 节点池升级顺序配置，key/value对格式。 &gt; key表示节点池ID，默认节点池取值为\&quot;DefaultPool\&quot; &gt; value表示对应节点池的优先级，默认值为0，优先级最低，数值越大优先级越高 
        :type node_pool_order: dict(str, int)
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        :param target_version: 目标集群版本，例如\&quot;v1.23\&quot;
        :type target_version: str
        :param is_only_upgrade: 是否在集群升级流程中执行升级前检查。默认为false，表示会执行升级前检查，如果您在集群升级编排中调用了升级前检查的API，则升级时可用将该字段置为false，不再额外执行一次检查
        :type is_only_upgrade: bool
        """
        
        

        self._addons = None
        self._node_order = None
        self._node_pool_order = None
        self._strategy = None
        self._target_version = None
        self._is_only_upgrade = None
        self.discriminator = None

        if addons is not None:
            self.addons = addons
        if node_order is not None:
            self.node_order = node_order
        if node_pool_order is not None:
            self.node_pool_order = node_pool_order
        self.strategy = strategy
        self.target_version = target_version
        if is_only_upgrade is not None:
            self.is_only_upgrade = is_only_upgrade

    @property
    def addons(self):
        r"""Gets the addons of this ClusterUpgradeAction.

        插件配置列表

        :return: The addons of this ClusterUpgradeAction.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UpgradeAddonConfig`]
        """
        return self._addons

    @addons.setter
    def addons(self, addons):
        r"""Sets the addons of this ClusterUpgradeAction.

        插件配置列表

        :param addons: The addons of this ClusterUpgradeAction.
        :type addons: list[:class:`huaweicloudsdkcce.v3.UpgradeAddonConfig`]
        """
        self._addons = addons

    @property
    def node_order(self):
        r"""Gets the node_order of this ClusterUpgradeAction.

        节点池内节点升级顺序配置。 > key表示节点池ID，默认节点池取值为\"DefaultPool\" 

        :return: The node_order of this ClusterUpgradeAction.
        :rtype: dict(str, list[NodePriority])
        """
        return self._node_order

    @node_order.setter
    def node_order(self, node_order):
        r"""Sets the node_order of this ClusterUpgradeAction.

        节点池内节点升级顺序配置。 > key表示节点池ID，默认节点池取值为\"DefaultPool\" 

        :param node_order: The node_order of this ClusterUpgradeAction.
        :type node_order: dict(str, list[NodePriority])
        """
        self._node_order = node_order

    @property
    def node_pool_order(self):
        r"""Gets the node_pool_order of this ClusterUpgradeAction.

        节点池升级顺序配置，key/value对格式。 > key表示节点池ID，默认节点池取值为\"DefaultPool\" > value表示对应节点池的优先级，默认值为0，优先级最低，数值越大优先级越高 

        :return: The node_pool_order of this ClusterUpgradeAction.
        :rtype: dict(str, int)
        """
        return self._node_pool_order

    @node_pool_order.setter
    def node_pool_order(self, node_pool_order):
        r"""Sets the node_pool_order of this ClusterUpgradeAction.

        节点池升级顺序配置，key/value对格式。 > key表示节点池ID，默认节点池取值为\"DefaultPool\" > value表示对应节点池的优先级，默认值为0，优先级最低，数值越大优先级越高 

        :param node_pool_order: The node_pool_order of this ClusterUpgradeAction.
        :type node_pool_order: dict(str, int)
        """
        self._node_pool_order = node_pool_order

    @property
    def strategy(self):
        r"""Gets the strategy of this ClusterUpgradeAction.

        :return: The strategy of this ClusterUpgradeAction.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this ClusterUpgradeAction.

        :param strategy: The strategy of this ClusterUpgradeAction.
        :type strategy: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        """
        self._strategy = strategy

    @property
    def target_version(self):
        r"""Gets the target_version of this ClusterUpgradeAction.

        目标集群版本，例如\"v1.23\"

        :return: The target_version of this ClusterUpgradeAction.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ClusterUpgradeAction.

        目标集群版本，例如\"v1.23\"

        :param target_version: The target_version of this ClusterUpgradeAction.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def is_only_upgrade(self):
        r"""Gets the is_only_upgrade of this ClusterUpgradeAction.

        是否在集群升级流程中执行升级前检查。默认为false，表示会执行升级前检查，如果您在集群升级编排中调用了升级前检查的API，则升级时可用将该字段置为false，不再额外执行一次检查

        :return: The is_only_upgrade of this ClusterUpgradeAction.
        :rtype: bool
        """
        return self._is_only_upgrade

    @is_only_upgrade.setter
    def is_only_upgrade(self, is_only_upgrade):
        r"""Sets the is_only_upgrade of this ClusterUpgradeAction.

        是否在集群升级流程中执行升级前检查。默认为false，表示会执行升级前检查，如果您在集群升级编排中调用了升级前检查的API，则升级时可用将该字段置为false，不再额外执行一次检查

        :param is_only_upgrade: The is_only_upgrade of this ClusterUpgradeAction.
        :type is_only_upgrade: bool
        """
        self._is_only_upgrade = is_only_upgrade

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
        if not isinstance(other, ClusterUpgradeAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
