# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmActionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_enabled': 'bool'
    }

    attribute_map = {
        'alarm_enabled': 'alarm_enabled'
    }

    def __init__(self, alarm_enabled=None):
        r"""UpdateAlarmActionRequestBody

        The model defined in huaweicloud sdk

        :param alarm_enabled: **参数解释**： 告警是否启用 **约束限制**： 不涉及 **取值范围**： - true：开启告警 - false：关闭告警 **默认取值**： 不涉及 
        :type alarm_enabled: bool
        """
        
        

        self._alarm_enabled = None
        self.discriminator = None

        self.alarm_enabled = alarm_enabled

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this UpdateAlarmActionRequestBody.

        **参数解释**： 告警是否启用 **约束限制**： 不涉及 **取值范围**： - true：开启告警 - false：关闭告警 **默认取值**： 不涉及 

        :return: The alarm_enabled of this UpdateAlarmActionRequestBody.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this UpdateAlarmActionRequestBody.

        **参数解释**： 告警是否启用 **约束限制**： 不涉及 **取值范围**： - true：开启告警 - false：关闭告警 **默认取值**： 不涉及 

        :param alarm_enabled: The alarm_enabled of this UpdateAlarmActionRequestBody.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateAlarmActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
