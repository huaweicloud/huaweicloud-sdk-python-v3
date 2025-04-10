# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDdmInstanceNodesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'subnet_id': 'str',
        'is_auto_pay': 'bool',
        'nodes': 'list[EnlargeNodeInfo]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'subnet_id': 'subnet_id',
        'is_auto_pay': 'is_auto_pay',
        'nodes': 'nodes'
    }

    def __init__(self, group_id=None, subnet_id=None, is_auto_pay=None, nodes=None):
        r"""ExpandDdmInstanceNodesRequestBody

        The model defined in huaweicloud sdk

        :param group_id: 组id，指定当前进行节点扩容的组。当实例的组&gt;1时，必填。
        :type group_id: str
        :param subnet_id: 子网ID，当组内节点的subnetId&gt;1时，必填。
        :type subnet_id: str
        :param is_auto_pay: 变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        :param nodes: 节点信息列表。最小1，最大32
        :type nodes: list[:class:`huaweicloudsdkddm.v1.EnlargeNodeInfo`]
        """
        
        

        self._group_id = None
        self._subnet_id = None
        self._is_auto_pay = None
        self._nodes = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        self.nodes = nodes

    @property
    def group_id(self):
        r"""Gets the group_id of this ExpandDdmInstanceNodesRequestBody.

        组id，指定当前进行节点扩容的组。当实例的组>1时，必填。

        :return: The group_id of this ExpandDdmInstanceNodesRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ExpandDdmInstanceNodesRequestBody.

        组id，指定当前进行节点扩容的组。当实例的组>1时，必填。

        :param group_id: The group_id of this ExpandDdmInstanceNodesRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ExpandDdmInstanceNodesRequestBody.

        子网ID，当组内节点的subnetId>1时，必填。

        :return: The subnet_id of this ExpandDdmInstanceNodesRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ExpandDdmInstanceNodesRequestBody.

        子网ID，当组内节点的subnetId>1时，必填。

        :param subnet_id: The subnet_id of this ExpandDdmInstanceNodesRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ExpandDdmInstanceNodesRequestBody.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this ExpandDdmInstanceNodesRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ExpandDdmInstanceNodesRequestBody.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this ExpandDdmInstanceNodesRequestBody.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def nodes(self):
        r"""Gets the nodes of this ExpandDdmInstanceNodesRequestBody.

        节点信息列表。最小1，最大32

        :return: The nodes of this ExpandDdmInstanceNodesRequestBody.
        :rtype: list[:class:`huaweicloudsdkddm.v1.EnlargeNodeInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ExpandDdmInstanceNodesRequestBody.

        节点信息列表。最小1，最大32

        :param nodes: The nodes of this ExpandDdmInstanceNodesRequestBody.
        :type nodes: list[:class:`huaweicloudsdkddm.v1.EnlargeNodeInfo`]
        """
        self._nodes = nodes

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
        if not isinstance(other, ExpandDdmInstanceNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
