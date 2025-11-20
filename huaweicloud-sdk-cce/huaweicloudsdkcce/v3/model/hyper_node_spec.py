# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperNodeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'nodepool_id': 'str',
        'node_template': 'list[NodeTemplateInHyperNode]',
        'charge_mode': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'nodepool_id': 'nodepoolID',
        'node_template': 'nodeTemplate',
        'charge_mode': 'chargeMode'
    }

    def __init__(self, flavor=None, nodepool_id=None, node_template=None, charge_mode=None):
        r"""HyperNodeSpec

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**： 超节点规格
        :type flavor: str
        :param nodepool_id: **参数解释**： 所属节点池ID
        :type nodepool_id: str
        :param node_template: **参数解释**： 超节点下节点相关的配置。
        :type node_template: list[:class:`huaweicloudsdkcce.v3.NodeTemplateInHyperNode`]
        :param charge_mode: **参数解释**： 付费方式 **取值范围**： - prepaid: 预付费，即包年包月； - postpaid: 后付费，即按需付费；
        :type charge_mode: str
        """
        
        

        self._flavor = None
        self._nodepool_id = None
        self._node_template = None
        self._charge_mode = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if nodepool_id is not None:
            self.nodepool_id = nodepool_id
        if node_template is not None:
            self.node_template = node_template
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def flavor(self):
        r"""Gets the flavor of this HyperNodeSpec.

        **参数解释**： 超节点规格

        :return: The flavor of this HyperNodeSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this HyperNodeSpec.

        **参数解释**： 超节点规格

        :param flavor: The flavor of this HyperNodeSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def nodepool_id(self):
        r"""Gets the nodepool_id of this HyperNodeSpec.

        **参数解释**： 所属节点池ID

        :return: The nodepool_id of this HyperNodeSpec.
        :rtype: str
        """
        return self._nodepool_id

    @nodepool_id.setter
    def nodepool_id(self, nodepool_id):
        r"""Sets the nodepool_id of this HyperNodeSpec.

        **参数解释**： 所属节点池ID

        :param nodepool_id: The nodepool_id of this HyperNodeSpec.
        :type nodepool_id: str
        """
        self._nodepool_id = nodepool_id

    @property
    def node_template(self):
        r"""Gets the node_template of this HyperNodeSpec.

        **参数解释**： 超节点下节点相关的配置。

        :return: The node_template of this HyperNodeSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NodeTemplateInHyperNode`]
        """
        return self._node_template

    @node_template.setter
    def node_template(self, node_template):
        r"""Sets the node_template of this HyperNodeSpec.

        **参数解释**： 超节点下节点相关的配置。

        :param node_template: The node_template of this HyperNodeSpec.
        :type node_template: list[:class:`huaweicloudsdkcce.v3.NodeTemplateInHyperNode`]
        """
        self._node_template = node_template

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this HyperNodeSpec.

        **参数解释**： 付费方式 **取值范围**： - prepaid: 预付费，即包年包月； - postpaid: 后付费，即按需付费；

        :return: The charge_mode of this HyperNodeSpec.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this HyperNodeSpec.

        **参数解释**： 付费方式 **取值范围**： - prepaid: 预付费，即包年包月； - postpaid: 后付费，即按需付费；

        :param charge_mode: The charge_mode of this HyperNodeSpec.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, HyperNodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
