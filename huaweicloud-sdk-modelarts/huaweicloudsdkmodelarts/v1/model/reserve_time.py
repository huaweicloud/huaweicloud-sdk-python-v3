# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReserveTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_unit': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'time_unit': 'time_unit',
        'duration': 'duration'
    }

    def __init__(self, time_unit=None, duration=None):
        r"""ReserveTime

        The model defined in huaweicloud sdk

        :param time_unit: **参数解释**：时间单位。  **约束限制**：不涉及。  **取值范围**：  - HOURS：小时   **默认取值**：不涉及。
        :type time_unit: str
        :param duration: **参数解释**：保留时长。  **约束限制**：不涉及。  **取值范围**：最小值为1。  **默认取值**：不涉及。
        :type duration: int
        """
        
        

        self._time_unit = None
        self._duration = None
        self.discriminator = None

        self.time_unit = time_unit
        self.duration = duration

    @property
    def time_unit(self):
        r"""Gets the time_unit of this ReserveTime.

        **参数解释**：时间单位。  **约束限制**：不涉及。  **取值范围**：  - HOURS：小时   **默认取值**：不涉及。

        :return: The time_unit of this ReserveTime.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this ReserveTime.

        **参数解释**：时间单位。  **约束限制**：不涉及。  **取值范围**：  - HOURS：小时   **默认取值**：不涉及。

        :param time_unit: The time_unit of this ReserveTime.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def duration(self):
        r"""Gets the duration of this ReserveTime.

        **参数解释**：保留时长。  **约束限制**：不涉及。  **取值范围**：最小值为1。  **默认取值**：不涉及。

        :return: The duration of this ReserveTime.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ReserveTime.

        **参数解释**：保留时长。  **约束限制**：不涉及。  **取值范围**：最小值为1。  **默认取值**：不涉及。

        :param duration: The duration of this ReserveTime.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, ReserveTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
