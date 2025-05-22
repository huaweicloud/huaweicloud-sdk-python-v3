# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolSpecUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_template': 'NodeSpecUpdate',
        'initial_node_count': 'int',
        'ignore_initial_node_count': 'bool',
        'autoscaling': 'NodePoolNodeAutoscaling',
        'node_management_update': 'NodeManagement',
        'taint_policy_on_existing_nodes': 'str',
        'label_policy_on_existing_nodes': 'str',
        'user_tags_policy_on_existing_nodes': 'str',
        'extension_scale_groups': 'list[ExtensionScaleGroup]'
    }

    attribute_map = {
        'node_template': 'nodeTemplate',
        'initial_node_count': 'initialNodeCount',
        'ignore_initial_node_count': 'ignoreInitialNodeCount',
        'autoscaling': 'autoscaling',
        'node_management_update': 'nodeManagementUpdate',
        'taint_policy_on_existing_nodes': 'taintPolicyOnExistingNodes',
        'label_policy_on_existing_nodes': 'labelPolicyOnExistingNodes',
        'user_tags_policy_on_existing_nodes': 'userTagsPolicyOnExistingNodes',
        'extension_scale_groups': 'extensionScaleGroups'
    }

    def __init__(self, node_template=None, initial_node_count=None, ignore_initial_node_count=None, autoscaling=None, node_management_update=None, taint_policy_on_existing_nodes=None, label_policy_on_existing_nodes=None, user_tags_policy_on_existing_nodes=None, extension_scale_groups=None):
        r"""NodePoolSpecUpdate

        The model defined in huaweicloud sdk

        :param node_template: 
        :type node_template: :class:`huaweicloudsdkcce.v3.NodeSpecUpdate`
        :param initial_node_count: **参数解释：** 节点池期望节点个数。 **约束限制：** 更新节点池时，此字段为必填字段。 &gt; 注意：如果更新节点池时不填此字段，节点池期望节点个数将取默认值0，如果此时节点池节点个数大于0将导致节点池缩容。  **取值范围：** 大于0，小于集群节点规模。 **默认取值：** 0
        :type initial_node_count: int
        :param ignore_initial_node_count: **参数解释：** 该参数用于控制更新节点池时 **节点池期望节点个数(spec.initialNodeCount)** 的默认行为。当该参数未设置或者为false时，如果用户请求Body体中未设置spec.initialNodeCount，更新时将自动初始化spec.initialNodeCount为0。当该参数为true时，将忽略spec.initialNodeCount参数。 &gt; 当用户不需要更新节点池spec.initialNodeCount时，必须显示的设置该参数为true，同时在更新节点池Body体中不设置spec.initialNodeCount。  **约束限制：** 不涉及 **取值范围：** - false：更新节点池时，如果spec.initialNodeCount参数未设置，将初始化spec.initialNodeCount为0。 &gt; 如果节点池当前spec.initialNodeCount 不等于0将导致节点池缩容。  - true：更新节点池时，忽略spec.initialNodeCount参数，节点池spec.initialNodeCount参数将保持原样。  **默认取值：** false
        :type ignore_initial_node_count: bool
        :param autoscaling: 
        :type autoscaling: :class:`huaweicloudsdkcce.v3.NodePoolNodeAutoscaling`
        :param node_management_update: 
        :type node_management_update: :class:`huaweicloudsdkcce.v3.NodeManagement`
        :param taint_policy_on_existing_nodes: **参数解释：** 是否同步K8S污点。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，K8S污点的改动将会被同步更新到存量节点上。 - 填写为ignore，节点池K8S污点将不会同步更新到存量节点上。  **默认取值：** 无
        :type taint_policy_on_existing_nodes: str
        :param label_policy_on_existing_nodes: **参数解释：** 是否同步K8S标签。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，K8S标签的改动将会被同步更新到存量节点上。 - 填写为ignore，K8S标签将不会同步更新到存量节点上。  **默认取值：** 无
        :type label_policy_on_existing_nodes: str
        :param user_tags_policy_on_existing_nodes: **参数解释：** 是否同步节点池资源标签。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，节点池资源标签标签的改动将会被同步更新到存量节点上。 - 填写为ignore，节点池资源标签标签将不会同步更新到存量节点上。  **默认取值：** 无
        :type user_tags_policy_on_existing_nodes: str
        :param extension_scale_groups: 节点池扩展伸缩组配置列表，详情参见ExtensionScaleGroup类型定义
        :type extension_scale_groups: list[:class:`huaweicloudsdkcce.v3.ExtensionScaleGroup`]
        """
        
        

        self._node_template = None
        self._initial_node_count = None
        self._ignore_initial_node_count = None
        self._autoscaling = None
        self._node_management_update = None
        self._taint_policy_on_existing_nodes = None
        self._label_policy_on_existing_nodes = None
        self._user_tags_policy_on_existing_nodes = None
        self._extension_scale_groups = None
        self.discriminator = None

        if node_template is not None:
            self.node_template = node_template
        self.initial_node_count = initial_node_count
        if ignore_initial_node_count is not None:
            self.ignore_initial_node_count = ignore_initial_node_count
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if node_management_update is not None:
            self.node_management_update = node_management_update
        if taint_policy_on_existing_nodes is not None:
            self.taint_policy_on_existing_nodes = taint_policy_on_existing_nodes
        if label_policy_on_existing_nodes is not None:
            self.label_policy_on_existing_nodes = label_policy_on_existing_nodes
        if user_tags_policy_on_existing_nodes is not None:
            self.user_tags_policy_on_existing_nodes = user_tags_policy_on_existing_nodes
        if extension_scale_groups is not None:
            self.extension_scale_groups = extension_scale_groups

    @property
    def node_template(self):
        r"""Gets the node_template of this NodePoolSpecUpdate.

        :return: The node_template of this NodePoolSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSpecUpdate`
        """
        return self._node_template

    @node_template.setter
    def node_template(self, node_template):
        r"""Sets the node_template of this NodePoolSpecUpdate.

        :param node_template: The node_template of this NodePoolSpecUpdate.
        :type node_template: :class:`huaweicloudsdkcce.v3.NodeSpecUpdate`
        """
        self._node_template = node_template

    @property
    def initial_node_count(self):
        r"""Gets the initial_node_count of this NodePoolSpecUpdate.

        **参数解释：** 节点池期望节点个数。 **约束限制：** 更新节点池时，此字段为必填字段。 > 注意：如果更新节点池时不填此字段，节点池期望节点个数将取默认值0，如果此时节点池节点个数大于0将导致节点池缩容。  **取值范围：** 大于0，小于集群节点规模。 **默认取值：** 0

        :return: The initial_node_count of this NodePoolSpecUpdate.
        :rtype: int
        """
        return self._initial_node_count

    @initial_node_count.setter
    def initial_node_count(self, initial_node_count):
        r"""Sets the initial_node_count of this NodePoolSpecUpdate.

        **参数解释：** 节点池期望节点个数。 **约束限制：** 更新节点池时，此字段为必填字段。 > 注意：如果更新节点池时不填此字段，节点池期望节点个数将取默认值0，如果此时节点池节点个数大于0将导致节点池缩容。  **取值范围：** 大于0，小于集群节点规模。 **默认取值：** 0

        :param initial_node_count: The initial_node_count of this NodePoolSpecUpdate.
        :type initial_node_count: int
        """
        self._initial_node_count = initial_node_count

    @property
    def ignore_initial_node_count(self):
        r"""Gets the ignore_initial_node_count of this NodePoolSpecUpdate.

        **参数解释：** 该参数用于控制更新节点池时 **节点池期望节点个数(spec.initialNodeCount)** 的默认行为。当该参数未设置或者为false时，如果用户请求Body体中未设置spec.initialNodeCount，更新时将自动初始化spec.initialNodeCount为0。当该参数为true时，将忽略spec.initialNodeCount参数。 > 当用户不需要更新节点池spec.initialNodeCount时，必须显示的设置该参数为true，同时在更新节点池Body体中不设置spec.initialNodeCount。  **约束限制：** 不涉及 **取值范围：** - false：更新节点池时，如果spec.initialNodeCount参数未设置，将初始化spec.initialNodeCount为0。 > 如果节点池当前spec.initialNodeCount 不等于0将导致节点池缩容。  - true：更新节点池时，忽略spec.initialNodeCount参数，节点池spec.initialNodeCount参数将保持原样。  **默认取值：** false

        :return: The ignore_initial_node_count of this NodePoolSpecUpdate.
        :rtype: bool
        """
        return self._ignore_initial_node_count

    @ignore_initial_node_count.setter
    def ignore_initial_node_count(self, ignore_initial_node_count):
        r"""Sets the ignore_initial_node_count of this NodePoolSpecUpdate.

        **参数解释：** 该参数用于控制更新节点池时 **节点池期望节点个数(spec.initialNodeCount)** 的默认行为。当该参数未设置或者为false时，如果用户请求Body体中未设置spec.initialNodeCount，更新时将自动初始化spec.initialNodeCount为0。当该参数为true时，将忽略spec.initialNodeCount参数。 > 当用户不需要更新节点池spec.initialNodeCount时，必须显示的设置该参数为true，同时在更新节点池Body体中不设置spec.initialNodeCount。  **约束限制：** 不涉及 **取值范围：** - false：更新节点池时，如果spec.initialNodeCount参数未设置，将初始化spec.initialNodeCount为0。 > 如果节点池当前spec.initialNodeCount 不等于0将导致节点池缩容。  - true：更新节点池时，忽略spec.initialNodeCount参数，节点池spec.initialNodeCount参数将保持原样。  **默认取值：** false

        :param ignore_initial_node_count: The ignore_initial_node_count of this NodePoolSpecUpdate.
        :type ignore_initial_node_count: bool
        """
        self._ignore_initial_node_count = ignore_initial_node_count

    @property
    def autoscaling(self):
        r"""Gets the autoscaling of this NodePoolSpecUpdate.

        :return: The autoscaling of this NodePoolSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodePoolNodeAutoscaling`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        r"""Sets the autoscaling of this NodePoolSpecUpdate.

        :param autoscaling: The autoscaling of this NodePoolSpecUpdate.
        :type autoscaling: :class:`huaweicloudsdkcce.v3.NodePoolNodeAutoscaling`
        """
        self._autoscaling = autoscaling

    @property
    def node_management_update(self):
        r"""Gets the node_management_update of this NodePoolSpecUpdate.

        :return: The node_management_update of this NodePoolSpecUpdate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeManagement`
        """
        return self._node_management_update

    @node_management_update.setter
    def node_management_update(self, node_management_update):
        r"""Sets the node_management_update of this NodePoolSpecUpdate.

        :param node_management_update: The node_management_update of this NodePoolSpecUpdate.
        :type node_management_update: :class:`huaweicloudsdkcce.v3.NodeManagement`
        """
        self._node_management_update = node_management_update

    @property
    def taint_policy_on_existing_nodes(self):
        r"""Gets the taint_policy_on_existing_nodes of this NodePoolSpecUpdate.

        **参数解释：** 是否同步K8S污点。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，K8S污点的改动将会被同步更新到存量节点上。 - 填写为ignore，节点池K8S污点将不会同步更新到存量节点上。  **默认取值：** 无

        :return: The taint_policy_on_existing_nodes of this NodePoolSpecUpdate.
        :rtype: str
        """
        return self._taint_policy_on_existing_nodes

    @taint_policy_on_existing_nodes.setter
    def taint_policy_on_existing_nodes(self, taint_policy_on_existing_nodes):
        r"""Sets the taint_policy_on_existing_nodes of this NodePoolSpecUpdate.

        **参数解释：** 是否同步K8S污点。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，K8S污点的改动将会被同步更新到存量节点上。 - 填写为ignore，节点池K8S污点将不会同步更新到存量节点上。  **默认取值：** 无

        :param taint_policy_on_existing_nodes: The taint_policy_on_existing_nodes of this NodePoolSpecUpdate.
        :type taint_policy_on_existing_nodes: str
        """
        self._taint_policy_on_existing_nodes = taint_policy_on_existing_nodes

    @property
    def label_policy_on_existing_nodes(self):
        r"""Gets the label_policy_on_existing_nodes of this NodePoolSpecUpdate.

        **参数解释：** 是否同步K8S标签。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，K8S标签的改动将会被同步更新到存量节点上。 - 填写为ignore，K8S标签将不会同步更新到存量节点上。  **默认取值：** 无

        :return: The label_policy_on_existing_nodes of this NodePoolSpecUpdate.
        :rtype: str
        """
        return self._label_policy_on_existing_nodes

    @label_policy_on_existing_nodes.setter
    def label_policy_on_existing_nodes(self, label_policy_on_existing_nodes):
        r"""Sets the label_policy_on_existing_nodes of this NodePoolSpecUpdate.

        **参数解释：** 是否同步K8S标签。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，K8S标签的改动将会被同步更新到存量节点上。 - 填写为ignore，K8S标签将不会同步更新到存量节点上。  **默认取值：** 无

        :param label_policy_on_existing_nodes: The label_policy_on_existing_nodes of this NodePoolSpecUpdate.
        :type label_policy_on_existing_nodes: str
        """
        self._label_policy_on_existing_nodes = label_policy_on_existing_nodes

    @property
    def user_tags_policy_on_existing_nodes(self):
        r"""Gets the user_tags_policy_on_existing_nodes of this NodePoolSpecUpdate.

        **参数解释：** 是否同步节点池资源标签。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，节点池资源标签标签的改动将会被同步更新到存量节点上。 - 填写为ignore，节点池资源标签标签将不会同步更新到存量节点上。  **默认取值：** 无

        :return: The user_tags_policy_on_existing_nodes of this NodePoolSpecUpdate.
        :rtype: str
        """
        return self._user_tags_policy_on_existing_nodes

    @user_tags_policy_on_existing_nodes.setter
    def user_tags_policy_on_existing_nodes(self, user_tags_policy_on_existing_nodes):
        r"""Sets the user_tags_policy_on_existing_nodes of this NodePoolSpecUpdate.

        **参数解释：** 是否同步节点池资源标签。 **约束限制**： 不涉及 **取值范围：** - 填写为refresh，节点池资源标签标签的改动将会被同步更新到存量节点上。 - 填写为ignore，节点池资源标签标签将不会同步更新到存量节点上。  **默认取值：** 无

        :param user_tags_policy_on_existing_nodes: The user_tags_policy_on_existing_nodes of this NodePoolSpecUpdate.
        :type user_tags_policy_on_existing_nodes: str
        """
        self._user_tags_policy_on_existing_nodes = user_tags_policy_on_existing_nodes

    @property
    def extension_scale_groups(self):
        r"""Gets the extension_scale_groups of this NodePoolSpecUpdate.

        节点池扩展伸缩组配置列表，详情参见ExtensionScaleGroup类型定义

        :return: The extension_scale_groups of this NodePoolSpecUpdate.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ExtensionScaleGroup`]
        """
        return self._extension_scale_groups

    @extension_scale_groups.setter
    def extension_scale_groups(self, extension_scale_groups):
        r"""Sets the extension_scale_groups of this NodePoolSpecUpdate.

        节点池扩展伸缩组配置列表，详情参见ExtensionScaleGroup类型定义

        :param extension_scale_groups: The extension_scale_groups of this NodePoolSpecUpdate.
        :type extension_scale_groups: list[:class:`huaweicloudsdkcce.v3.ExtensionScaleGroup`]
        """
        self._extension_scale_groups = extension_scale_groups

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
        if not isinstance(other, NodePoolSpecUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
