# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IotdaRuleAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'action_id': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'action_id': 'action_id'
    }

    def __init__(self, rule_id=None, action_id=None):
        """IotdaRuleAction

        The model defined in huaweicloud sdk

        :param rule_id: IoTDA中的规则Id
        :type rule_id: str
        :param action_id: IoTDA中推送数据动作ID
        :type action_id: str
        """
        
        

        self._rule_id = None
        self._action_id = None
        self.discriminator = None

        self.rule_id = rule_id
        self.action_id = action_id

    @property
    def rule_id(self):
        """Gets the rule_id of this IotdaRuleAction.

        IoTDA中的规则Id

        :return: The rule_id of this IotdaRuleAction.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this IotdaRuleAction.

        IoTDA中的规则Id

        :param rule_id: The rule_id of this IotdaRuleAction.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def action_id(self):
        """Gets the action_id of this IotdaRuleAction.

        IoTDA中推送数据动作ID

        :return: The action_id of this IotdaRuleAction.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this IotdaRuleAction.

        IoTDA中推送数据动作ID

        :param action_id: The action_id of this IotdaRuleAction.
        :type action_id: str
        """
        self._action_id = action_id

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
        if not isinstance(other, IotdaRuleAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
