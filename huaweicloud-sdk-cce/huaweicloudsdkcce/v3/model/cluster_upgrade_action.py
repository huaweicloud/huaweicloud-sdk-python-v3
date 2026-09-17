# coding: utf-8

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
        'is_only_upgrade': 'bool',
        'agency_name': 'str'
    }

    attribute_map = {
        'addons': 'addons',
        'node_order': 'nodeOrder',
        'node_pool_order': 'nodePoolOrder',
        'strategy': 'strategy',
        'target_version': 'targetVersion',
        'is_only_upgrade': 'isOnlyUpgrade',
        'agency_name': 'agencyName'
    }

    def __init__(self, addons=None, node_order=None, node_pool_order=None, strategy=None, target_version=None, is_only_upgrade=None, agency_name=None):
        r"""ClusterUpgradeAction

        The model defined in huaweicloud sdk

        :param addons: **参数解释：** 插件配置列表，CCE会在集群升级过程中按照配置对插件进行升级 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type addons: list[:class:`huaweicloudsdkcce.v3.UpgradeAddonConfig`]
        :param node_order: **参数解释：** 节点池内节点升级顺序配置。key表示节点池ID，默认节点池取值为\&quot;DefaultPool\&quot; **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type node_order: dict(str, list[NodePriority])
        :param node_pool_order: **参数解释：** 节点池升级顺序配置，key/value对格式。key表示节点池ID，默认节点池取值为\&quot;DefaultPool\&quot;，value表示对应节点池的优先级，默认值为0，优先级最低，数值越大优先级越高 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type node_pool_order: dict(str, int)
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkcce.v3.UpgradeStrategy`
        :param target_version: **参数解释：** 升级的目标集群版本，例如\&quot;v1.23\&quot; **约束限制：** 只能升级到高版本，不允许填写等于或低于当前集群版本的值 **取值范围：** CCE支持的集群版本 **默认取值：** 不涉及
        :type target_version: str
        :param is_only_upgrade: **参数解释：** 是否在集群升级流程中跳过升级前检查。 **约束限制：** 不涉及 **取值范围：** - false：表示在集群升级流程中会执行升级前检查。 - true：表示在集群升级流程中跳过升级前检查。  **默认取值：** false
        :type is_only_upgrade: bool
        :param agency_name: **参数解释：** 指定集群使用的委托。该委托用于生成集群中组件使用的临时访问凭证，在集群中自动创建其他相关云服务的资源时会使用该委托权限。 当不传时，集群将优先继承原有配置，若原先未配置，则自动选择使用CCE的默认委托CCEAutoClusterAgency；当传空时，自动选择使用CCE的默认委托CCEAutoClusterAgency。  [ &gt; 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0556.html)](tag:hws) [ &gt; 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0556.html)](tag:hws_hk)  **约束限制：** 仅v1.28.15-r90、v1.29.15-r50、v1.30.14-r50、v1.31.14-r10、v1.32.9-r10、v1.33.7-r10、v1.34.3-r0及以上版本集群支持该参数 **取值范围：** 不涉及 **默认取值：** 空
        :type agency_name: str
        """
        
        

        self._addons = None
        self._node_order = None
        self._node_pool_order = None
        self._strategy = None
        self._target_version = None
        self._is_only_upgrade = None
        self._agency_name = None
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
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def addons(self):
        r"""Gets the addons of this ClusterUpgradeAction.

        **参数解释：** 插件配置列表，CCE会在集群升级过程中按照配置对插件进行升级 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The addons of this ClusterUpgradeAction.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UpgradeAddonConfig`]
        """
        return self._addons

    @addons.setter
    def addons(self, addons):
        r"""Sets the addons of this ClusterUpgradeAction.

        **参数解释：** 插件配置列表，CCE会在集群升级过程中按照配置对插件进行升级 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param addons: The addons of this ClusterUpgradeAction.
        :type addons: list[:class:`huaweicloudsdkcce.v3.UpgradeAddonConfig`]
        """
        self._addons = addons

    @property
    def node_order(self):
        r"""Gets the node_order of this ClusterUpgradeAction.

        **参数解释：** 节点池内节点升级顺序配置。key表示节点池ID，默认节点池取值为\"DefaultPool\" **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The node_order of this ClusterUpgradeAction.
        :rtype: dict(str, list[NodePriority])
        """
        return self._node_order

    @node_order.setter
    def node_order(self, node_order):
        r"""Sets the node_order of this ClusterUpgradeAction.

        **参数解释：** 节点池内节点升级顺序配置。key表示节点池ID，默认节点池取值为\"DefaultPool\" **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param node_order: The node_order of this ClusterUpgradeAction.
        :type node_order: dict(str, list[NodePriority])
        """
        self._node_order = node_order

    @property
    def node_pool_order(self):
        r"""Gets the node_pool_order of this ClusterUpgradeAction.

        **参数解释：** 节点池升级顺序配置，key/value对格式。key表示节点池ID，默认节点池取值为\"DefaultPool\"，value表示对应节点池的优先级，默认值为0，优先级最低，数值越大优先级越高 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The node_pool_order of this ClusterUpgradeAction.
        :rtype: dict(str, int)
        """
        return self._node_pool_order

    @node_pool_order.setter
    def node_pool_order(self, node_pool_order):
        r"""Sets the node_pool_order of this ClusterUpgradeAction.

        **参数解释：** 节点池升级顺序配置，key/value对格式。key表示节点池ID，默认节点池取值为\"DefaultPool\"，value表示对应节点池的优先级，默认值为0，优先级最低，数值越大优先级越高 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

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

        **参数解释：** 升级的目标集群版本，例如\"v1.23\" **约束限制：** 只能升级到高版本，不允许填写等于或低于当前集群版本的值 **取值范围：** CCE支持的集群版本 **默认取值：** 不涉及

        :return: The target_version of this ClusterUpgradeAction.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ClusterUpgradeAction.

        **参数解释：** 升级的目标集群版本，例如\"v1.23\" **约束限制：** 只能升级到高版本，不允许填写等于或低于当前集群版本的值 **取值范围：** CCE支持的集群版本 **默认取值：** 不涉及

        :param target_version: The target_version of this ClusterUpgradeAction.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def is_only_upgrade(self):
        r"""Gets the is_only_upgrade of this ClusterUpgradeAction.

        **参数解释：** 是否在集群升级流程中跳过升级前检查。 **约束限制：** 不涉及 **取值范围：** - false：表示在集群升级流程中会执行升级前检查。 - true：表示在集群升级流程中跳过升级前检查。  **默认取值：** false

        :return: The is_only_upgrade of this ClusterUpgradeAction.
        :rtype: bool
        """
        return self._is_only_upgrade

    @is_only_upgrade.setter
    def is_only_upgrade(self, is_only_upgrade):
        r"""Sets the is_only_upgrade of this ClusterUpgradeAction.

        **参数解释：** 是否在集群升级流程中跳过升级前检查。 **约束限制：** 不涉及 **取值范围：** - false：表示在集群升级流程中会执行升级前检查。 - true：表示在集群升级流程中跳过升级前检查。  **默认取值：** false

        :param is_only_upgrade: The is_only_upgrade of this ClusterUpgradeAction.
        :type is_only_upgrade: bool
        """
        self._is_only_upgrade = is_only_upgrade

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ClusterUpgradeAction.

        **参数解释：** 指定集群使用的委托。该委托用于生成集群中组件使用的临时访问凭证，在集群中自动创建其他相关云服务的资源时会使用该委托权限。 当不传时，集群将优先继承原有配置，若原先未配置，则自动选择使用CCE的默认委托CCEAutoClusterAgency；当传空时，自动选择使用CCE的默认委托CCEAutoClusterAgency。  [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0556.html)](tag:hws) [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0556.html)](tag:hws_hk)  **约束限制：** 仅v1.28.15-r90、v1.29.15-r50、v1.30.14-r50、v1.31.14-r10、v1.32.9-r10、v1.33.7-r10、v1.34.3-r0及以上版本集群支持该参数 **取值范围：** 不涉及 **默认取值：** 空

        :return: The agency_name of this ClusterUpgradeAction.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ClusterUpgradeAction.

        **参数解释：** 指定集群使用的委托。该委托用于生成集群中组件使用的临时访问凭证，在集群中自动创建其他相关云服务的资源时会使用该委托权限。 当不传时，集群将优先继承原有配置，若原先未配置，则自动选择使用CCE的默认委托CCEAutoClusterAgency；当传空时，自动选择使用CCE的默认委托CCEAutoClusterAgency。  [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/usermanual-cce/cce_10_0556.html)](tag:hws) [ > 关于CCE系统委托的说明详情参见[系统委托说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0556.html)](tag:hws_hk)  **约束限制：** 仅v1.28.15-r90、v1.29.15-r50、v1.30.14-r50、v1.31.14-r10、v1.32.9-r10、v1.33.7-r10、v1.34.3-r0及以上版本集群支持该参数 **取值范围：** 不涉及 **默认取值：** 空

        :param agency_name: The agency_name of this ClusterUpgradeAction.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, ClusterUpgradeAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
