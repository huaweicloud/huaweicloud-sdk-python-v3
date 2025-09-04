# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapNodeInfoResponseBodyNodeList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'node_name': 'str',
        'role': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'role': 'role'
    }

    def __init__(self, node_id=None, node_name=None, role=None):
        r"""HtapNodeInfoResponseBodyNodeList

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**： HTAP标准版实例节点ID。  **取值范围**：  不涉及。
        :type node_id: str
        :param node_name: **参数解释**： HTAP标准版实例节点名称。  **取值范围**：  不涉及。
        :type node_name: str
        :param role: **参数解释**： HTAP标准版实例节点角色。  **取值范围**： - fe-leader - fe-follower - fe-observer - be
        :type role: str
        """
        
        

        self._node_id = None
        self._node_name = None
        self._role = None
        self.discriminator = None

        self.node_id = node_id
        self.node_name = node_name
        self.role = role

    @property
    def node_id(self):
        r"""Gets the node_id of this HtapNodeInfoResponseBodyNodeList.

        **参数解释**： HTAP标准版实例节点ID。  **取值范围**：  不涉及。

        :return: The node_id of this HtapNodeInfoResponseBodyNodeList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this HtapNodeInfoResponseBodyNodeList.

        **参数解释**： HTAP标准版实例节点ID。  **取值范围**：  不涉及。

        :param node_id: The node_id of this HtapNodeInfoResponseBodyNodeList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this HtapNodeInfoResponseBodyNodeList.

        **参数解释**： HTAP标准版实例节点名称。  **取值范围**：  不涉及。

        :return: The node_name of this HtapNodeInfoResponseBodyNodeList.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this HtapNodeInfoResponseBodyNodeList.

        **参数解释**： HTAP标准版实例节点名称。  **取值范围**：  不涉及。

        :param node_name: The node_name of this HtapNodeInfoResponseBodyNodeList.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def role(self):
        r"""Gets the role of this HtapNodeInfoResponseBodyNodeList.

        **参数解释**： HTAP标准版实例节点角色。  **取值范围**： - fe-leader - fe-follower - fe-observer - be

        :return: The role of this HtapNodeInfoResponseBodyNodeList.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this HtapNodeInfoResponseBodyNodeList.

        **参数解释**： HTAP标准版实例节点角色。  **取值范围**： - fe-leader - fe-follower - fe-observer - be

        :param role: The role of this HtapNodeInfoResponseBodyNodeList.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, HtapNodeInfoResponseBodyNodeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
