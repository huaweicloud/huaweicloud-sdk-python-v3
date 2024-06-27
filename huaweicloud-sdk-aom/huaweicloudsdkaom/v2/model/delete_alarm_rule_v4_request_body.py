# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAlarmRuleV4RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rules': 'list[str]'
    }

    attribute_map = {
        'alarm_rules': 'alarm_rules'
    }

    def __init__(self, alarm_rules=None):
        """DeleteAlarmRuleV4RequestBody

        The model defined in huaweicloud sdk

        :param alarm_rules: 告警规则名称列表。
        :type alarm_rules: list[str]
        """
        
        

        self._alarm_rules = None
        self.discriminator = None

        self.alarm_rules = alarm_rules

    @property
    def alarm_rules(self):
        """Gets the alarm_rules of this DeleteAlarmRuleV4RequestBody.

        告警规则名称列表。

        :return: The alarm_rules of this DeleteAlarmRuleV4RequestBody.
        :rtype: list[str]
        """
        return self._alarm_rules

    @alarm_rules.setter
    def alarm_rules(self, alarm_rules):
        """Sets the alarm_rules of this DeleteAlarmRuleV4RequestBody.

        告警规则名称列表。

        :param alarm_rules: The alarm_rules of this DeleteAlarmRuleV4RequestBody.
        :type alarm_rules: list[str]
        """
        self._alarm_rules = alarm_rules

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
        if not isinstance(other, DeleteAlarmRuleV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
