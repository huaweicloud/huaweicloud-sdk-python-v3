# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListActionRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_rules': 'list[ActionRule]'
    }

    attribute_map = {
        'action_rules': 'action_rules'
    }

    def __init__(self, action_rules=None):
        r"""ListActionRuleResponse

        The model defined in huaweicloud sdk

        :param action_rules: 告警行动规则列表
        :type action_rules: list[:class:`huaweicloudsdkaom.v2.ActionRule`]
        """
        
        super(ListActionRuleResponse, self).__init__()

        self._action_rules = None
        self.discriminator = None

        if action_rules is not None:
            self.action_rules = action_rules

    @property
    def action_rules(self):
        r"""Gets the action_rules of this ListActionRuleResponse.

        告警行动规则列表

        :return: The action_rules of this ListActionRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.ActionRule`]
        """
        return self._action_rules

    @action_rules.setter
    def action_rules(self, action_rules):
        r"""Sets the action_rules of this ListActionRuleResponse.

        告警行动规则列表

        :param action_rules: The action_rules of this ListActionRuleResponse.
        :type action_rules: list[:class:`huaweicloudsdkaom.v2.ActionRule`]
        """
        self._action_rules = action_rules

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
        if not isinstance(other, ListActionRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
