# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSqlFilterRuleInfo:

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
        'rules': 'list[NodeSqlFilterRule]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'rules': 'rules'
    }

    def __init__(self, node_id=None, rules=None):
        r"""NodeSqlFilterRuleInfo

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param rules: SQL限流规则。集合的sql_type值不能重复。
        :type rules: list[:class:`huaweicloudsdkgaussdb.v3.NodeSqlFilterRule`]
        """
        
        

        self._node_id = None
        self._rules = None
        self.discriminator = None

        self.node_id = node_id
        self.rules = rules

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeSqlFilterRuleInfo.

        节点ID

        :return: The node_id of this NodeSqlFilterRuleInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeSqlFilterRuleInfo.

        节点ID

        :param node_id: The node_id of this NodeSqlFilterRuleInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def rules(self):
        r"""Gets the rules of this NodeSqlFilterRuleInfo.

        SQL限流规则。集合的sql_type值不能重复。

        :return: The rules of this NodeSqlFilterRuleInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.NodeSqlFilterRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this NodeSqlFilterRuleInfo.

        SQL限流规则。集合的sql_type值不能重复。

        :param rules: The rules of this NodeSqlFilterRuleInfo.
        :type rules: list[:class:`huaweicloudsdkgaussdb.v3.NodeSqlFilterRule`]
        """
        self._rules = rules

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
        if not isinstance(other, NodeSqlFilterRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
