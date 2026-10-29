# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_expression': 'str',
        'alarm_level': 'str'
    }

    attribute_map = {
        'condition_expression': 'condition_expression',
        'alarm_level': 'alarm_level'
    }

    def __init__(self, condition_expression=None, alarm_level=None):
        r"""AlarmCondition

        The model defined in huaweicloud sdk

        :param condition_expression: **参数解释：** 触发告警的条件表达式。 **约束限制：** - 不支持纯数字。 - 不支持以数字开头的。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type condition_expression: str
        :param alarm_level: **参数解释：** 触发的告警级别。 **约束限制：** 不支持纯数字，不支持以数字开头的。 **取值范围：** - Info：提示 - Minor：次要 - Major：重要 - Critical：紧急 **默认取值：** 不涉及。
        :type alarm_level: str
        """
        
        

        self._condition_expression = None
        self._alarm_level = None
        self.discriminator = None

        self.condition_expression = condition_expression
        self.alarm_level = alarm_level

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this AlarmCondition.

        **参数解释：** 触发告警的条件表达式。 **约束限制：** - 不支持纯数字。 - 不支持以数字开头的。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The condition_expression of this AlarmCondition.
        :rtype: str
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this AlarmCondition.

        **参数解释：** 触发告警的条件表达式。 **约束限制：** - 不支持纯数字。 - 不支持以数字开头的。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param condition_expression: The condition_expression of this AlarmCondition.
        :type condition_expression: str
        """
        self._condition_expression = condition_expression

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmCondition.

        **参数解释：** 触发的告警级别。 **约束限制：** 不支持纯数字，不支持以数字开头的。 **取值范围：** - Info：提示 - Minor：次要 - Major：重要 - Critical：紧急 **默认取值：** 不涉及。

        :return: The alarm_level of this AlarmCondition.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmCondition.

        **参数解释：** 触发的告警级别。 **约束限制：** 不支持纯数字，不支持以数字开头的。 **取值范围：** - Info：提示 - Minor：次要 - Major：重要 - Critical：紧急 **默认取值：** 不涉及。

        :param alarm_level: The alarm_level of this AlarmCondition.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

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
        if not isinstance(other, AlarmCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
