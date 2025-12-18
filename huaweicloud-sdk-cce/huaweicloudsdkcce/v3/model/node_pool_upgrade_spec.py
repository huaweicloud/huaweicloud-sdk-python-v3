# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolUpgradeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_unavailable': 'int',
        'force': 'bool',
        'retry_times': 'int',
        'skipped_nodes': 'list[str]',
        'node_i_ds': 'list[str]',
        'node_pool_id': 'str',
        'node_template': 'NodeTemplate'
    }

    attribute_map = {
        'max_unavailable': 'maxUnavailable',
        'force': 'force',
        'retry_times': 'retryTimes',
        'skipped_nodes': 'skippedNodes',
        'node_i_ds': 'nodeIDs',
        'node_pool_id': 'nodePoolID',
        'node_template': 'nodeTemplate'
    }

    def __init__(self, max_unavailable=None, force=None, retry_times=None, skipped_nodes=None, node_i_ds=None, node_pool_id=None, node_template=None):
        r"""NodePoolUpgradeSpec

        The model defined in huaweicloud sdk

        :param max_unavailable: **参数解释**： 每批最大同步节点。节点升级时，允许节点不可用的最大数量。节点重置方式进行同步时节点将不可用，请合理设置该参数，尽量避免出现集群节点不可用数量过多导致Pod无法调度的情况。 **约束限制**： 不涉及 **取值范围**： 取值范围[1-20] **默认取值**： 不涉及 
        :type max_unavailable: int
        :param force: Pod无法驱逐时，是否强制重置。
        :type force: bool
        :param retry_times: 
        :type retry_times: int
        :param skipped_nodes: 
        :type skipped_nodes: list[str]
        :param node_i_ds: **参数解释**： 本次操作同步的节点池中选择的节点ID列表，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type node_i_ds: list[str]
        :param node_pool_id: **参数解释**： 节点池ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type node_pool_id: str
        :param node_template: 
        :type node_template: :class:`huaweicloudsdkcce.v3.NodeTemplate`
        """
        
        

        self._max_unavailable = None
        self._force = None
        self._retry_times = None
        self._skipped_nodes = None
        self._node_i_ds = None
        self._node_pool_id = None
        self._node_template = None
        self.discriminator = None

        if max_unavailable is not None:
            self.max_unavailable = max_unavailable
        if force is not None:
            self.force = force
        if retry_times is not None:
            self.retry_times = retry_times
        if skipped_nodes is not None:
            self.skipped_nodes = skipped_nodes
        if node_i_ds is not None:
            self.node_i_ds = node_i_ds
        self.node_pool_id = node_pool_id
        if node_template is not None:
            self.node_template = node_template

    @property
    def max_unavailable(self):
        r"""Gets the max_unavailable of this NodePoolUpgradeSpec.

        **参数解释**： 每批最大同步节点。节点升级时，允许节点不可用的最大数量。节点重置方式进行同步时节点将不可用，请合理设置该参数，尽量避免出现集群节点不可用数量过多导致Pod无法调度的情况。 **约束限制**： 不涉及 **取值范围**： 取值范围[1-20] **默认取值**： 不涉及 

        :return: The max_unavailable of this NodePoolUpgradeSpec.
        :rtype: int
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        r"""Sets the max_unavailable of this NodePoolUpgradeSpec.

        **参数解释**： 每批最大同步节点。节点升级时，允许节点不可用的最大数量。节点重置方式进行同步时节点将不可用，请合理设置该参数，尽量避免出现集群节点不可用数量过多导致Pod无法调度的情况。 **约束限制**： 不涉及 **取值范围**： 取值范围[1-20] **默认取值**： 不涉及 

        :param max_unavailable: The max_unavailable of this NodePoolUpgradeSpec.
        :type max_unavailable: int
        """
        self._max_unavailable = max_unavailable

    @property
    def force(self):
        r"""Gets the force of this NodePoolUpgradeSpec.

        Pod无法驱逐时，是否强制重置。

        :return: The force of this NodePoolUpgradeSpec.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this NodePoolUpgradeSpec.

        Pod无法驱逐时，是否强制重置。

        :param force: The force of this NodePoolUpgradeSpec.
        :type force: bool
        """
        self._force = force

    @property
    def retry_times(self):
        r"""Gets the retry_times of this NodePoolUpgradeSpec.

        :return: The retry_times of this NodePoolUpgradeSpec.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this NodePoolUpgradeSpec.

        :param retry_times: The retry_times of this NodePoolUpgradeSpec.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def skipped_nodes(self):
        r"""Gets the skipped_nodes of this NodePoolUpgradeSpec.

        :return: The skipped_nodes of this NodePoolUpgradeSpec.
        :rtype: list[str]
        """
        return self._skipped_nodes

    @skipped_nodes.setter
    def skipped_nodes(self, skipped_nodes):
        r"""Sets the skipped_nodes of this NodePoolUpgradeSpec.

        :param skipped_nodes: The skipped_nodes of this NodePoolUpgradeSpec.
        :type skipped_nodes: list[str]
        """
        self._skipped_nodes = skipped_nodes

    @property
    def node_i_ds(self):
        r"""Gets the node_i_ds of this NodePoolUpgradeSpec.

        **参数解释**： 本次操作同步的节点池中选择的节点ID列表，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The node_i_ds of this NodePoolUpgradeSpec.
        :rtype: list[str]
        """
        return self._node_i_ds

    @node_i_ds.setter
    def node_i_ds(self, node_i_ds):
        r"""Sets the node_i_ds of this NodePoolUpgradeSpec.

        **参数解释**： 本次操作同步的节点池中选择的节点ID列表，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param node_i_ds: The node_i_ds of this NodePoolUpgradeSpec.
        :type node_i_ds: list[str]
        """
        self._node_i_ds = node_i_ds

    @property
    def node_pool_id(self):
        r"""Gets the node_pool_id of this NodePoolUpgradeSpec.

        **参数解释**： 节点池ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The node_pool_id of this NodePoolUpgradeSpec.
        :rtype: str
        """
        return self._node_pool_id

    @node_pool_id.setter
    def node_pool_id(self, node_pool_id):
        r"""Sets the node_pool_id of this NodePoolUpgradeSpec.

        **参数解释**： 节点池ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param node_pool_id: The node_pool_id of this NodePoolUpgradeSpec.
        :type node_pool_id: str
        """
        self._node_pool_id = node_pool_id

    @property
    def node_template(self):
        r"""Gets the node_template of this NodePoolUpgradeSpec.

        :return: The node_template of this NodePoolUpgradeSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeTemplate`
        """
        return self._node_template

    @node_template.setter
    def node_template(self, node_template):
        r"""Sets the node_template of this NodePoolUpgradeSpec.

        :param node_template: The node_template of this NodePoolUpgradeSpec.
        :type node_template: :class:`huaweicloudsdkcce.v3.NodeTemplate`
        """
        self._node_template = node_template

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
        if not isinstance(other, NodePoolUpgradeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
