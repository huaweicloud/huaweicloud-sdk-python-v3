# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchEnableAlarmPoliciesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_policy_ids': 'list[str]',
        'enabled': 'bool'
    }

    attribute_map = {
        'alarm_policy_ids': 'alarm_policy_ids',
        'enabled': 'enabled'
    }

    def __init__(self, alarm_policy_ids=None, enabled=None):
        """BatchEnableAlarmPoliciesRequestBody

        The model defined in huaweicloud sdk

        :param alarm_policy_ids: 需要批量启停的告警规则策略的ID列表
        :type alarm_policy_ids: list[str]
        :param enabled: 开关
        :type enabled: bool
        """
        
        

        self._alarm_policy_ids = None
        self._enabled = None
        self.discriminator = None

        self.alarm_policy_ids = alarm_policy_ids
        self.enabled = enabled

    @property
    def alarm_policy_ids(self):
        """Gets the alarm_policy_ids of this BatchEnableAlarmPoliciesRequestBody.

        需要批量启停的告警规则策略的ID列表

        :return: The alarm_policy_ids of this BatchEnableAlarmPoliciesRequestBody.
        :rtype: list[str]
        """
        return self._alarm_policy_ids

    @alarm_policy_ids.setter
    def alarm_policy_ids(self, alarm_policy_ids):
        """Sets the alarm_policy_ids of this BatchEnableAlarmPoliciesRequestBody.

        需要批量启停的告警规则策略的ID列表

        :param alarm_policy_ids: The alarm_policy_ids of this BatchEnableAlarmPoliciesRequestBody.
        :type alarm_policy_ids: list[str]
        """
        self._alarm_policy_ids = alarm_policy_ids

    @property
    def enabled(self):
        """Gets the enabled of this BatchEnableAlarmPoliciesRequestBody.

        开关

        :return: The enabled of this BatchEnableAlarmPoliciesRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BatchEnableAlarmPoliciesRequestBody.

        开关

        :param enabled: The enabled of this BatchEnableAlarmPoliciesRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, BatchEnableAlarmPoliciesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
