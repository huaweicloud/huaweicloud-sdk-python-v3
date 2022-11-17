# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateL7RuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule': 'UpdateL7RuleOption'
    }

    attribute_map = {
        'rule': 'rule'
    }

    def __init__(self, rule=None):
        """UpdateL7RuleRequestBody

        The model defined in huaweicloud sdk

        :param rule: 
        :type rule: :class:`huaweicloudsdkelb.v3.UpdateL7RuleOption`
        """
        
        

        self._rule = None
        self.discriminator = None

        self.rule = rule

    @property
    def rule(self):
        """Gets the rule of this UpdateL7RuleRequestBody.

        :return: The rule of this UpdateL7RuleRequestBody.
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateL7RuleOption`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this UpdateL7RuleRequestBody.

        :param rule: The rule of this UpdateL7RuleRequestBody.
        :type rule: :class:`huaweicloudsdkelb.v3.UpdateL7RuleOption`
        """
        self._rule = rule

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
        if not isinstance(other, UpdateL7RuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
