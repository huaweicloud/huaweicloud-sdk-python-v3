# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordsAlarmConditions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'str',
        'number': 'int',
        'alarm_level': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'number': 'number',
        'alarm_level': 'alarm_level'
    }

    def __init__(self, condition=None, number=None, alarm_level=None):
        r"""KeywordsAlarmConditions

        The model defined in huaweicloud sdk

        :param condition: **参数解释：** 触发条件，即满足该条件时，会触发告警。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type condition: str
        :param number: **参数解释：** 匹配条数。当关键词搜索结果的日志条数达到设定的条数时，会触发告警。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type number: int
        :param alarm_level: **参数解释：** 告警级别。 **约束限制：** 不涉及。 **取值范围：** -   Info：提示 -   Minor：次要 -   Major：重要 -   Critical：紧急 **默认取值：** 不涉及。
        :type alarm_level: str
        """
        
        

        self._condition = None
        self._number = None
        self._alarm_level = None
        self.discriminator = None

        self.condition = condition
        self.number = number
        self.alarm_level = alarm_level

    @property
    def condition(self):
        r"""Gets the condition of this KeywordsAlarmConditions.

        **参数解释：** 触发条件，即满足该条件时，会触发告警。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The condition of this KeywordsAlarmConditions.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this KeywordsAlarmConditions.

        **参数解释：** 触发条件，即满足该条件时，会触发告警。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param condition: The condition of this KeywordsAlarmConditions.
        :type condition: str
        """
        self._condition = condition

    @property
    def number(self):
        r"""Gets the number of this KeywordsAlarmConditions.

        **参数解释：** 匹配条数。当关键词搜索结果的日志条数达到设定的条数时，会触发告警。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The number of this KeywordsAlarmConditions.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this KeywordsAlarmConditions.

        **参数解释：** 匹配条数。当关键词搜索结果的日志条数达到设定的条数时，会触发告警。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param number: The number of this KeywordsAlarmConditions.
        :type number: int
        """
        self._number = number

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this KeywordsAlarmConditions.

        **参数解释：** 告警级别。 **约束限制：** 不涉及。 **取值范围：** -   Info：提示 -   Minor：次要 -   Major：重要 -   Critical：紧急 **默认取值：** 不涉及。

        :return: The alarm_level of this KeywordsAlarmConditions.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this KeywordsAlarmConditions.

        **参数解释：** 告警级别。 **约束限制：** 不涉及。 **取值范围：** -   Info：提示 -   Minor：次要 -   Major：重要 -   Critical：紧急 **默认取值：** 不涉及。

        :param alarm_level: The alarm_level of this KeywordsAlarmConditions.
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
        if not isinstance(other, KeywordsAlarmConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
