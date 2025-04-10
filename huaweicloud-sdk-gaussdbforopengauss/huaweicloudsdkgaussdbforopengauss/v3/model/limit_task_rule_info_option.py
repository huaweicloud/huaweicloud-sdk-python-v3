# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LimitTaskRuleInfoOption:

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
        'rule_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'rule_id': 'rule_id',
        'status': 'status'
    }

    def __init__(self, node_id=None, rule_id=None, status=None):
        r"""LimitTaskRuleInfoOption

        The model defined in huaweicloud sdk

        :param node_id: 节点id。
        :type node_id: str
        :param rule_id: 规则id。
        :type rule_id: str
        :param status: 状态，当前支持：CREATING，UPDATEING，DELETING，WAIT_EXCUTE，EXCUTING，TIME_OVER，DELETED，CREATE_FAILED，UPDATE_FAILED，DELETE_FAILED，EXCEPTION。
        :type status: str
        """
        
        

        self._node_id = None
        self._rule_id = None
        self._status = None
        self.discriminator = None

        self.node_id = node_id
        self.rule_id = rule_id
        self.status = status

    @property
    def node_id(self):
        r"""Gets the node_id of this LimitTaskRuleInfoOption.

        节点id。

        :return: The node_id of this LimitTaskRuleInfoOption.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this LimitTaskRuleInfoOption.

        节点id。

        :param node_id: The node_id of this LimitTaskRuleInfoOption.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this LimitTaskRuleInfoOption.

        规则id。

        :return: The rule_id of this LimitTaskRuleInfoOption.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this LimitTaskRuleInfoOption.

        规则id。

        :param rule_id: The rule_id of this LimitTaskRuleInfoOption.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def status(self):
        r"""Gets the status of this LimitTaskRuleInfoOption.

        状态，当前支持：CREATING，UPDATEING，DELETING，WAIT_EXCUTE，EXCUTING，TIME_OVER，DELETED，CREATE_FAILED，UPDATE_FAILED，DELETE_FAILED，EXCEPTION。

        :return: The status of this LimitTaskRuleInfoOption.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LimitTaskRuleInfoOption.

        状态，当前支持：CREATING，UPDATEING，DELETING，WAIT_EXCUTE，EXCUTING，TIME_OVER，DELETED，CREATE_FAILED，UPDATE_FAILED，DELETE_FAILED，EXCEPTION。

        :param status: The status of this LimitTaskRuleInfoOption.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, LimitTaskRuleInfoOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
