# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'alarm_rules': 'list[AlarmRuleEntity]'
    }

    attribute_map = {
        'count': 'count',
        'alarm_rules': 'alarm_rules'
    }

    def __init__(self, count=None, alarm_rules=None):
        r"""ListAlarmRulesResponse

        The model defined in huaweicloud sdk

        :param count: 告警规则总条数
        :type count: int
        :param alarm_rules: 告警规则
        :type alarm_rules: list[:class:`huaweicloudsdkbcc.v1.AlarmRuleEntity`]
        """
        
        super(ListAlarmRulesResponse, self).__init__()

        self._count = None
        self._alarm_rules = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if alarm_rules is not None:
            self.alarm_rules = alarm_rules

    @property
    def count(self):
        r"""Gets the count of this ListAlarmRulesResponse.

        告警规则总条数

        :return: The count of this ListAlarmRulesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAlarmRulesResponse.

        告警规则总条数

        :param count: The count of this ListAlarmRulesResponse.
        :type count: int
        """
        self._count = count

    @property
    def alarm_rules(self):
        r"""Gets the alarm_rules of this ListAlarmRulesResponse.

        告警规则

        :return: The alarm_rules of this ListAlarmRulesResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.AlarmRuleEntity`]
        """
        return self._alarm_rules

    @alarm_rules.setter
    def alarm_rules(self, alarm_rules):
        r"""Sets the alarm_rules of this ListAlarmRulesResponse.

        告警规则

        :param alarm_rules: The alarm_rules of this ListAlarmRulesResponse.
        :type alarm_rules: list[:class:`huaweicloudsdkbcc.v1.AlarmRuleEntity`]
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
        if not isinstance(other, ListAlarmRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
