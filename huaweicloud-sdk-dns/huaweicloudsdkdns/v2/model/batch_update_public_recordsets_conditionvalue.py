# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePublicRecordsetsConditionvalue:

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
        'value': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'value': 'value'
    }

    def __init__(self, condition=None, value=None):
        r"""BatchUpdatePublicRecordsetsConditionvalue

        The model defined in huaweicloud sdk

        :param condition: **参数解释：** 条件信息的键。 **约束限制：** 不涉及。 **取值范围：** - host_name：主机记录。  **默认取值：** 不涉及。
        :type condition: str
        :param value: **参数解释：** 条件信息的值。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type value: str
        """
        
        

        self._condition = None
        self._value = None
        self.discriminator = None

        self.condition = condition
        if value is not None:
            self.value = value

    @property
    def condition(self):
        r"""Gets the condition of this BatchUpdatePublicRecordsetsConditionvalue.

        **参数解释：** 条件信息的键。 **约束限制：** 不涉及。 **取值范围：** - host_name：主机记录。  **默认取值：** 不涉及。

        :return: The condition of this BatchUpdatePublicRecordsetsConditionvalue.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this BatchUpdatePublicRecordsetsConditionvalue.

        **参数解释：** 条件信息的键。 **约束限制：** 不涉及。 **取值范围：** - host_name：主机记录。  **默认取值：** 不涉及。

        :param condition: The condition of this BatchUpdatePublicRecordsetsConditionvalue.
        :type condition: str
        """
        self._condition = condition

    @property
    def value(self):
        r"""Gets the value of this BatchUpdatePublicRecordsetsConditionvalue.

        **参数解释：** 条件信息的值。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The value of this BatchUpdatePublicRecordsetsConditionvalue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this BatchUpdatePublicRecordsetsConditionvalue.

        **参数解释：** 条件信息的值。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param value: The value of this BatchUpdatePublicRecordsetsConditionvalue.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, BatchUpdatePublicRecordsetsConditionvalue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
