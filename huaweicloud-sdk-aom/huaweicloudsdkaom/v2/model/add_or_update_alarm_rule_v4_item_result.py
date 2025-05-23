# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOrUpdateAlarmRuleV4ItemResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_name': 'str',
        'result': 'str'
    }

    attribute_map = {
        'alarm_rule_name': 'alarm_rule_name',
        'result': 'result'
    }

    def __init__(self, alarm_rule_name=None, result=None):
        r"""AddOrUpdateAlarmRuleV4ItemResult

        The model defined in huaweicloud sdk

        :param alarm_rule_name: 告警规则名称。
        :type alarm_rule_name: str
        :param result: 告警规则新增或修改结果。
        :type result: str
        """
        
        

        self._alarm_rule_name = None
        self._result = None
        self.discriminator = None

        self.alarm_rule_name = alarm_rule_name
        self.result = result

    @property
    def alarm_rule_name(self):
        r"""Gets the alarm_rule_name of this AddOrUpdateAlarmRuleV4ItemResult.

        告警规则名称。

        :return: The alarm_rule_name of this AddOrUpdateAlarmRuleV4ItemResult.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        r"""Sets the alarm_rule_name of this AddOrUpdateAlarmRuleV4ItemResult.

        告警规则名称。

        :param alarm_rule_name: The alarm_rule_name of this AddOrUpdateAlarmRuleV4ItemResult.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def result(self):
        r"""Gets the result of this AddOrUpdateAlarmRuleV4ItemResult.

        告警规则新增或修改结果。

        :return: The result of this AddOrUpdateAlarmRuleV4ItemResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this AddOrUpdateAlarmRuleV4ItemResult.

        告警规则新增或修改结果。

        :param result: The result of this AddOrUpdateAlarmRuleV4ItemResult.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, AddOrUpdateAlarmRuleV4ItemResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
