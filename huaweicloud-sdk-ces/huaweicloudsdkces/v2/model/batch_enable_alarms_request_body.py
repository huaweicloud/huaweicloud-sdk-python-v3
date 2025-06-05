# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchEnableAlarmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_ids': 'list[str]',
        'alarm_enabled': 'bool'
    }

    attribute_map = {
        'alarm_ids': 'alarm_ids',
        'alarm_enabled': 'alarm_enabled'
    }

    def __init__(self, alarm_ids=None, alarm_enabled=None):
        r"""BatchEnableAlarmsRequestBody

        The model defined in huaweicloud sdk

        :param alarm_ids: 需要批量启停的告警规则的ID列表
        :type alarm_ids: list[str]
        :param alarm_enabled: 是否开启告警规则。true:开启，false:关闭。
        :type alarm_enabled: bool
        """
        
        

        self._alarm_ids = None
        self._alarm_enabled = None
        self.discriminator = None

        self.alarm_ids = alarm_ids
        self.alarm_enabled = alarm_enabled

    @property
    def alarm_ids(self):
        r"""Gets the alarm_ids of this BatchEnableAlarmsRequestBody.

        需要批量启停的告警规则的ID列表

        :return: The alarm_ids of this BatchEnableAlarmsRequestBody.
        :rtype: list[str]
        """
        return self._alarm_ids

    @alarm_ids.setter
    def alarm_ids(self, alarm_ids):
        r"""Sets the alarm_ids of this BatchEnableAlarmsRequestBody.

        需要批量启停的告警规则的ID列表

        :param alarm_ids: The alarm_ids of this BatchEnableAlarmsRequestBody.
        :type alarm_ids: list[str]
        """
        self._alarm_ids = alarm_ids

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this BatchEnableAlarmsRequestBody.

        是否开启告警规则。true:开启，false:关闭。

        :return: The alarm_enabled of this BatchEnableAlarmsRequestBody.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this BatchEnableAlarmsRequestBody.

        是否开启告警规则。true:开启，false:关闭。

        :param alarm_enabled: The alarm_enabled of this BatchEnableAlarmsRequestBody.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

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
        if not isinstance(other, BatchEnableAlarmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
