# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowL7RuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7policy_id': 'str',
        'l7rule_id': 'str'
    }

    attribute_map = {
        'l7policy_id': 'l7policy_id',
        'l7rule_id': 'l7rule_id'
    }

    def __init__(self, l7policy_id=None, l7rule_id=None):
        """ShowL7RuleRequest

        The model defined in huaweicloud sdk

        :param l7policy_id: 7层转发策略。
        :type l7policy_id: str
        :param l7rule_id: 7层转发规则。
        :type l7rule_id: str
        """
        
        

        self._l7policy_id = None
        self._l7rule_id = None
        self.discriminator = None

        self.l7policy_id = l7policy_id
        self.l7rule_id = l7rule_id

    @property
    def l7policy_id(self):
        """Gets the l7policy_id of this ShowL7RuleRequest.

        7层转发策略。

        :return: The l7policy_id of this ShowL7RuleRequest.
        :rtype: str
        """
        return self._l7policy_id

    @l7policy_id.setter
    def l7policy_id(self, l7policy_id):
        """Sets the l7policy_id of this ShowL7RuleRequest.

        7层转发策略。

        :param l7policy_id: The l7policy_id of this ShowL7RuleRequest.
        :type l7policy_id: str
        """
        self._l7policy_id = l7policy_id

    @property
    def l7rule_id(self):
        """Gets the l7rule_id of this ShowL7RuleRequest.

        7层转发规则。

        :return: The l7rule_id of this ShowL7RuleRequest.
        :rtype: str
        """
        return self._l7rule_id

    @l7rule_id.setter
    def l7rule_id(self, l7rule_id):
        """Sets the l7rule_id of this ShowL7RuleRequest.

        7层转发规则。

        :param l7rule_id: The l7rule_id of this ShowL7RuleRequest.
        :type l7rule_id: str
        """
        self._l7rule_id = l7rule_id

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
        if not isinstance(other, ShowL7RuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
